"""
Now that the user can add a new topic, they'll want to add new entries too. We'll again define
a URL, write a view function and a template, and link to the page. But first, we'll add
another class to forms.py.
"""

# # The Entry ModelForm

"""
We need to create a form associated with the Entry model but this time with a bit more
customization than TopicForm:
"""

# forms.py


from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
--snip--


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


"""
We update the import statement ot include Entry as well as Topic. We make a new class called 
EntryForm that inherits from forms.ModelForm. The EntryForm class has a nested Meta class 
listing the model it's based on and the field to include in the form. We again give the field 
'text' a blank label(line 31).

At line 32 we include the widgets attribute. A widget is an HTML form element, such as a 
single-line text box, multi-line text area, or drop-down list. By including the widgets 
attribute, you can override Django's default widget choices. By telling Django to use a 
forms.Textarea element, we're customizing the input widget for the field 'text so the text area 
ill be 80 columns wide instead of the default 40. This gives users enough room to write a 
meaningful entry.
"""


# # The new_entry URL

"""
New entries must be associated with a particular topic, so we need to include a topic_id 
argument in the URL for adding a new entry. Here's the URL, which you add to 
learning_logs/urls.py: 
"""

# learning_logs/urls.py:

--snip--
urlpatterns = [
    --snip--
    # Path for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),
]


"""
This URL pattern matches any URL with the form 
http://localhost:8000/new_entry/id/, where 'id' is a number matching the topic ID. The code
<int:topic_id> captures a numerical value and assigns it to the variable topic_id. When a URL
matching this pattern is requested, Django sends the request and the topic's ID to the 
new_entry() view function.
"""

# # The new_entry() View Function

"""
The view function for new_entry is much like the function for adding a new topic. Add the 
following code to your views.py file:
"""

# views.py

from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

--snip--
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

"""
We update the import statement to include the EntryForm we just made. The definition of 
new_entry() has a topic_id parameter to store the value it receives from the URL. We'll need 
the topic to render the page and process the form's data, so we use topic_id to get the correct
topic object at line 90.

At line 92 we check whether the request method is POST or GET. The if block executes if it's a 
GET request, and we create a blank instance of EntryForm(line 94).

If the request method is POST, we process the data by making an instance of EntryForm, populated
with the POST data from the request object(line 97). We then check whether the form is valid. 
If it is, we need to set the entry object's topic attribute before saving it to the database.
When we call save(), we include the argument commit=False(line 99) to tell Django to create a
new entry object and assign it to new_entry without saving it to the database yet. We set the
topic attribute of new_entry to the topic we pulled from the database at the beginning of the
function(line 100). Then we call save() with no arguments, saving the entry to the database with
the correct associated topic.

The redirect() call at line 102 requires two arguments--the name of the view we want to redirect
to and the argument that view function required. Here, we're redirecting to topic(), which needs
the argument topic_id. This view then renders the topic page that the user made an entry for, 
and they should see their new entry in the list of entries.

At the end of the function ,we create a context dictionary and render the page using the 
new_entry.html template. This code will execute for a blank form or for a submitted form that is
evaluated as invalid.
"""