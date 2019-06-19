"""
To use our models, we have to tell Django to include our app in the overall project. Open
settings.py(In the learning_lob/learning_log directory); you'll see a section that tells Django
which apps are installed and work together in the project:
"""

# settings.py

--snip--
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
--snip--

"""
Add our app to this list by modifying INSTALLED_APPS so it looks like this:
"""

INSTALLED_APPS = [
    # My apps.
    'learning_logs',

    # Default Django apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

"""
Grouping apps together in a project helps to keep track of them as the project grows to include
more apps. Here we start a section called My apps, which includes only learning_logs for now.
It's important to place your own apps BEFORE the default apps in case you need to override any
behaviour of the default apps with your own custom behaviour.

Next we need to tell Django to modify the database so it can store information related to the
model Topic. From the terminal, run the following command:
"""

python manage.py makemigrations learning_logs

# Migrations for 'learning_logs':
#   learning_logs\migrations\0001_initial.py
#     - Create model Topic


"""
The command makemigrations tells Django to figure out how to modify the database so it can store 
the data associated with any new models we've defined. The output here shows that Django has
created a migration fille called 0001_initial.py. This migration will create a table for the 
model Topic in the database.

Now we'll apply this migration and have Django modify the database for us:
"""

python manage.py migrate

# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
# Running migrations:
#   Applying learning_logs.0001_initial... OK

"""
Most of the output from this command is identical to the first time we issued the migrate
command. The line we need to check appears at line 68, where Django confirms that the migration
for learning_logs worked OK.

Whenever we want to modify the data that Learning Log manages, we'll follow these three steps:
    Modify models.py
    Call makemigrations on learning_logs
    Tell Django to migrate the project.
"""
