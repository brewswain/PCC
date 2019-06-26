"""
Users should be able to enter data exclusive to them, so we'll create a system to figure out 
which data belongs to which user. Then we'll restrict access to certain pages so users can work
with only their data.

We'll modify the Topic model so every topic belongs to a specific user. This will also take care
of entries, because every entry belongs to a specific topic. We'll start by restricting access
to certain pages.

Django makes it easy to restrict access to certain pages to logged in users through the
'@login_required' decorator. A decorator is a directive placed just before a function definition
that Python applies to the function before it runs, to alter how the function code behaves. 
Let's look at an example.
"""

# # Restricting Access to the Topics Page

"""
Each topic will be owned by a user, so only registered users can request the topics page. Add
the following code to learning_logs/views/py:
"""

# learning_logs/views.py


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
--snip--


@login_required
def topics(request):


--snip--


"""
We first import the login_required() function. We apply login_required() as a decorator to the
topics() view function by prepending login_required with the @ symbol. As a result, Python knows
to run the code in login_required() before the code in topics().

The code in login_required() checks whether a user is logged in, and Django runs the code in
topics() only if they are. If the user isn't logged in, they're redirected to the login page.

To make this redirect work, we need to modify settings.py so Django knows where to find the 
login page. Add the following at the very end of settings.py:
"""

# settings.py

--snip--

# My Settings
LOGIN_URL = 'users:login'

"""
Now when an unauthenticated user requests a page protected by the @login_required decorator, 
Django will send the user to the URL defined by LOGIN_URL in settings.py.

You can test this setting by logging out of any user accounts and going to the home page. Click
the Topics link, which should redirect you to the login page. Then log in to any of your 
accounts, and from the home page click the Topics link again. You should be able to access the
topics page.
"""
