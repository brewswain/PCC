"""
Now we need to rewrite index.html to inherit from base.html. Add the following code to
index.html:
"""

# index.html

# {% extends "learning_logs/base.html" %}

# {% block content %}
# <p>
# Learning Log helps you keep track of your learning, for any topic you're
# learning about.
# </p>
# {% endblock content %}

"""
If you compare this to the original index.html, you can see that we've replaced the Learning
Log title with the code for inheriting from a parent template(line 8). A child template must 
have an {% extends %} tag on the first line to tell Django which parent template to inherit 
from. The file base.html is part of learning_logs, so we include learning_logs in the path to 
the parent template. This line pulls in everything contained in the base.html template and
allows index.html to define what goes in the space reserved by the content block.

We define the content block at line 10 by inserting a {% block %} tag with the name content.
Everything that we aren't inheriting from the parent template goes inside the content block.
Here, that's the paragraph describing the Learning Log project. At line 15 we indicate that
we're finished defining the content by using an {% endblock content %} tag. The {% endblock %}
tag doesn't require a name, but if a template grows to contain multiple blocks, it can be 
helpful to know exactly which block is ending.

You can start to see the benefit of template inheritance: in a child template, we only need to
include content that's unique to that page. This not only simplifies each template, but also
makes it much easier to modify the site. To modify an element common to many pages, you only 
need to modify the parent template. Your changes are then carried over to every page that 
inherits from that template. In a project that includes tens or hundreds of pages, this 
structure can make it much easier and faster to improve your site.

NB. In a large project, it's common to have one parent template called base.html for the entire
site and parent templates for each major section of the site. All the section templates inherit 
from base.html, and each page in the site inherits from a section template. This way you can 
easily modify the look and feel of the site as a whole, any section in the site, or any 
individual page. This configuration provides a very efficient way to work, and it encourages 
you to steadily update your site over time.
"""
