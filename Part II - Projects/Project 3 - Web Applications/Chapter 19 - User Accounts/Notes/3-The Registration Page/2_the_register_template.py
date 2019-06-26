"""
Now create a template for the registration page, which will be similar to thelogin page. Be sure
to save it in the same directory as login.html:
"""

# users/templates/registration/register.html

{% extends 'learning_logs/base.html' % }

{% block content % }
<form method = "POST" action = "{% url 'users:register' %}" >
    {% csrf_token % }
    {{form.as_p}}

    <button name = "submit" > Register < /button >
    <input type = "hidden" name = "next" value = "{% url 'learning_logs:index' %}" >
</form >

{% endblock content % }

"""
We use the as_p method again so Django will display all the fields in the form appropriately, 
including any error messages if the form isn't filled out correctly.
"""
