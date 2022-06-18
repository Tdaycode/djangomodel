from django.db import models

# Create your models here.


class Post:
    title = models.CharField(max_length=200, string=True)
    text = models.TextField()
    author = models.get_user_model()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
