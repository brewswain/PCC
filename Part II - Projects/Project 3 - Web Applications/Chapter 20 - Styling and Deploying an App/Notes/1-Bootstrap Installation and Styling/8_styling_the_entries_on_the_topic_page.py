"""
The topic page has more content than most pages, so it needs a bit more work. We'll use
Bootstrap's card component to make each entry stand out. A card is a div with a set of
flexible, predefined styles that's perfect for displaying a topic's entries:
"""

# topic.html
{% extends 'learning_logs/base.html' % } 


{% block page_header % }
<h3 > {{topic}} < /h3 >
{% endblock page_header % }

{% block content % }
<p >
    <a href = "{% url 'learning_logs:new_entry' topic.id %}" > Add new entry < /a >
</p >


{% for entry in entries % }
<div class = "card mb-3" >
    <h4 class = "card-header" >
        {{entry.date_added | date: 'M d, Y H:i'}}
        <small >
            <a href = "{% url 'learning_logs:edit_entry' entry.id %}" > edit entry < /a >
        </small >
    </h4 >
    <div class = "card-body" >
        {{entry.text | linebreaks}}
    </div >
</div >
{% empty % }
<p > There are no entries for this topic yet. < /p >
{% endfor % }

{% endblock content % }

"""
We first place the topic in the page_header block(line 11). Then we delete the unordered list
structure previously used in this template. Instead of making each entry a list item, we 
create a div element with the selector card at line 22. This card has two nested elements: one
to hold the timestamp and the link to edit the entry, and another to hold the body of the 
entry.

The first element in the card is a header, which is an <h4> element with the selector 
card-header(line 23). This card header contains the date the entry was made and a link to edit
the entry. The <small> tag around the edit_entry link makes it appear a little smaller than 
the timestamp(line 25). 

The second element is a div with the selector card-body(line 29), which places the text of the
entry in a simple box on the card. Notice that the Django code for including the information
hasn't changed; only the elements that affect the page's appearance have changed.
