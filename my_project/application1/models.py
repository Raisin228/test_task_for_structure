from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


def user_directory_path_by_images(instance, filename):
    """Путь по которому сохраняются изображения на сервере"""
    return f'user_{instance.user.id}/images/{datetime.now().strftime("%Y-%m-%d")}/{filename}'


def user_directory_path_by_files(instance, filename):
    """Путь по которому сохраняются файлы на сервере"""
    return f'user_{instance.user.id}/files/{datetime.now().strftime("%Y-%m-%d")}/{filename}'


class Any_file(models.Model):
    """Модель для хранения файла/изображения + некое общее имя"""
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    some_name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to=user_directory_path_by_images)
    file = models.FileField(upload_to=user_directory_path_by_files)

    def __str__(self):
        return self.some_name
