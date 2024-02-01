import uuid
from datetime import datetime
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

from application1.storage_backends import YandexCloudStorage
from my_project.settings import AWS_S3_CUSTOM_DOMAIN


def user_directory_path_by_images(request, filename: str) -> str:
    """Путь по которому сохраняются изображения на сервере"""
    # что бы не было проблем с коллизиями файлов
    uniq_id = uuid.uuid4()
    f_name = str(uniq_id)[:5] + '_' + filename
    return f'media/users/images/{datetime.now().strftime("%Y-%m-%d")}/{f_name}'


def user_directory_path_by_files(request, filename: str) -> str:
    """Путь по которому сохраняются файлы на сервере"""
    uniq_id = uuid.uuid4()
    f_name = str(uniq_id)[:5] + '_' + filename
    return f'media/users/files/{datetime.now().strftime("%Y-%m-%d")}/{f_name}'


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


class AnyFile(models.Model):
    """Модель для хранения файла/изображения + некое общее имя"""
    some_name = models.CharField(max_length=50, unique=True)
    image = YandexImageField(upload_to=user_directory_path_by_images, storage=YandexCloudStorage())
    file = YandexFileField(upload_to=user_directory_path_by_files, storage=YandexCloudStorage())

    def __str__(self):
        return self.some_name
