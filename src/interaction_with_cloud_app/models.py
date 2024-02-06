import uuid
from datetime import datetime
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

from interaction_with_cloud_app.storage_backends import YandexCloudStorage
from src.settings import AWS_S3_CUSTOM_DOMAIN
from django.utils.html import format_html


def user_directory_path_by_images(request, filename: str) -> str:
    """The path where the images are saved on the server"""
    # to avoid problems with file collisions
    uniq_id = uuid.uuid4()
    f_name = str(uniq_id)[:5] + '_' + filename
    return f'media/users/images/{datetime.now().strftime("%Y-%m-%d")}/{f_name}'


def user_directory_path_by_files(request, filename: str) -> str:
    """The path where the files are saved on the server"""
    uniq_id = uuid.uuid4()
    f_name = str(uniq_id)[:5] + '_' + filename
    return f'media/users/files/{datetime.now().strftime("%Y-%m-%d")}/{f_name}'


class YandexStorage(S3Boto3Storage):
    """Provides basic functionality for working with YS"""

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = AWS_S3_CUSTOM_DOMAIN
        super().__init__(*args, **kwargs)


class YandexImageField(models.ImageField):
    """Now images will be store in the YS instead of S3"""

    def __init__(self, *args, **kwargs):
        kwargs['storage'] = YandexStorage()
        super().__init__(*args, **kwargs)


class YandexFileField(models.FileField):
    """Now files will be store in the YS instead of S3"""

    def __init__(self, *args, **kwargs):
        kwargs['storage'] = YandexStorage()
        super().__init__(*args, **kwargs)


class AnyFile(models.Model):
    """Model for store files/images + some common name"""
    some_name = models.CharField(max_length=50, unique=True)
    relative_url_image = YandexImageField(upload_to=user_directory_path_by_images, storage=YandexCloudStorage(),
                                          verbose_name='Your Image')
    abs_image_url = models.URLField(blank=True, editable=False)

    relative_url_file = YandexFileField(upload_to=user_directory_path_by_files, storage=YandexCloudStorage(),
                                        verbose_name='Your File')
    abs_file_url = models.URLField(blank=True, editable=False)

    def __str__(self):
        return self.some_name

    def save(self, *args, **kwargs):
        """Before save obj in db we create absolute URL for file and save"""
        super().save(*args, **kwargs)

        # Create absolute links
        if self.relative_url_file:
            self.abs_file_url = f"https://{AWS_S3_CUSTOM_DOMAIN}/{self.relative_url_file}"
        if self.relative_url_image:
            self.abs_image_url = f"https://{AWS_S3_CUSTOM_DOMAIN}/{self.relative_url_image}"
        super().save(*args, **kwargs)

    def url_file(self) -> str:
        """Display absolute link to the file in django admin"""
        return format_html("<a href='%s'>%s</a>" % (self.abs_file_url, self.abs_file_url))

    def url_image(self) -> str:
        """Display absolute link to the image in django admin"""
        return format_html("<a href='%s'>%s</a>" % (self.abs_image_url, self.abs_image_url))
