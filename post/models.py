from django.db import models
from category.models import Category
from django.utils.text import slugify
from blogs.utils.slug import generate_unique_slug


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