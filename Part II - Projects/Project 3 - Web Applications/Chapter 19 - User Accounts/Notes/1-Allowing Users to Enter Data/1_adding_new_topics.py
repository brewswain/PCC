"""
Let's start by allowing users to add a new topic. Adding a form-based page works in much the 
same way as the pages we've already built: we define a URL, write a view function, and write a
template. The one major difference is the addition of a new module called forms.py, which will 
contain the forms.
"""

# # The Topic ModelForm

"""
Any page that lets a user enter and submit information on a web page is a form, even if it 
doesn't look like one. When users enter information, we need to validate that the information
is the right kind of data and is not malicious, such as code to interrupt our server. We then
need to process and save valid information to the appropriate place in the database. Django
automates much of this work.

The simplest way to build a form in Django is to use a ModelForm, which uses the information
from the models we defined in Chapter 18 to automatically build a form. Write your first form
in the file forms.py, which you should create in the same directory as models.py:
"""

# learning_logs/forms.py




from django import forms
from .models import Topic
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


"""
We first import the forms module and the model we'll work with, called Topic. At line 29 we 
define a class called TopicForm, which inherits from forms.Modelform.

The simplest version of a ModelForm consists of a nested Meta class telling Django which model
to base the form on and which fields to include in the form. At Line 31 we build a form from the
Topic model and include only the text field(line 32). The code at line 33 tells Django not to 
generate a label for the text field.
"""

# # The new_topic URL

"""
The URL for a new page should be short and descriptive. When the user wants to add a new topic, 
we'll send them to 
http://localhost:8000/new_topic/. 
Here's the URL pattern for the new_topic page, which you add to learning_logs/urls.py:
"""

# learning_logs/urls.py

--snip--
urlpatterns = [
    --snip--
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name="new_topic"),
]


"""
This URL pattern sends requests to the view function new_topic(), which we'll write next.
"""



# # The new_topic() View Function

"""
The new_topic() function needs to handle two different situations: initial requests for the
new_topic page(in which case it should show a blank form), and the processing of any data 
submitted in the form. After data from a submitted form is processed, it needs to redirect 
the user back to the topics page:
"""

# views.py


from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

--snip--

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

"""
We import the function redirect, which we'll use to redirect the user back to the topics page
after they submit their topic. The redirect() function takes in the name of a view and
redirects the user to that view. We also import the form we just wrote, TopicForm.
"""

## GET and POST Requests

"""
The two main types of requests you'll use when building web apps are GET requests and POST 
requests. You use GET requests for pages that only read data from the server. You usually use 
POST requests when the user needs to submit information thorugh a form. We'll be specifying the 
POST method for processing all of our forms. (A few other kinds of requests exist, but we won't
use them in this project.)

The new_topic() function(line 87) takes in the request object as a parameter. When the user 
initially requests this page, their browser will send a GET request. Once the user has filled
out and submitted the form, their browser will submit a POST request. Depending on the request,
we'll know whether the user is requesting a blank form (a GET request) or asking us to process
a completed form(a POST request).

The test at line 89 determines whether the request method is GET or POST. If the request method
isn't POST, the request is probably GET, so we need to return a blank form(if it's another kind
of request, it's still safe to return a blank form). We make an instance of TopicForm(line 91),
assign it to the variable form, and send the form to the template in the context dictionary 
(line 100). Because we included no arguments when instantiating TopicForm, Django creates a 
blank form that the user can fill out.

If the request method is POST, the else block runs and processes the data submitted in the form. 
We make an instance of TopicForm(line 94) and pass it the data entered by the user, stored in
request.POST. The form object that's returned contains the information submitted by the user.

We can't save the submitted information in the database until we've checked that it's valid
(line 95.) The is_valid() method checks that all required fields have been filled in(all fields
in a form are required by default) and that the data entered matches the field types expected-
for example, that the length of text is less than 200 characters, as we specified in models.py
in Chapter 18. This automatic validation saves us a lot of work. If everything is valid, we can
call save() at line 96, which writes the data from the form to the database.

Once we've saved the data, we can leave this page. We use redirect() to redirect the user's 
browser to the topics page, where the user should see the topic they just entered in the list
of topics. 

The context variable is defined at the end of the view function, and the page is rendered using
the template new_topic.html, which we'll create next. This code is placed outside of any if 
block; it will run if a blank form was created, and it will run if a submitted form is 
determined to be invalid. An invalid form will include some default error messages to help the
user submit acceptable data.
"""