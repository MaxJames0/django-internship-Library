import time
from django.utils.text import slugify


def image_upload_user(instance, filename):
    path = 'uploads/' + 'user/' + slugify(instance.username, allow_unicode=True) 
    name = str(time.time()) + '_' + str(instance.username) + "_" + filename
    return path + '/' + name
    