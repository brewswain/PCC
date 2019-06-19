"""
Let's think about our data for a moment. Each user will need to create a number of topics in
their learning log. Each entry they make will be tied to a topic, and these entries will be
displayed as text. We'll also need to store the timestamp of each entry, so we can show users
when they made each entry.

Open the file models.py, and look at its existing content:
"""

# models.py

from django.db import models

# Create your models here.

"""
A module called models is being imported for us, and we're being invited to create models of
our own. A model tells Django how to work with the data that will be stored in the app.
Code-wise, a model is just a class; it has attributes and moethods, just like very class
we've discussed. Here's the model for the topics users will store:
"""


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeFiled(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


"""
We've created a class called Topic, which inherits from Model--a parent class included in
Django that defines a model's basic functionality. We add two attributes to the Topic class:
'text' and 'date_added'.

The text attribute is a CharField--a piece of data that's made up of characters, or 
text(line 26.) You use CharField when you want to store a small amount of text, such as a name,
a title, or a city. When we define a CharField attribute, we have to tell Django how much space
it should reserve in the database. Here we give it a max_length of 200 characters, which should
be enough to hold most topic names.

The date_added attribute is a DateTimeField--a piece of data that will record a date and 
time(line 27). We pass the argument auto_now_add=True, which tells Django to automattically set
this attribute to the current date and time whenever the user creates a new topic.

NB. To see the different kinds of fields you can use in a model, see the Django Model Field
Reference at https://docs.djangoproject.com/en/2.2/ref/models/fields/ . You won't need all the
information right now, but it will be extremely useful when you're developing your own apps.

We tell Django which attribute to use by default when it displays information about a topic.
Django calls a __str__() method to display a simple representation of a model. Here we've 
written a __str__() method that returns the string stored in the text attribute(line 29).
"""
