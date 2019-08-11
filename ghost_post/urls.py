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

from ghost_post.views import *
from ghost_post.models import *

admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('post', add_post, name='add_post'),
    path('downvote/', down_vote, name='id'),
    path('upvote/', up_vote, name='id'),
    path('boasts', boasts, name='boasts'),
    path('boasts/topvoted', top_voted, name='top_boasts'),
    path('boasts/leastvoted', least_voted, name='least_boasts'),
    path('roasts/topvoted', top_voted, name='top_roasts'),
    path('roasts/leastvoted', least_voted, name='least_roasts'),
    path('roasts', roasts, name='roasts'),
    path('topvoted', top_voted, name='top_voted'),
    path('leastvoted', least_voted, name='least_voted'),
    path('delete/', delete_post, name='id')
]
