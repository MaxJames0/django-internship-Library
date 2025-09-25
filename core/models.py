from django.db import models

# Create your models here.


class Contact_us(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    your_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.your_name} | {self.your_email}'
    
