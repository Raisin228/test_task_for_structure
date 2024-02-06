from storages.backends.s3boto3 import S3Boto3Storage


class YandexCloudStorage(S3Boto3Storage):

    """We explicitly specify Django now we will store files in the YCS, and
    also we write minimal settings"""
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = True
