from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from storages.backends.s3boto3 import S3Boto3Storage

from my_project.settings import AWS_S3_CUSTOM_DOMAIN


class YandexStorage(S3Boto3Storage):
    """Предоставляет базовый функционал для работы с YS"""

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = AWS_S3_CUSTOM_DOMAIN
        super().__init__(*args, **kwargs)


class YandexImageField(models.ImageField):
    """Теперь изображения будут храниться не в S3 а в YS"""

    def __init__(self, *args, **kwargs):
        kwargs['storage'] = YandexStorage()
        super().__init__(*args, **kwargs)


class YandexFileField(models.FileField):
    """Теперь файлы будут храниться не в S3 а в YS"""

    def __init__(self, *args, **kwargs):
        kwargs['storage'] = YandexStorage()
        super().__init__(*args, **kwargs)


def user_directory_path_by_images(instance, filename: str) -> str:
    """Путь по которому сохраняются изображения на сервере"""
    return f'media/{filename}'
    # return f'user_{instance.user.id}/images/{datetime.now().strftime("%Y-%m-%d")}/{filename}'


def user_directory_path_by_files(instance, filename: str) -> str:
    """Путь по которому сохраняются файлы на сервере"""
    return f'media/{filename}'
    # return f'user_{instance.user.id}/files/{datetime.now().strftime("%Y-%m-%d")}/{filename}'


class AnyFile(models.Model):
    """Модель для хранения файла/изображения + некое общее имя"""
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    some_name = models.CharField(max_length=50, unique=True)
    image = YandexImageField(upload_to=user_directory_path_by_images)
    file = YandexFileField(upload_to=user_directory_path_by_files)

    def __str__(self):
        return self.some_name

    def delete(self, *args, **kwargs):
        # Удаление файла из Yandex Cloud Storage
        self.file.storage.delete(self.file.name)

        # Вызываем стандартный метод удаления
        super(AnyFile, self).delete(*args, **kwargs)
