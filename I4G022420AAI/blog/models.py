from time import timezone
from django.db import models

# Create your models here.
class post (models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField()
  author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='blog_posts')
  created_date = models.DateTimeField(auto_now_add=True)
  publshed_date = models.DateTimeField(default=timezone.now)
