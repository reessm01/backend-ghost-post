from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, Response
from ghost_post.api.serializers import *
from ghost_post.models import *

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all()[::-1]

# class up_vote(APIView):
#     def get(self, request, *args, **kwargs):
#         post_id = int(request.GET.get('id'))
#         post = Post.objects.get(id=post_id)
#         post.vote_count += 1
#         post.save()

#         return Response(status=200)
