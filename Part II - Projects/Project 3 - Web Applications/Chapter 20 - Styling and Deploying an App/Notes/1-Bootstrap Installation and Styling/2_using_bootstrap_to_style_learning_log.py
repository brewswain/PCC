"""
Bootstrap is a large collection of styling tools. It also has a number of templates you can
apply to your project to create an overall style. It's much easier to use these templates than
it is to use individual styling tools. To see the templates Bootstrap offers, go to
http://getbootstrap.com/, click 'Examples', and look for the Navbars section. We'll use the
Navbar static template, which provides a simple top navigation bar and a container for the
page's content.
"""

# # Modifying base.html

"""
We need to modify the base.html template to accommodate the Bootstrap template.

The first change we'll make to base.html defines the HTML headers in the file, so whenever a
Learning Log page is open, the browser title bar displays the site name. We'll also add some
requirements for using Bootstrap in our templates. Delete everything in base.html and replace
it with the following code:
"""

# base.html

{ % load bootstrap4 % }

<!DOCTYPE html >
<html lang = "en" >
   <head >
       <meta charset = "UTF-8" / >
        <meta name = "viewport" content = "width=device-width, initial-scale=1.0" / >
        <meta http-equiv = "X-UA-Compatible" content = "ie=edge" / >
        <title > Learning Log < /title >

        { % bootstrap_css % } 
        { % bootstrap_javascript jquery = 'full' % }
    </head >
    <body > </body >
</html >

"""
At line 23 we load the collection of template tags available in django-bootstrap4. Next, we
declare this file as an HTML document(line 25) written in English(line 26). An HTML file is
divided into two main parts, the head and the body -- the head of a the file begins at line 
27. The head of an HTML file doesn't contain any content: it just tells the browser what it
needs to know to display the page correctly. At line 31 we include a title element for that
page, which will display in the browser's title bar whenever Learning Log is open.

At line 33 we use one of django-bootstrap4's custom template tags, which tells Django to 
include all the Bootstrap style files. The tag that follows enables all the interactive 
behaviour you might use on a page, such as collapsible navigation bars. At line 35 is the
closing head tag.
"""
