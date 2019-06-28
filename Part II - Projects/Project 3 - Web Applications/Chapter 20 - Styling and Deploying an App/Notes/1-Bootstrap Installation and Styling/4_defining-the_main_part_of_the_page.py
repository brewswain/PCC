"""
The rest of base.html contains the main part of the page:
"""

# base.html

--snip--
</nav >
<main role = "main" class = "container" >
<div class = "pb-2 mb-2 border-bottom" >
    {% block page_header % } { % endblock page_header % }
    </div >

    <div >
    {% block content % } { % endblock content % }
    </div >
</main >
</body >
</html >

"""
At line 9 we open a <main> tag. The main element is used for the most significant part of the 
body of a page. Here we assign the bootstrap selector container, which is a simple way to 
group elements on a page. We'll place two div elements in this container.

The first div element(line 10) contains a page_header block. We'll use this block to title
most pages. To make this section stand out from the rest of the page, we place some padding
below the header. Padding refers to space between an element's content and its border. The
selector pb-2 is a bootstrap directive that provides a moderate amount of padding at the 
bottom of the styled element. A margin is the space between an element's border and other
elements on the page. We want a border only on the bottom of the page, so we use the selector
border-bottom, which provides a thin border at the bottom of the page_header block.

At line 14 we define one more div element, which contains the block content. We don't apply 
any specific style to this block, so we can style the content of any page as we see fit for 
that page. We end the base.html file with closing tags for the main, body, and html elements.

When you load Learning Log's home page in a browser, you should see a professional looking
responsive nav-bar.
"""
