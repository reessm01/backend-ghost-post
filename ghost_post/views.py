from django.shortcuts import render, HttpResponseRedirect, reverse

from ghost_post.models import *
from ghost_post.forms import *

def add_post(request, *args, **kwargs):
    if request.method == 'GET':
        page = 'generic_form.html'
        button_label = 'Ghost it'
        form = PostForm()
        return render(request, page, {'form': form, 'button_label': button_label})
    # else:
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         u = request.user
    #         Recipe.objects.create(
    #             title=data['title'],
    #             description=data['description'],
    #             time_rq=data['time_rq'],
    #             instructions=data['instructions'],
    #             author=Author.objects.get(user=u)
    #         )
    #     return HttpResponseRedirect(reverse('homepage'))