"""
The edit_entry pages have URLs in the form http://localhost:8000/edit_entry/entry_id/, where
the entry_id is a number. Let's protect this page so no one can use the URL to gain access to
someone else's entries:
"""

# views.py

--snip--
@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404


"""
We retrieve the entry and the topic associated with this entry. We then check whether the 
owner of the topic matches the currently logged in user; if they don't match, we raise an
Http404 exception.
"""
