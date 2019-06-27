"""
Currently, our page for adding new topics is broken, because it doesn't associate new topics
with any particular user. If you try adding a new topic, you'll see the error message
IntegrityError along with NOT NULL constraint failed: learning_logs_topic.owner_id.

Django's saying you can't create a new topic without specifying a value for the topic's owner
field.

There's a straightforward fix for this problem, because we have access to the current user
through the request object. Add the following code, which associates the new topic with the
current user:
"""

# views.py
--snip--
@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


"""
When we first call form.save(), we pass the commit=False argument because we need to modify 
the new topic before saving it to the database(line 26). We then set the new topic's owner 
attribute to the current user(line 27). Finally, we call save() on the topic instance just 
defined(line 28). Now the topic has all the required data and will save successfully.

You should be able to add as many new topics as you want for as many different users as you
want. Each user will have access only to their own data ,whether they're viewing data, 
entering new data, or modifying old data.
"""
