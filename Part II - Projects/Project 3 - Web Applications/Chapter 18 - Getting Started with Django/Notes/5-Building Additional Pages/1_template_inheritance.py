"""
Now that we've established a routine for building a page, we can start to build out the Learning
Log project. We'll build two pages that display data: A page that lists all topics and a page 
that shows all the entries for a particular topic. For each page, we'll specify a URL pattern, 
write a view function, and write a template. But before we do this, we'll create a base 
template that all templates in the project can inherit from.
"""

# Template Inheritance

"""
When building a website, some elements will always need to be repeated on each page. Rather 
than writing these elements directly into each page, you can write a base template 
containing the repeated elements and then have each page inherit from the base. This approach
lets you focus on developing the unique aspects of each page and makes it much easier to change
the overall look and feel of the project.
"""
