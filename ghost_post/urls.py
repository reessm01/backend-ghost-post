"""ghost_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from ghost_post.views import *
from ghost_post.models import *

# admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='homepage'),
    path('post', csrf_exempt(add_post.as_view()), name='add_post'),
    path('downvote/', down_vote.as_view(), name='id'),
    path('upvote/', up_vote.as_view(), name='id'),
    path('boasts', boasts.as_view(), name='boasts'),
    path('roasts', roasts.as_view(), name='roasts'),
    path('topvoted', top_voted.as_view(), name='top_voted'),
    path('leastvoted', least_voted.as_view(), name='least_voted'),
    path('delete/', csrf_exempt(delete_post.as_view()), name='id'),
    path('token', csrf.as_view())
]
