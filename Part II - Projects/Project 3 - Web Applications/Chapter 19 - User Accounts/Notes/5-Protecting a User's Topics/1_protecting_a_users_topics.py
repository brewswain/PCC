"""
We haven't restricted access to the topic pages yet, so any registered user could try a bunch 
of URLs, like http://localhost:8000/topics/1/, and retrieve topic pages that happen to match.

Try it yourself. While logged in as the user that owns all topics, copy the URL or note the ID 
in the URL of a topic, and then log out and log back in as a different user. Enter that topic's 
URL. You should be able to read the entries, even though you're logged in as a different user.

We'll fix this now by performing a check before retrieving the requested entries in the topic()
view function:
"""

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

--snip--
@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


--snip--

"""
A 404 response is a standard error response that's returned when a requested resource doesn't
exist on a server. Here we import the Http404 exception(line 17), which we'll raise if the user
requests a topic they shouldn't see. After receiving a topic request, we make sure the topic's 
user matches the currently logged in user before rendering the page. If the current user doesn't
own the requested topic, we raise the Http404 exception(line 25), and Django returns a 404
error page.

Now if you try to view another user's topic entries, you'll see a Page Not Found message from 
Django. In Chapter 20, we'll configure the project so that users will see a proper error page.
"""
