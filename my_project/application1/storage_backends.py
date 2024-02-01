from storages.backends.s3boto3 import S3Boto3Storage


class YandexCloudStorage(S3Boto3Storage):
    """Явно указываем Django что теперь файлы будут храниться в YCS.
    Задаём минимальные настройки"""
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = True
