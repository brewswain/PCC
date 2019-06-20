"""
A view function takes in information from a request, prepares the data needed to generate a 
page, and then sends the data back to the browser, often by using a template that defines
what the page will look like.

The file views.py in learning_logs was generated automatically when we ran the command:
"""

python manage.py startapp

"""
Here's what's in views.py right now:
"""

# views.py

# from django.shortcuts import render

# Create your views here.

"""
Currently, this file just imports the render() function, which renders the response based on
the data provided by views. Open the views file and add the following code for the home page:
"""

# Create your views here.


def index(request):
    """The homepage for Learning Log."""
    return render(request, 'learning_logs/index.html')


"""
When a URL request matches the pattern we just defined, Django looks for a function called 
index() in the views.py file. Django then passes the request object to this view function. In
this case, we don't need to process any data for the page, so the only code in the function is a 
call to render(). The render() function here passes two arguments--the original request object 
and a template it can use to build the page. Let's write this template.
"""
