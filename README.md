### Description

---

In this repository i created backend application that allow superuser of website 
using django admin store them files to the yandex object storage. 

This way very useful because it helps to avoid some problems. 

Problems that you avoid use this method:

- You will be able to spend less money to rent your server. Usually simple server cost more money so store 
information on the cloud more profitably.
- Your data are located more security because cloud provider every day work with his security to protect 
your information.
- etc...

### Run backend

---

*First step*
* You need to clone repository to your local pc.\
`git clone https://github.com/Raisin228/storing-files-in-the-yandex-cloud.git`
* Go to directory with file .gitignore and create virtual environment.\
`python -m venv venv`
* Activate your venv.\
`venv/Scripts/activate`
* Install requirements from requirements.txt by command in terminal.
`pip install -r requirements.txt`

*Second step*
* You need to create account in 
<a href='https://cloud.yandex.ru/ru/'>yandex cloud</a>.
* After make simple steps to set up your backet. You can follow tips from the <a href='https://www.youtube.com/watch?v=L_6PiJFaldI'>video</a>.
* Make .env file nearby with venv folder and paste this code.
  ```
  ID_KEY = {Your key}
  SECRET_KEY = {Your secret key}
  BUCKET_NAME = {Your bucket name}
  ```

*Third step*
* You need to make migrations. Go to src folder. Note you need to be in the same
directory with manage.py and write.\
`python mange.py migrate`
* Create superuser.\
`python manage.py createsuperuser`

*Forty step*
* Run server\
`python mange.py runserver`

It's all!! I hope everything worked out for you and you didn't dance with 
a tambourine. Go to admin page and try to upload your files. 

### Technology stack 

---

1. [Python3](https://www.python.org/) - program language
2. [Yandex Cloud](https://cloud.yandex.ru/ru/) - s3 analog
3. [Django 5.0.1](https://www.djangoproject.com/) - backend framework
4. [SQLite](https://www.sqlite.org/index.html) - database for storing links to user files

### Project's photo

---

### Uploading files
<img src="https://github.com/Raisin228/storing-files-in-the-yandex-cloud/blob/main/screenshots/Django%20admin%20with%20file.png">

### Database after files was upload
<img src="https://github.com/Raisin228/storing-files-in-the-yandex-cloud/blob/main/screenshots/DB.png">

### YOS with files
<img src="https://github.com/Raisin228/storing-files-in-the-yandex-cloud/blob/main/screenshots/Files%20uploded%20to%20the%20cloud.png">

