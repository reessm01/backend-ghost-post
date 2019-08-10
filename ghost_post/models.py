from django.db import models

class post(models.Model):
    text = models.CharField(max_length=280)
    is_boast = models.BooleanField(default=True)
    upvote_counts = models.IntegerField()
    downvote_counts = models.IntegerField()