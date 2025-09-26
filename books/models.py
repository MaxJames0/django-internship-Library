from django.db import models
from django.contrib.auth import get_user_model
from .utils import image_upload_book
from django.utils.text import slugify
from extensions.utils import jalali_converter   
from .models import *

# Create your models here.


Users = get_user_model()


class BookCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='دسته بندی')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')

    def __str__(self):
        return self.name

    def jcreated_at(self):
        return jalali_converter(self.created_at)
    jcreated_at.short_description = "ساخته شده در"


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(unique=True, blank=True)
    desc = models.TextField(verbose_name='توضیحات کوتاه')
    categories = models.ManyToManyField('books.BookCategory', related_name='books', verbose_name='دسته بندی')
    author = models.CharField(max_length=150, verbose_name='نویسنده')
    added_by = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='اضافه شده توسط')
    cover_image = models.ImageField(upload_to=image_upload_book, verbose_name='کاور کتاب')
    is_published = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='اضافه شده در')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='بروز شده در')
    is_borrowed = models.BooleanField(default=False, verbose_name='در امانت؟')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} | {self.author}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def jcreated_at(self):
        return jalali_converter(self.created_at)
    jcreated_at.short_description = "اضافه شده در"
    
    
class CommentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='author')
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} | {self.book.title[:10]}'
    
    
class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows', verbose_name='کتاب')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='borrowed_books', verbose_name='کاربر')
    borrowed_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ امانت')
    returned = models.BooleanField(default=False, verbose_name='تحویل داده شده؟')

    class Meta:
        ordering = ['-borrowed_at']

    def __str__(self):
        return f'{self.user} | {self.book.title} | {"تحویل داده شده" if self.returned else "در امانت"}'
    
    def jborrowed_at(self):
        return jalali_converter(self.borrowed_at)
    jborrowed_at.short_description = "امانت گرفته شده در"

