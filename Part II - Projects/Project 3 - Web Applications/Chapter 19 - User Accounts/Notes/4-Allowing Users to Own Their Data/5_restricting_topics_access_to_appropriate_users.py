"""
Currently, if you're logged in, you'll be able to see all the topics, no matter which user 
you're logged in as. We'll change that by showing users only the topics that belong to them.

Make the following changes to the topics() function in views.py:
"""

# views.py

--snip--
@login_required
def topics(request):
    """Shows all Topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


"""
When a user is logged in, the request object has a request.user attribute set that stores info
about the user. The query Topic.objects.filter(owner=request.user) tells Django to retrieve only
the Topic objects from the database whose owner attribute matches the current user. Because 
we're not changing how the topics are displayed, we don't need to change the template for the
topics page at all.

To see if this works, log in as the user you connected all existing topics to, and go to the 
topics page. You should see all the topics. Now log out, and log back in as a different user. 
The topics page should list no topics.
"""
