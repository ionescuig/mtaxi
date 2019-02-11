# MTAXI website

Hosted on: [official page](https://www.mtaxiltd.co.uk) and [heroku](https://mtaxi.herokuapp.com)


Website for a taxi company:
- landing page
  - info about company and other details
- quote page
  - uses quote model
    - different fields validation
    - add quote to database
    - send email from bot email to company's owner email
- thank you page
- admin page
  - quote
    - modified fields to display
    - added filter
    - added search

---

#### Instructions (for Windows)

Create a new project directory:
```
mkdir new-project
cd new-project
```

Clone project from GitHub (do this before anything else, git clone needs an empty folder):
```
git clone https://github.com/ionescuig/mtaxi.git .
```

Create a virtual environment and activate it:
```
virtualenv venv
.\venv\scripts\activate
```

From this moment you will work only in virtual environment `(venv) C:\your-path\new-project\`.

Move to `src` folder and install required packages:
```
cd src
pip install -r requirements.txt
```

Make a copy of `production.py` with the name `local.py` to be able to run the project on your local machine:
```
cp mtaxi\settings\production.py mtaxi\settings\local.py
```

Modify the following fields in `local.py` with your preferred editor:
```
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST_USER = 'your_email'
EMAIL_HOST_PASSWORD = 'your_password'

DEFAULT_FROM_EMAIL = 'from_email'
DEFAULT_TO_EMAIL = 'to_email'

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

```

Create database, create a superuser and run the server:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

From here you can modify the templates (or anything you want) with your details (company name, phone number, email address, ...).

The project is ready for heroku, just modify `ALLOWED_HOSTS` in `production.py` and after setting the heroku project (a tutorial is out of scope) add Heroku Environment Variables for Django keys:
```
heroku config:set SECRET_KEY=<your-django-secret-key>
heroku config:set EMAIL_HOST_USER='your_email'
heroku config:set EMAIL_HOST_PASSWORD='your_password'
heroku config:set DEFAULT_FROM_EMAIL='from_email'
heroku config:set DEFAULT_TO_EMAIL='to_email'
```
