"""
Now that we have an efficient approach to building pages, we can focus on our next two pages:
The general topics page and the page to display entries for a single topic. the topics page will
show all topics that users have created, and it's the first page that will involve working
with data.
"""

# # The Topics URL Pattern

"""
First, we define the URL for the topics page. It's common to choose a simple URL fragment that
reflects the kind of information presented on the page. We'll use the word topics, so the URL
http://localhost:8000/topics/ will return this page. Here's how we modify
learning_logs/urls.py:
"""

# learning_logs/urls.py

"""Defines URLS patterns for learning_logs."""


from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name="topics"),
]

"""
We've simply added topics/ into ths string argument used for the home page URL(line 29). When
Django examines a requested URL, this pattern will match any URL that has the base URL followed
by topics. You can include or omit a forward slash at the end, but there can't be anything else
after the word topics, or the pattern won't match. Any request with a URL that matches this
pattern will then be passed to the function topipcs() in views.py.
"""

# # The Topics View

"""
The topics() function needs to retrieve some data from the database and send it to the template.
Here's what we need to add to views.py:
"""

# views.py

# from django.shortcuts import render
# from .models import Topic

# Create your views here.


def index(request):
    """The homepage for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Shows all Topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


"""
We first import the model associated with the data we need(line 50). The topics() function
needs one parameter: the request object Django received from the server(line 60). At line 62 we
query the database by asking for the Topic objects, sorted by the date_added attribute. We
store the resulting queryset in topics.

At line 63 we define a context that we'll send to the template. A context is a dictionary in
which the keys are names we'll use in the template to access the data, and the values are the
data we need to send to the template. In this case, there's one key-value pair, which contains
the set of topics we'll display on the page. When building a page that uses data, we pass the
context variable to render() as well as the request object and the path to the template (line
64).
"""

# # The Topics Template

"""
The template for the topics page receives the context dictionary, so the template can use the
data that topics() provides. Make a file called topics.html in the same directory as index.html.
Here's how we can display the topics in the template:
"""

# topics.html

# {% extends 'learning_log/base.html' %} {% block content %}

# <p>Topics</p>

# <ul>
#   {% for topic in topics %}
#   <li>{{ topic }}</li>
#   {% empty %}
#   <li>No topics have been added yet.</li>
#   {% endfor %}
# </ul>

# {% endblock content %}

"""
We use the {% extends %} tag to inherit from base.html, just as the index template does, and 
then open a content block. The body of this page contains a bulleted list of the topics that 
have been entered. We begin the bulleted list of topics at line 95. At line 96 we have another
template tag equivalent to a for loop, which loops through the list topics from the context
dictionary. The code used in templates differs from Python in some important ways. Python
uses indentation to indicate which lines of a for statement are part of a loop. In a template,
every for loop needs an explicit {% endfor %} tag indicating where the end of the loop occurs. 
So in a template, you'll see loops written like this:

==================================
|   {% for item in list %}       |
|   do something with each item  |
|   {% endfor %}                 |
==================================

Inside the loop, we want to turn each topic into an item in the bulleted list. To print a 
variable in a template, wrap the variable name in double braces. The braces won't appear on 
tje page; they just indicate to Django that we're using a template variable. So the code
{{topic}} at line 97 will be replaced by the value of topic on each pass through the loop. The
HTML tag <li></li> indicates a list item.

At line 98, we use the {% empty %} template tag, which tells Django what to do if there are no
items in the list. In this case, we print a message informing the user that no topics have been
added yet. The last two lines close out the for loop(line 100) and then close out the bullet 
list(line 101).

Now we need to modify the base template to include a link to the topics page. Add the following 
code to base.html:
"""

# base.html

# <p>
#   <a href="{% url'learning_logs:index' %}">Learning Log</a> -
#   <a href="{% url'learning_logs:topics' %}">topics</a>
# </p>

# {% block content %}{% endblock content %}

"""
We add a dash after the link to the home page(line 139), and then add a lin kto the topics page
using the {% url %} template tag again(line 140). This line tells Django to generate a link 
matching the URL pattern with the name 'topics' in learning_logs/urls.py.

Now when you refresh the home page in your browser, you'll see a topics link.
"""
