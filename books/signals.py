from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Borrow, Book

@receiver(post_save, sender=Borrow)
def update_book_borrowed_status(sender, instance, **kwargs):
    instance.book.is_borrowed = not instance.returned
    instance.book.save()

@receiver(post_delete, sender=Borrow)
def reset_book_borrowed_status(sender, instance, **kwargs):
    instance.book.is_borrowed = False
    instance.book.save()

