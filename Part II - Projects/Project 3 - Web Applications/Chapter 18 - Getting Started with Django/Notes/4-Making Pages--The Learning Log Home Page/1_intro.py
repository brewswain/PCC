"""
Making web pages with Django consists of three stages: defining URLs, writing views, and 
writing templates. You can do these in any order, but in this project we'll always start by 
defining the URL pattern. A URL pattern describes the way the URL is laid out. It also tells
Django what to look for when matching a browser request with a site URL so it knows which page
to return.

Each URL then maps to a particular view--The view function retrieves and then processes the 
data needed for that page. The view function often renders the page using a template, which 
contains the overall structure of the page. To see how this works, let's make the home page
for Learning Log. We'll define the URL for the home page, write its view function, and create
a simple template.

Because all we're doing is making sure Learning Log works as it's supposed to, we'll make a 
simple page for now. A functioning web app is fun to style when it's complete; an app that 
looks good but doesn't work well is pointless. For now, the home page will display only a title
and a brief description.
"""
