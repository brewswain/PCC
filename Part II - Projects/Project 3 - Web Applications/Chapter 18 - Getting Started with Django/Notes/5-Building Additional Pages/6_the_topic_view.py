"""
The topic() function needs to get the topic and all associated entries from the database, as
shown here:
"""

# views.py

--snip--


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


"""
This is the first view function that requires a parameter other than the request object. The 
function accepts the value captured by the expression /<int:topic_id>/ and stores it in 
topic_id (line 11). At line 13 we use get() to retrieve the topic, just as we did in the Django 
shell. At line 14 we get the entries associated with this topic, and we order them according to
date_added. The minus sign in front of date_added sorts the results in reverse order, which 
will display the most recent entries first. We store the topic and entries in the context 
dictionary (line 15) and send context to the template topic.html(line 16).

NB. The code phrases at lines 13 and 14 are called queries, because they query the database for
specific information. When you're writing queries like these in your own projects, it's helpful 
to try them out in the Django shell first. You'll get much quicker feedback in the shell that 
you will by writing a view and template, and then checking the results in a browser.
"""

# # The Topic Template

"""
The template needs to display the name of the topic and the entries. We also need to inform the
user if no entries have been made yet for this topic.
"""

# topic.html

{ % extends 'learning_logs/base.html' % } { % block content % }

<p > Topic: {{topic}} < /p >
<p > EntriesL < /p >
<ul >
    { % for entry in entries % }
    <li >
    <p > {{entry.date_added | date: "M d, Y H:i"}} < /p >
    <p > {{entry.text | linebreaks}} < /p >
    </li >
    { % empty % }
    <li > There are no entries for this topic yet. < /li >
    { % endfor % }
</ul >

{ % endblock content % }

"""
We extend base.html as we do for all pages in the project. Next, we show the topic that's
currently being displayed(line 45), which is stored in the template variable {{topic}}. The
variable topic is available because it's included in the context dictionary. We then start a
bulleted list to show each of the entries(line 47) and loop through them as we did the topics
earlier.

Each bullet lists two pieces of information: the timestamp and the full text of each entry.
For the timestamp(line 50), we display the value of the attribute date_added. In Django 
templates, a vertical line ( | ) represents a template filter--a function that modifies the
value in a template variable. The filter date:'M d, Y H:i' displays timestamps in the format
January 1, 2018 23:00. The next line displays the full value of text rather than just the
first 50 characters from entry. The filter linebreaks(line 51) ensures that long text entries
includes line breaks ina  format understood by browsers rather than showing a block of 
uninterrupted text. At line 53 we use the {% empty %} template tag to print a message 
informing the user that no entries have been made.
"""

# # Links from the Topics Page

"""
Before we look at hte topic page in a browser, we need to modify the topics template so each
topic links to the appropriate page. Here's the change you need to make to topics.html:
"""

# topics.html

--snip--
    {% for topic in topics % }
    <li >
    <a href = " {% url 'learning_logs:topic' topic.id %} " > {{topic}} < /a >
    </li >
    {% empty % }
--snip--
