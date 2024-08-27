from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('Movieapp1:movies_by_category',args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)




class Movie(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    releaseDate = models.DateTimeField()
    actors = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='movie1', blank=True)
    reviews = models.TextField()
    available = models.BooleanField(default=True)
    ratings = models.FloatField()
    youtube_url = models.URLField()


    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'


    def get_url(self):
        return reverse('Movieapp1:movCatdetail',args=[self.category.slug,self.slug])





    def __str__(self):
        return '{}'.format(self.name)

