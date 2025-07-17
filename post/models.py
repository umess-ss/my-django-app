from django.db import models
from category.models import Category
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    created_at =models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = base_slug
        super().save(*args,**kwargs)


    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title