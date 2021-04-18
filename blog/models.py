from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Категорія(ю)'
        verbose_name_plural = 'Категорії'
        ordering = ['title']
    

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url Tag', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Url публікації', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(verbose_name='Контент', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='К-сть переглядів')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts',
                verbose_name='Категорії')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', 
                verbose_name='Теги')
    is_published = models.BooleanField(default=True, verbose_name='Опублікований')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Публікація(ю)'
        verbose_name_plural = 'Публікації'
        ordering = ['-created_at', 'title']
