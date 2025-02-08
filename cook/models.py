from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    # Категория новостей
    title = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class Post(models.Model):
    title = models.CharField(max_length = 255, verbose_name = "название")
    content = models.TextField(default = "Скоро будет текст", verbose_name = "текст статьи")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "время создания")
    update_at = models.DateTimeField(auto_now = True, verbose_name = "обноаление")
    photo = models.ImageField(upload_to="photos/", blank = True,  null = True, verbose_name = "фото")
    wathed = models.IntegerField(default = 0, verbose_name = "просмотрено")
    is_published = models.BooleanField(default = True, verbose_name = "публикация")
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = "категория")
 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = "Пост" )
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "пользователь" )
    text = models.TextField(verbose_name = "коментарий")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    
    
    def __str__(self):
        return self.text
    
    
    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'коментарии'