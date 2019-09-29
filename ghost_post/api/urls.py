from django.conf.urls import include, url
from ghost_post.api.views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'post', PostViewSet, basename='post')
# router.register(r'upvote', up_vote, basename='upvote')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'%^api/auth', include('rest_framework.urls'))
]