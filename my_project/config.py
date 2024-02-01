from dotenv import load_dotenv
import os

load_dotenv('../.env')

YANDEX_ID_KEY: str = os.getenv('ID_KEY')

YANDEX_SECRET_KEY: str = os.getenv('SECRET_KEY')
YANDEX_BUCKET_NAME: str = os.getenv('BUCKET_NAME')

