from django.db import models
from post.models import Post

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        db_table = 'feedbacks'