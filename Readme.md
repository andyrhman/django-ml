# Django ML

<p align="center">
  <img src="https://1000logos.net/wp-content/uploads/2020/08/Django-Logo.png" width="300" height="200" />
</p>

## Introduction

This is my 4th project of django web framework, this project is for Machine Learning model integration to REST API using library like Tensorflow & Keras.

## First Time Set Up & Configuration

Install the Django Web Framework:

```bash
sudo apt update && sudo apt install python3.10 python3.10-venv python3.10-dev # tensorflow only exist in 3.10 for now
sudo apt update && sudo apt install libgl1-mesa-glx # For OpenCV
pip install django
pip install djangorestframework   
pip install django-filter
pip install python-decouple
pip install pandas
pip install numpy
pip install opencv-python
pip install tensorflow
```

Create the directory:

```bash
mkdir django-auth
django-admin startproject app .
django-admin startapp <folder name>

```

## Adding first migration

Before you use docker create the app and the model
```bash
django-admin startapp <folder name>
python3 manage.py makemigrations
python manage.py migrate
python3 manage.py runserver
python manage.py createsuperuser --email test3@mail.com
```

Go To settings.py and add this:

```python
INSTALLED_APPS = [
  // other lists,
  "rest_framework",
  "core"
]
```

## Features

List the main features of your autth server. For example:
- User authentication and authorization
- Auth Token
- 2FA Authentication

## Installation

Provide step-by-step instructions for installing and setting up the project locally. Include commands and any additional configurations. For example:

```bash
git clone https://github.com/andyrhman/django-ambassador.git
cd django-ambassador
pip install -r requirements.txt