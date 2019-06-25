"""
Let's add the login link to base.html so it appears on every page. We don't want the link to 
display when the user is already logged in, so we nest it inside an {% if %} tag:
"""

# base.html

<p >
<a href = "{% url 'learning_logs:index' %}" > Learning Log < /a > -
<a href = "{% url 'learning_logs:topics' %}" > Topics < /a > -

    { % if user.is_authenticated % } 
    Hello, {{user.username}}.
    { % else % }
    <a href = "{% url 'users:login' %}" > Log in < /a >
    { % endif % }
</p >

{ % block content % }{ % endblock content % }

"""
In Django's authentication system, every template has a user variable, which always has an
is_authenticated attribute set: the attribute is True if the user is logged in and False if 
they aren't. This attribute allows you to display one message to authenticated users and another
to unauthenticated users.

Here we display a greeting to users currently logged in(line 12). Authenticated users have an
additional username attribute set, which we use to personalize the greeting and remind the user
that they're logged in(line 13). At line 15 we display a link to the login page for users who 
haven't been authenticated.
"""
