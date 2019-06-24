"""
Now we'll make a new template called new_topic.html to display the form we just created:
"""

# new_topic.html

{ % extends 'learning_logs/base.html' % } { % block content % }
<p > Add a new topic: < /p >

<form action = "{% url 'learning_logs:new_topic' %}" method = "POST" >
    { % csrf_token % }
    {{form.as_p}}
    <button name = "submit" > Add topic < /button >
</form >

{ % endblock content % }

"""
This template extends base.html, so it has the same base structure as the rest of the pages is
Learning Log. At line 10 we define an HTML form. The action argument tells the browser where to
send the data submitted in the form; in this case, we send it back to the view function 
new_topic(). The method argument tells the browser to submit the data as a POST request.

Django uses the template tag {% csrf_token %}(line 11) to prevent attackers from using the form
to gain unauthorized access to the server(this kind of attack is called a cross-site request
forgery). At line 12 we display the form; here you can see how simple Django can make certain
tasks, such as displaying a form. We only need to include the template variable {{form.as_p}}
for Django to create all the fields necessary to display the form automatically. The 'as_p'
modifier tells Django to render all the form elements in paragraph format, as a simple way to
display the form nearly.

Django doesn't create a submit button for forms, so we define one at line 13. 
"""

# # Linking to the new_topic Page

"""
Next, we include a link to the new_topic page on the topics page:
"""

# topics.html
--snip--

</ul >

<a href = "{% url 'learning_logs:new_topic' %}" > Add a new topic < /a >

{% endblock content % }

"""
Place the link after the list of existing topics. Use the form to add a few new topics of your
own.
"""
