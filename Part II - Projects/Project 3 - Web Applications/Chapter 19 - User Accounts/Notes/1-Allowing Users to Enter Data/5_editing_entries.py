"""
The URL for the page needs to pass the ID of the entry to be edited. 
Here's learning_logs/urls.py:
"""

# learning_logs/urls.py

urlpatterns = [
    --snip--
    # Path for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),
]

"""
The ID passed in the URL(for example, http://localhost:8000/edit_entry/1/) is stored in the
parameter entry_id. The URL pattern sends requests that match this format to the view function
edit_entry().
"""

# # The edit_entry() View Function

"""
When the edit_entry page receives a GET request, the edit_entry() function returns a form for 
editing the entry. When the page receives a POST request with revised entry text, it saves the
modified text into the database:
"""

# views.py

from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
--snip--

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry:' entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

"""
We first import the Entry model(line 32). At line 38 we get the entry object that the user 
wants to edit and the topic associated with this entry. In the if block, which runs for a GET
request, we make an instance of EntryForm with the argument instance=entry (line 43). This 
argument tells Django to create the form prefilled with information from the existing entry
object. The user will see their existing data and be able to edit that data.

When processing a POST request, we pass the instance=entry argument and the data=request.POST
argument(line 46). These arguments tell Django to create a form instance based on the 
information associated with the existing entry object, updated with any relevant data from 
request.POST. We then check whether the form is valid; if it is, we call save() with no
arguments because the entry is already associated with the correct topic(line 48). We then 
redirect to the topic page, where the user should see the updated version of the entry they
edited(line 49).

If we're showing an initial form for editing the entry or if the submitted form is invalid, we 
create the context dictionary and render the page using the edit_entry.html template.
"""