from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=280)
    is_boast = models.BooleanField(default=True)
    upvote_counts = models.IntegerField(default=0)
    downvote_counts = models.IntegerField(default=0)