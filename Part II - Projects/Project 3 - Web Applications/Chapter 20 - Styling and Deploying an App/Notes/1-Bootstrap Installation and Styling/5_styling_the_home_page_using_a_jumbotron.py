"""
To update the home page, we'll use a Bootstrap element called a jumbotron, which is a large box
that stands out from the rest of the page and can contain anything you want. Typically, it's
used on home pages to hold a brief description of the overall project and a call to action that
invites the viewer to get involved. Here's the revised index.html file:
"""

# index.html

{ % extends "learning_logs/base.html"%}
{% block page_header % }
<div class = "jumbotron" >
  <h1 class = "display-3" > Track your learning. < /h1 >

   <p class = "lead" >
      Make your own Learning Log, and keep a list of the topics you're learning
       about. Whenever you learn something new about a topic, make an entry
        summarizing what you've learned.
    </p >

    <a
      href = "{% url 'users:register' %}"
       class = "btn btn-lg btn-primary"
        role = "button"
        >Register & raquo
        < / a
    >
</div >
{% endblock page_header % }

"""
At line 11 we tell Django that we're about to define what goes in the page_header block. A
jumbotron is just a div element with a set of styling directives applied to it(line 12). The
jumbotron selector applies this group of styling directives from the Bootstrap library to this 
element.

Inside the jumbotron are three elements. The first is a short message, Track your learning, that
gives first-time visitors a sense of what Learning Log does. The h1 class is a first-level 
header, and the display-3 selector adds a thinner and taller look to this particular header(line
13). At line 15 we include a longer message that provides more information about what the user
can do with their learning log.

Rather than just useing a text link, we create a button at line 21 that invites users to 
register their Learning Log account. This is the same link as in the header, but the button
stands out on the page and shows the viewer what they need to do to start using the project.
The selectors you see here style this as a large button that represents a call to action. The
code &raquo; is an HTML entity that looks like two right angle brackets combined(>>).

At line 28 we close the page_header block. We aren't adding any more content to this page, so
we don't need to define the content block on this page.
"""
