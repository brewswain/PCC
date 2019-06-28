"""
Let's make sure the pages for viewing information are styled appropriately as well, starting
with the topics page:
"""

# topics.html

{% extends 'learning_logs/base.html' % } 


{% block page_header % }
<h1 > Topics < /h1 >
{% endblock page_header % }

{% block content % }
<ul >
    {% for topic in topics % }
    <li > <h3 >
    <a href = " {% url 'learning_logs:topic' topic.id %} " > {{topic}} < /a >
    </li > </h3 >
    {% empty % }
    <li > <h3 > No topics have been added yet. < /h3 > </li >
    {% endfor % }
</ul >

<h3 > <a href = "{% url 'learning_logs:new_topic' %}" > Add a new topic < /a > </h3 >

{% endblock content % }

"""
We don't need the {& load bootstrap4 &} tag, because we're not using any custom bootstrap4
template tags in this file. We move the heading Topics into the page_header block and give it
a header styling instead of using the simple paragraph tag(line 11). We style each topic as an
<h3> element to make them a little larger on the page(line 18) and do the same for the link to
add a new topic(line 26).
"""
