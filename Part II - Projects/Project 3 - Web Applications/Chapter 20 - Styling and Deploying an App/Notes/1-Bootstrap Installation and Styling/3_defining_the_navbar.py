"""
The code that defines the navigation bar at the top of the page is fairly long, because it
has to work well on narrow phone screens and wide desktop monitors. We'll work through the
navigation bar in sections.

Here's the first part of the navigation bar:
"""

# base.html

   <body >
       <nav class = "navbar navbar-expand-md navbar-light bg-light mb-4 border" >
           <a href = "{% url 'learning_logs:index' %}" class = "navbar-brand"
               >Learning Log < /a
            >
            <button
               class = "navbar-toggler"
                type = "button"
                data-toggle = "collapse"
                data-target = "#navbarCollapse"
                aria-controls = "navbarCollapse"
                aria-expanded = "false"
                aria-label = "Toggle navigation"
            >
               <span class = "navbar-toggler-icon" > </span >
            </button >
        </nav >
    </body >

"""
The first element is the opening body tag. The body of an HTML file contains the content users 
will see on a page. At line 12 is a <nav> element that indicates the page's navigation links 
section. Everything contained in this element is styled according to the Bootstrap style rules
defined by the selectors navbar, navbar-expand-md, and the rest that you see here. A selector
determines which elements on a page a certain style rule apples to. The navbar-light and 
bg-light selectors style the navigation bar with a light-themed background. The mb in mb-4 is 
short for margin-bottom; This selector ensures that a little space appears between the 
navigation bar and the rest of the page. The border selector provides a thin border around the 
light background to set it off a little from the rest of the page.

At line 13 we set the project's name to appear at the far left of the navigation bar and make it
a link to the home page; it will appear on every page in the project. The navbar-brand selector
styles this link so it stands out from the rest of the links and is a way of branding the site.

At line 16 the template defines a button that appears if the browser window is too narrow to 
display the whole navigation bar horizontally. When the user clicks the button, the navigation
elements will appear in a drop-down list. The collapse reference causes the nav-bar to collapse
when the user shrinks the browser window or when the site is displayed on mobile devices with 
small screens.

Here's the next section of code that defines the nav-bar:
"""

# base.html
--snip--
</button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a href="{% url 'learning_logs:topics' %}" class="nav-link"
              >Topics</a
            >
          </li>
        </ul>

"""
At line 57 we open a new section of the nav-bar. The term div is short for division; You build
a web page by dividing it into sections and defining style and behaviour rules that apply to
that section. Any styling or behaviour rules that are defined in an opening div tag affect 
everything you see until the next closing div tag, which is written as </div>. This is the 
beginning of the part of the nav-bar that will be collapsed on narrow screens and windows.

At line 58 we define a new set of links. Bootstrap defines navigation elements as items in an
unordered list with style rules that make it look nothing like a list. Every link or element
you need on the bar can be included as an item in one of these lists. Here, the only item in 
the list is our link to the Topics page(line 59).

Here's the next part of the navigation bar:
"""

# base.html

--snip--
</ul>
    <ul class="navbar-nav ml-auto">
        {% if user.is_authenticated %}
        <li class="nav-item">
        <span class="navbar-text">Hello, {{ user.username }}.</span>
        </li>
        <li class="nav-item">
        <a href="{% url 'users:logout' %}" class="nav-link">Log out</a>
        </li>
        {% else %}
        <li class="nav-item">
        <a href="{% url 'users:register' %}" class="nav-link">Register</a>
        </li>
        <li class="nav-item">
        <a href="{% url 'users:login' %}" class="nav-link">Log in</a>
        </li>
        {% endif %}
    </ul>
    </div>
</nav>

"""
At line 85 we begin a new set of links by using another opening <ul> tag. You can have as many
groups of links as you need on a page. This will be the group of links related to login and
registration that appears on the right side of the navigation bar. The selector ml-auto is
short for margin-left-automatic: This selector examins the other elements in the nav-bar and
works out a left margin that pushis this group of links to the right side of the screen.

The if block at line 86 is the same conditional block we used earlier to display appropriate
messages to users depending on whether or not they're logged in. The block is a little longer
now because some styling rules are inside the conditional tags. 

At line 88 is a <span> element. The span element styles pieces of text, or elements of a page,
that are part of a longer line. Whereas div elements create their own division in a page, 
span elements are continuous within a larger section. This an be confusing at first, because
many pages have deeply nested div elements. Here, we're using the span element to style 
informational text on the navigation bar, such as the logged-in user's name. We want this
info to appear different from a link, so users aren't tempted to click these elements.

At line 102 we close the div element that contains the parts of the nav-bar that will collapse
on narrow screens, and at the end of this section we close the nav-bar overall. If you wanted
to add more links to the nav-bar, you'd add another <li> item to any of the <ul> groups that
we've defined in the nav-bar by using identical styling directives as what you've seen here.

There's still a bit more we need to add to base.html. We need to define two blocks that the
individual pages can use to place the content specific to those pages.
"""
