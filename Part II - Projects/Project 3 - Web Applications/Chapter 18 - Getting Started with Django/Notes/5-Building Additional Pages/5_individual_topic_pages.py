"""
Next, we need to create a page that can focus ona  single topic, showing the topic name and all
the entries for that topic. We'll again define a new URL pattern, write a view, and create a
template. We'll also modify the topics page so each item in the bulleted list links to its
corresponding topic page.
"""

# # The Topic URL Pattern

"""
The URL pattern for the topic page is a little different than the prior URL patterns because
it will use the topic's id attribute to indicate which topic was requested. For example, if the
user wants to see the detail page for the Chess topic, where the id is 1, the URL will be
http://localhost:8000/topics/1/.

Here's a pattern to match this URL, which you should place in learning_logs/urls.py:
"""

# learning_logs/urls.py

--snip--
urlpatterns = [
    --snip--
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

"""
Let's examine the string 'topics/<int:topic_id>/' in this URL pattern. The first part of the
string tells Django to look for URLs that have the word topics after the base URL. The second
part of the string, /<int:topic_id>/, matches an integer between two forward slashes and stores
the integer value in an argument called topic_id.

When Django finds a URL that matches this pattern, it calls the view function topic() with the
value stored in topic_id as an argument. We'll use the value of topic_id to get the correct
topic inside the function.
"""
