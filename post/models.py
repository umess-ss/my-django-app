from django.db import models
from category.models import Category
from django.utils.text import slugify
from blogs.utils.slug import generate_unique_slug
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    created_at =models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.pk or Post.objects.get(pk=self.pk).title != self.title:
            self.slug = generate_unique_slug(Post, self.title)
        super().save(*args,**kwargs)



    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title
    



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post}'
