"""
Django makes it easy to restrict access to pages, but you have to decide which pages to protect.
It's best to think about which pages need to be unrestricted first, and then restrict all the
other pages in the project. You can easily correct overrestricting access, and it's less
dangerous than leaving sensitive pages unrestricted.

In Learning Log, we'll keep the home page and the registration page unrestricted. We'll restrict 
access to every other page.

Here's learning_logs/views.py with @login_required decorators applied to every view except 
index():
"""

# learning_logs/views.py


@login_required
def topics(request):


--snip--


@login_required
def topic(request, topic_id):


--snip--


@login_required
def new_topic(request):


--snip--

# etc etc

"""
Try accessing each of these pages while logged out: You'll be redirected back to the login page.
You'll also be unable to click links to pages such as new_topic. But if you enter the URL
http://localhost:8000/new_topic/, you'll be redirected to the login page. You should restrict
access to any URL that's publicly accessible and relates to private user data.
"""
