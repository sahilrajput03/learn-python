# Learn django

**Getting Started with django:** [Click here](https://www.djangoproject.com/start/)

Continue from: https://docs.djangoproject.com/en/4.0/intro/tutorial03/#raising-a-404-error

```bash
# Starting a new project named `mysite`
django-admin startproject mysite

# Start the dev server
cd mysite
python manage.py runserver
# Browse @ http://localhost:8000/

# create web app in our project
python manage.py startapp polls

## Important files
mysite/mysite/urls.py
mysite/polls/urls.py
mysite/polls/views.py

# Added settings for db config in file: `mysite/mysite/settings.py` # src: Setting up postgres with django: https://youtu.be/KqcS3P32s6Y
# BEWARE: pgadmin is actually a good ui manager for postgres, src above^^.
# Instlled for postgres support
sudo pacman -S python-psycopg2
# Seup migrations and migrate to db
python manage.py makemigrations # ~ This is not specified in django docs though.
python manage.py migrate
# That'll fill the database with appropriate data and you would be able to see lots of tables created by command:
psql -d django_app1 -U postgres -c "\d"
# See the database via psql:

# Creating a super user:
python manage.py createsuperuser # use username as `admin` and choose some passwd.


## ~Sahil, Migrating models after adding Mode definition in `polls/models.py` and adding `polls` app i.e., `polls.apps.PollsConfig` to array i.e., `INSTALLED_APPS` in `mysite/settings.py`.
# DJANGO DOCS: By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration. ** Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.
python manage.py makemigrations polls


# DJANGO DOCS: The sqlmigrate command takes migration names and returns their SQL:
python manage.py sqlmigrate polls 0001 # ~Sahil, Here 0001 is the number on the filenames in `polls/migrations/` directory.


# DJANGO DOCS: You can also run python manage.py check; this checks for any problems in your  without making migrations or touching the database.
python manage.py check;
# Output (default):
# System check identified no issues (0 silenced).


# DJANGO DOCS: Now, run migrate again to create those model tables in your database. The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.
python manage.py migrate


# Remember the three-step guide to making model changes: (SHORT NOTES FROM django)
# 1. Change your models (in models.py).
# 2. Run python manage.py makemigrations to create migrations for those changes
# 3. Run python manage.py migrate to apply those changes to the database.


## Creating superuser
python manage.py createsuperuser ## admin,sahilrajput03@gmail.com, password: <same as archlinux user>
# Now you can browse admin section via: http://localhost:8000/admin/
```

source: https://docs.djangoproject.com/en/4.0/intro/tutorial01/

Directory structure

```txt
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

These files are:

- The outer `mysite/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [`django-admin` and `manage.py`](https://docs.djangoproject.com/en/4.0/ref/django-admin/).
- The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
- `mysite/__init__.py`: **An empty file that tells Python that this directory should be considered a Python package.** If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
- `mysite/settings.py`: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/4.0/topics/settings/) will tell you all about how settings work.
- `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/).
- `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/) for more details.
- `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/) for more details.

## What is wsgi and asgi?

```txt
WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.

WSGI is a Python standard described in detail in PEP 3333.
src: https://wsgi.readthedocs.io/en/latest/what.html
```

**Only things you need to know between wsgi and asgi:** https://medium.com/analytics-vidhya/difference-between-wsgi-and-asgi-807158ed1d4c

- ASGI is successor of WSGI. WSGI did not have asynchronous callables.

- Lean how to deploy with ASGI: https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/

# Command Logs

```bash
python manage.py makemigrations
# OUTPUT:
No changes detected



python manage.py migrate
# OUTPUT:
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK



## THIS IS FROM DJANGO'S DOCS:
python manage.py makemigrations polls
# OUTPUT:
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice

```

Sql sampled output form commands:

```sql
--- THIS IS FORM DJANGO'S DOCS
python manage.py sqlmigrate polls 0001
-- Output:
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" integer NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

COMMIT;
```

bash related commands:

```bash
python manage.py migrate
# Output:
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK


## Creating superuser
python manage.py createsuperuser
# OUTPUT:
Username (leave blank to use 'array'): admin
Email address: sahilrajput03@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
