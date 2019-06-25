"""
When the user requests the login page, Django will use a default view function, but we still
need to provide a template for the page. The default authentication views look for templates
inside a folder called registration, so we'll need to make that folder. Inside the 
learning_log/users/ directory, make a directory called templates; inside that, make another 
directory called registration. Here's the login.html templaye, which you should save in 
learning_log/users/templates/registration:
"""

# login.html

{% extends 'learning_logs/base.html' % }

{% block content % } 

{% if form.errors % }
<p > Your username and password didn't match. Please try again. < /p >
{% endif % }

<form method = "POST" action = "{% url 'users:login' %}" >
    {% csrf_token % }
    {{form.as_p}}

    <button name = "submit" > Log in < /button >
    <input type = "hidden" name = "next" value = "{%  url 'learning_logs:index' %}" / >
</form >

{% endblock content % }

"""
This template extends base.html to ensure that the login page will have the same look and feel
as the rest of the site. Note that a template in one app can inherit from a template in another
app.

If the form's errors attribute is set, we display an error message(line 16), reporting that the
username and password combination don't match anything stored in the database.

We want the login view to process the form, so we set the action argument as the URL of the 
login page(line 20). The login view sends a form to the template, and it's up to us to display
the form(line 22) and add a submit button(line 24). At line 25 we include a hidden form element,
'next';  the value argument tells DJango where to redirect the user after they've logged in 
successfully. In this case, we send the user back to the home page.
"""
