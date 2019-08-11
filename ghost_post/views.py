from django.shortcuts import render, HttpResponseRedirect, reverse, render_to_response

from ghost_post.models import *
from ghost_post.forms import *

def index(request, *args, **kwargs):
    page = 'index.html'

    posts = Post.objects.all()

    return render(request, page, {'posts': posts[::-1]})

def up_vote(request, *args, **kwargs):
    page = 'index.html'

    post_id = int(request.GET.get('id'))    
    post = Post.objects.get(id=post_id)
    post.vote_count += 1
    post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def down_vote(request, *args, **kwargs):
    post_id = int(request.GET.get('id'))    
    post = Post.objects.get(id=post_id)
    post.vote_count -= 1
    post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_posts(is_boast):
    return Post.objects.all().filter(is_boast=is_boast)

def boasts(request, *args, **kwargs):
    page = 'index.html'

    boast_posts = get_posts(True)

    return render(request, page, {'posts': boast_posts[::-1]})

def roasts(request, *args, **kwargs):
    page = 'index.html'

    roast_posts = get_posts(False)

    return render(request, page, {'posts': roast_posts[::-1]})

def top_voted(request, *args, **kwargs):
    page = 'index.html'
    posts = get_posts_conditionally(request)
    posts = posts_by_votes(True, posts)

    return render(request, page, {'posts': posts})

def least_voted(request, *args, **kwargs):
    page = 'index.html'
    posts = get_posts_conditionally(request)
    posts = posts_by_votes(False, posts)

    return render(request, page, {'posts': posts})

def get_posts_conditionally(request):
    if 'boast' in request.path:
        return get_posts(True)
    elif 'roast' in request.path:
        return get_posts(False)
    else:
        return Post.objects.all()

def posts_by_votes(sort_by_top, posts):
    return sorted(posts, key=lambda post: post.vote_count, reverse=sort_by_top)

def add_post(request, *args, **kwargs):
    page = 'generic_form.html'
    button_label = 'Ghost it'
    form = PostForm(initial={'is_boast': '1'})
    method = 'POST'
    if request.method == 'GET':
        return render(request, page, {'form': form, 'button_label': button_label, 'method': method})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            is_boast = True if data['is_boast'] == '1' else False
            Post.objects.create(
                text=data['text'],
                is_boast=is_boast,
            )

            key = Post.objects.all()[0].random_string
            message = 'Post successfully saved!\n If you want to delete your message later save this key {}.'.format(key)
            return render(request, page, {'form': form, 'button_label': button_label, 'message':message})

def delete_post(request, *args, **kwargs):
    # Could not figure out why the http method delete wouldn't work, so gave up on that idea
    post_id = int(request.GET.get('id')) if request.GET.get('id') else None
    page = 'generic_form.html'
    button_label = 'Delete it'
    post = Post.objects.all().filter(id=post_id)
    if post:
        post_text = post[0].text
        warning_message = 'Enter the secret string that you were given after this post was created:'
        form = DeleteForm(request.POST)
        if not form.is_valid():
            form = DeleteForm(initial={'magic_string':''})
            return render(request, page, {'form': form, 'button_label': button_label, 'warning_message': warning_message, 'post_text': post_text})
        else:
            post_id = int(request.GET.get('id'))
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.get(id=post_id)
                if post.magic_string == data['magic_string']:
                    post.delete()
                    return HttpResponseRedirect(reverse('homepage'))
                else:
                    print('this one happened')
                    error_message = 'Incorrect magic string. Please try again.'
                return render(request, page, {'form': form, 'button_label': button_label, 'warning_message': warning_message, 'post_text': post_text, 'error_message':error_message})
    else:
        return HttpResponseRedirect(reverse('homepage'))