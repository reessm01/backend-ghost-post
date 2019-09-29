from django.shortcuts import render, HttpResponseRedirect, reverse, render_to_response, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView
from django.middleware.csrf import get_token
import json

from ghost_post.models import *
from ghost_post.forms import *
from ghost_post.api.serializers import PostSerializer

class csrf(TemplateView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'csrfToken': get_token(request)})


class index(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()[::-1]
        posts_json = serializers.serialize('json', posts)
        
        return HttpResponse(posts_json, content_type='application/json')


class up_vote(TemplateView):
    def get(self, request, *args, **kwargs):
        post_id = int(request.GET.get('id'))
        post = Post.objects.get(id=post_id)
        post.vote_count += 1
        post.save()

        return HttpResponse(status=200)


class down_vote(TemplateView):
    def get(self, request, *args, **kwargs):
        post_id = int(request.GET.get('id'))
        post = Post.objects.get(id=post_id)
        post.vote_count -= 1
        post.save()

        return HttpResponse(status=200)


def get_posts(is_boast):
    return Post.objects.all().filter(is_boast=is_boast)


class boasts(TemplateView):
    def get(self, request, *args, **kwargs):
        boast_posts = get_posts(True)[::-1]
        boasts_json = serializers.serialize('json', boast_posts)

        return HttpResponse(boasts_json, content_type='application/json')


class roasts(TemplateView):
    def get(self, request, *args, **kwargs):
        roast_posts = get_posts(False)[::-1]
        roasts_json = serializers.serialize('json', roast_posts)

        return HttpResponse(roasts_json, content_type='application/json')


class top_voted(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = get_posts_conditionally(request)
        posts = posts_by_votes(True, posts)
        posts_json = serializers.serialize('json', posts)

        return HttpResponse(posts_json, content_type='application/json')


class least_voted(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = get_posts_conditionally(request)
        posts = posts_by_votes(False, posts)
        posts_json = serializers.serialize('json', posts)

        return HttpResponse(posts_json, content_type='application/json')


def get_posts_conditionally(request):
    if 'boast' in request.path:
        return get_posts(True)
    elif 'roast' in request.path:
        return get_posts(False)
    else:
        return Post.objects.all()


def posts_by_votes(sort_by_top, posts):
    return sorted(posts, key=lambda post: post.vote_count, reverse=sort_by_top)


class add_post(TemplateView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        form = PostForm(data)
        is_boast = True if data['is_boast'] == 0 else False
        new_post = Post.objects.create(
            text=data['text'],
            is_boast=is_boast,
        )

        new_post = serializers.serialize('json', [new_post, ])
        print(new_post)
        
        return HttpResponse(new_post, content_type='application/json')


class delete_post(TemplateView):
    def delete(self, request, *args, **kwargs):
        magic = request.GET.get('magic')
        post = Post.objects.filter(magic_string=magic)
        if post:
            post[0].delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
