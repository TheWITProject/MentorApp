
# Mentor App ReadMe

  

## Clone me

`$ git clone https://github.com/TheWITProject/MentorApp.git`


## Setup

`$ cd MentorApp/`
`$ python3 -m venv myvenv`
`$ source myvenv/bin/activate`
` $ pip install -r requirements.txt`
` $ CREATE USER name;`
` $ CREATE DATABASE mentorapp OWNER name;`
` $ python manage.py migrate`
` $ python manage.py createsuperuser --username name`
password
` $ python manage.py runserver`