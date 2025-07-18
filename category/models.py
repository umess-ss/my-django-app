from django.db import models
from blogs.utils.slug import generate_unique_slug
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):
        if not self.pk or Category.objects.get(pk=self.pk).name != self.name:
            self.slug = generate_unique_slug(Category, self.name)
        super().save(*args,**kwargs)


    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name