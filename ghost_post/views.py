from django.shortcuts import render, HttpResponseRedirect, reverse

from ghost_post.models import *
from ghost_post.forms import *

def index(request, *args, **kwargs):
    page = 'index.html'

    posts = Post.objects.all()

    return render(request, page, {'posts': posts[::-1]})

def up_vote(request, *args, **kwargs):
    post_id = int(request.GET.get('id'))    
    post = Post.objects.get(id=post_id)
    post.vote_count += 1
    post.save()

    page = 'index.html'
    posts = Post.objects.all()
    return render(request, page, {'posts': posts[::-1]})

def down_vote(request, *args, **kwargs):
    post_id = int(request.GET.get('id'))    
    post = Post.objects.get(id=post_id)
    post.vote_count -= 1
    post.save()

    page = 'index.html'
    posts = Post.objects.all()
    return render(request, page, {'posts': posts[::-1]})

def add_post(request, *args, **kwargs):
    page = 'generic_form.html'
    button_label = 'Ghost it'
    form = PostForm(initial={'is_boast': '1'})
    if request.method == 'GET':
        return render(request, page, {'form': form, 'button_label': button_label})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            is_boast = True if data['is_boast'] == '1' else False
            Post.objects.create(
                text=data['text'],
                is_boast=is_boast,
            )
        # return HttpResponseRedirect(reverse('homepage'))
        message = 'Successfully saved'
        return render(request, page, {'form': form, 'button_label': button_label, 'message': message})