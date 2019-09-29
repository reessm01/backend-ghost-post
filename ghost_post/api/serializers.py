from rest_framework.serializers import HyperlinkedModelSerializer
from ghost_post.models import *


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'is_boast',
            'vote_count',
            'created_at',
        )
