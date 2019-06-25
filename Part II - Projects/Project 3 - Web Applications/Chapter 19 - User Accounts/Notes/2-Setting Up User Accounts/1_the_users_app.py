"""
In this section, we'll set up a user registration and authorization system so people can
register an account and log in and out. We'll create a new app to contain all the functionality
related to working with users. We'll use the default user authentication system included with
Django to do as much of the work as possible. We'll also modify the Topic model slightly so
every topic belongs to a certain user.

We'll start by creating a new app called users, using the startapp command:
"""

python manage.py startapp users

ls
# db.sqlite3  learning_log/  learning_logs/  ll_env/  manage.py*  users/

ls users
# __init__.py  admin.py  apps.py  migrations/  models.py  tests.py  views.py


"""
This command makes a new directory called users(line 14) with a structure identical to the
learning_logs app(line 17).
"""

# # Adding users to settings.py

"""
We need to add our new app to INSTALLED_APPS in settings.py, like so:
"""

# settings.py
--snip--
INSTALLED_APPS = [
    # My apps.
    'learning_logs',
    'users',

    # Default Django apps.
    --snip--
]

"""
Now Django will include the users app in the overall project.
"""

# # Including the URLs from users

"""
Next, we need to modify the root urls.py so it includes the URLs we write for the users app:
"""

# learning_log/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users.url)),
    path('', include('learning_logs.urls')),
]

"""
We add a line to include the file urls.py from users. This line will match any URL that 
starts with the word users, such as http://localhost:8000/users/login/.
"""
