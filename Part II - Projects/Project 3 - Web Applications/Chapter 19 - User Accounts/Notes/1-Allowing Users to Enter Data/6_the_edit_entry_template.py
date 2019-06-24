"""
Next, we create an edit_entry.html template, which is similar to new_entry.html:
"""

# edit_entry.html

{% extends 'learning_logs/base.html' % } { % block content % }
<p >
<a href = "{% url 'learning_logs:topic' topic.id %}" > {{topic}} < /a >
</p >

<p > Edit entry: < /p >

<form action = "{% url 'learning_logs:edit_entry' entry.id %}" method = "POST" >
    {% csrf_token % }
    {{form.as_p}}
    <button name = "submit" > Save changes < /button >
</form >

{% endblock content % }

"""
At line 14 the action argument sends the form back to the edit_entry() function for 
processing. We include the entry ID as an argument in the {% url %} tag, so the view function
can modify the correct entry object. We label the submit button as Save changes to remind the
user that they're saving edits, not creating a new entry(line 17).
"""

# # Linking to the edit_entry Page

"""
Now we need to include a link to the edit_entry page for each entry on the topic page:
"""

# topic.html

--snip--
<p > {{entry.date_added | date: 'M d, Y H:i'}} < /p >
<p > {{entry.text | linebreaks}} < /p >
<p >
<a href = "{% url 'learning_logs:edit_entry' entry.id %}" > Edit entry < /a >
</p >
--snip--

"""
We include the edit link after each entry's date and text has been displayed. We use the 
{% url %} template tag to determine the URL for the named URL pattern edit_entry, along with
the ID attribute of the current entry in the loop(entry.id). The link text Edit entry appears
after each entry on the page.

Learning Log now has most of the functionalitty it needs. Users can add topics and entries, and 
read through any set of entries they want. In the next section, we'll implement a user 
registration system so anyone can make an account with Learning Log and create their own set of 
topics and entries.
"""
