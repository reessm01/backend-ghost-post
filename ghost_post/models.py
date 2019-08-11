from django.db import models
from django.utils.crypto import get_random_string

class Post(models.Model):
    random_string = get_random_string(length=6)
    text = models.CharField(max_length=280)
    is_boast = models.BooleanField(default=True)
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    magic_string = models.CharField(default=random_string, max_length=6)