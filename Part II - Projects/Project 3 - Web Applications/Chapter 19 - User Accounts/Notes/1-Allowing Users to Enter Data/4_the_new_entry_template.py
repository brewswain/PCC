"""
As you can see in the following code, the template for new_entry is similar to the template for
new_topic:
"""

# new_entry.html

{ % extends 'learning_logs/base.html' % } { % block content % }
<p >
<a href = " {% url 'learning_logs:topic' topic.id %} " > {{topic}} < /a >
</p >

<p > Add a new entry: < /p >
<form action = " {% url 'learning_logs:new_entry' topic.id %}" method = "POST" >
    { % csrf_token % }
    {{form.as_p}}
    <button name = "submit" > Add Entry < /button >
</form >

{ % endblock content % }

"""
We show the topic at the top of the page(line 10), so the user can see which topic they're
adding an entry to. The topic also acts as a link back to the main page for that topic.

The form's action argument includes the topic_id value in the URL, so the view function can
associate the new entry with the correct topic(line 14). Other than that, this template looks
just like new_topic.html.
"""

# # Linking to the new_entry Page

"""
Next, we need to include a link to the new_entry page from each topic page in the topic 
template:
"""

# topic.html

{% extends 'learning_logs/base.html' % } { % block content % }

<p > Topic: {{topic}} < /p >
<p > Entries < /p >

<p > <a href = "{% url 'learning_logs:new_entry' topic.id %}" > Add new entry < /a > </p >
<ul >
--snip--

"""
We place the link to add entries just before showing the entries, because adding a new entry
will be the most common action on this page(line 45). Now users can add new topics and as many
entries as they want for each topic. Try out the new_entry page by adding a few entries to some
of the topics you've created.
"""
