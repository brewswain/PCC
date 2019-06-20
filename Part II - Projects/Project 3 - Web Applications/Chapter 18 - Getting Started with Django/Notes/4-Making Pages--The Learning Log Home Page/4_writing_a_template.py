"""
The template defines what the page should look like, and Django fills in the relevant data each
time the page is requested. A template allows you to access any data provided by the view.
Because our view for the home page provided no data, this template is fairly simple.

Inside the learning_logs folder, make a new folder called templates. Inside the templates 
folder, make another folder called learning_logs. This might seem a little redundant, but it 
sets up a structure that Django can interpret unambiguously, even in the context of a large
project containing many individual apps. Inside the inner learning_logs folder, make a new file
called index.html. The path to the file will be:

====================================================================
|   learning_log/learning_logs/templates/learning_logs/index.html  |
====================================================================

Enter the following code into that file:
"""
# # index.html

# <p>Learning Log</p>

# <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>

"""
This is a very simple file.  We have two paragraphs: the first acts as a title, and the second 
describes what users can do with Learning Log.

Now when you request the project's base URL, http://localhost:8000/, you should see the page we
just built instead of the default Django page. Django will take the requested URL, and that URL 
will match the pattern ''.
Then Django will call the function views.index(), which will render the page using the template
contained in index.html.

Although it might seem like a complicated process for creating one page, this separation 
between URLs, views, and templates works quite well. It allows you to think about each aspect
of a project separately. In larger projects, it allows individuals working on the project to
focus on the areas in which they're strongest. For example, a database specialist can focus on
the models, a programmer can focus on the view code, and a web designer can focus on the 
templates.

NB You might see the following error message:

================================================================
|   ModuleNotFOundError: No module named 'learning_logs.urls'  |
================================================================

If you do, restart the server via CTR-C and python manage.py runserver. Any time you run into
an error like this, try stopping and restarting the server.
"""
