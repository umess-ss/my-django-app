from django.db import models
from category.models import Category
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    created_at =models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title