"""
Now we need to provide a way for users to log out. We'll put a link in base.html that logs out
users; when they click this link, they'll go to a page confirming that they've been logged out.
"""

# # Adding a Logout Link to base.html

"""
We'll add the link for logging out to base.html to it's available on every page. We'll include
it in the {% if user.is_authenticated %} portion so only users who are already logged in can
see it:
"""

# base.html

--snip--
    { % if user.is_authenticated % } 
    Hello, {{user.username}}.
    <a href = "{% url 'users:logout' %}" > Log out < /a >
    { % else % }
--snip--

"""
The default named URL pattern for logging out is simply 'logout'.
"""

# # The Logout Confirmation Page

"""
Users will want to know that they've successfully logged out, so the default logout view renders
the page using the template logged_out.html, which we'll crate now. Here's a simple page
confirming that the user has been logged out. Save this file in templates/registration, the same
place where you saved login.html:
"""

# logged_out.html

{ % extends 'learning_logs/base.html' % }


{ % block content % }
<p > You have been logged out. Thank you for visiting!< /p >
{ % endblock content % }

"""
We don't need anything else on this page, because base.html provides links back to the home page
and the login page if the user wants to go back to either page.
"""
