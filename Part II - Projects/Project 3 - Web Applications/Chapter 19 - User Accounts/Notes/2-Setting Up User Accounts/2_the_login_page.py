"""
We'll first implement a login page. We'll use the default login view Django provides, so the
URL pattern for this app looks a little different. Make a new urls.py file in the directory
learning_log/users/, and add the following to it:
"""

# users/urls.py

"""Defines URL patterns for users."""


from django.urls import path, include
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]

"""
We import the path function, and then import the include function so we can include some
default authentication URLs that Django has defined. These default URLs include named URL
patterns, such as 'login' and 'logout'. We set the variable app_name to 'users' so Django can 
distinguish these URLs from URLs belonging to other apps(line 13). Even default URLs provided
by Django, when included in the users app's urls.py file, will be accessible through the users
namespace.

The login page's pattern matches the URL http://localhost:8000/users/login/ (line 16). When
Django reads this URL, the word users tells Django to look in users/urls.py, and login tells
it to send requests to Django's default login view.
"""
