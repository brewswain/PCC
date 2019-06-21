"""
We'll create a template called base.html in the same directory as index.html. This file will
contain elements common to all pages; every other template will inherit from base.html. The
only element we want to repeat on each page right now is the title at the top. Because we'll
this template on every page, let's make the title a link to the home page:
"""
# base.html

# <p>
#     <a href = "{% url'learning_logs:index' %}"> Learning Log </a>
# </p>

# {% block content % }{ % endblock content % }


"""
The first part of this file creates a paragraph containing the name of the project, which also
acts as a home page link. To generate a link, we use a template tag, which is indicated by 
braces and percent signs {% %}. A template tag generates information to be displayed on a page.
Our template tag {% url'learning_logs:index' %} generates a URL matching the URL pattern 
defined in learning_logs/urls.py with the name index(line 11). In this example, learning_logs 
is the namespace and index is a uniquely named URL pattern in that namespace. The namespaces 
comes from the value we assigned to app_name in the learning_logs/urls.py file.

In a simple HTML page, a link is surrounded by the anchor tag <a>:

=======================================
|   <a href="link_url">Link Text</a>  |
=======================================

Having the template tag generate the URL for us makes it much easier to keep our links up to 
date. We only need to change the URL pattern in urls.py, and Django will automatically insert
the updated URL the next time the page is requested. Every page in our project will inherit 
from base.html, so from now on, every page will have a link back to the home page.

At line 14 we insert a pair of block tags. This block, named content, is a placeholder; the 
child template will define the kind of information that goes in the content block.

A child template doesn't have to define every block from its parent, so you can reserve space
in parent templates for as many blocks as you like; the child template uses only as many as it
required.

NB. In Python code, we almost always use four spaces when we indent. Template files tend to have
more levels of nesting than Python files, so it's common to use only two spaces for each 
indentation level. You just need to ensure that you're consistent.
"""
