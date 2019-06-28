"""
We've refined the overall appearance of the login page but not the login form yet. Let's make
the form look consistent with the rest of the page by modifying the login.html file:
"""

# users/login.html

{% extends 'learning_logs/base.html' % } 
{% load bootstrap4 % }


{% block page_header % }
<h2 > Log in to your account. < /h2 >
{% endblock page_header % }

{% block content % }
<form method = "POST" action = "{% url 'users:login' %}" class = "form" >
{% csrf_token % }
{% bootstrap_form form % }
{% buttons % }
<button name = "submit" class = "btn btn-primary" > Log in < /button >
{% endbuttons % }

<input type = "hidden" name = "next" value = "{%  url 'learning_logs:index' %}" / >
</form >

{% endblock content % }

"""
At line 9 we load the bootstrap4 template tags into this template. At line 12 we define the 
page_header block, which tells the user what the page is for. Notice we've removed the 
{% if form.errors %} block from the template; django-boostrap4 manages form errors automatically.

At line 17 we add a class="form" attribute, and then we use the template tag 
{% bootstrap_form %} when we display the form(line 19); this replaces the {{form.as_p}} tag we
were previously using. The {% bootstrap_form %} template tag inserts Bootstrap style rules into 
the form's individual elements as the form is rendered. At line 20 we open a bootstrap4 template
tag {% buttons %}, which adds Bootstrap styling to buttons.
"""
