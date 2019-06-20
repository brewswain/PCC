"""
Users request pages by entering URLs into a browser and clicking links, so we'll need to decide
what URLs are needed. The home page URL is first: it's the base URL people use to access the
project. At the moment the base URL, http://localhost:8000/, returns the default Django site
that lets us know the project was set up correctly. We'll change this by mapping the base URL
to Learning Log's home page.

In the main learning_log project folder, open the file urls.py. Here's the code you should see:
"""

# learning_log/urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
The first two lines import a module and a function to manage URLs for the admin site(line 13).
The body of the file defines the urlpatterns variable(line 16). In this urls.py file, which
represents the project as a whole, the urlpatterns variable includes sets of URLs from the apps
in the project. The code at line 17 includes the module admin.site.urls, which defines all the
URLs that can be requested from the admin site.

We need to include the URLs for learning_logs, so add the following:
"""
# from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
]

"""
We've added a line to include the module learning_logs.url at line 32.

The default urls.py is in the learning_log folder; now we need to make a second urls.py file
in the learning_logs folder. Create a new Python file and save it as urls.py in learning_logs,
and enter this code into it:
"""

# learning_logs/urls.py

"""Defines URLS patterns for learning_logs."""

# from django.urls import path
# from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]

"""
To make it clear which urls.py we're working in, we add a docstring at the beginning of the 
file(line 45). We then import the path function, which is needed when mapping URLs to views
(line 47). We also import the views module(line 48); the dot tells Python to import the 
views.py module from the same directory as the current urls.py module. The variable app_name
helps Django distinguish this urls.py file from files of the same name in other apps within the
project(line 50). The variable urlpatterns in this module is a list of individual pages that 
can be requested from the learning_logs app(line 51).

The actual URL pattern is a call to the path() function, which takes three arguments(line 53).
The first argument is a string that helps Django route the current request properly. Django 
receives the requested URL and tries to route the request to a view. It does this by searching 
all the URL patterns we've defined to find one that matches the current request. Django ignores
the base URL for the project (http://localhost:8000/), so the empty string('') matches the base
URL. Any other URL won't match this pattern, and Django will return an error page if the URL 
requested doesn't match any existing URL patterns.

The second argument in path()[line 53] specifies which function to call in views.py. When a 
requested URL matches the pattern we're defining, Django calls the index() function from 
views.py (We'll write this view function in the next section). 

The third argument provides the name 'index' for this URL pattern so we can refer to it in other
code sections. Whenever we want to provide a link to the home page, we'll use this name instead
of writing out a URL.
"""
