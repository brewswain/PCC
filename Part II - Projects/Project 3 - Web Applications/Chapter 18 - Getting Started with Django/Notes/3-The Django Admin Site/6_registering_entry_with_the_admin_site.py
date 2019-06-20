"""
We also need to register the Entry model. Here's what admin.py should look like now:
"""

# admin.py

from django.contrib import admin
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)

"""
Go back to http://localhost/admin/, and you should see Entries listed under Learning_logs.
Click the Add link for Entries, or click Entries, and then choose Add entry. you should see
a drop-down list to select the topic you're creating an entry for and a text box for adding an 
entry, Select Chess from the drop-down list, and add an entry. For example:

"The opening is the first part of the game, roughly the first ten moves or so. In the opening,
it's a good idea to do three things--bring out your bishops and knights, try to control the
center of the board, and castle your king.

Of course, these are just guidelines. It wil lbe important to learn when to follow these 
guidelines and when to disregard these suggestions."

When you click Save, you'll be brought back to the main admin page for entries. Here, you'll
see the benefit of using text[:50] as the string representation for each entry; it's much 
easier to work with multiple entries in the admin interface if you see only the first part of
an entry rather than the entire text of each entry.

Make a second entry for Chess and one entry for Rock Climbing so we have some initial data. 
Here's a second entry for Chess:

"In the opening phase of the game, it's important to bring out your bishops and knights. 
These pieces are powerful and maneuverable enough to play a significant role in the 
beginning moves of a game."

And here's a first entry for Rock Climbing:

"One of the most important concepts in climbing is to keep your weight on your feet as much
as possible. There's a myth that climbers can hang all day on their arms. In reality, good
climbers have practiced specific ways of keeping their weight over their feet whenever 
possible."

These three entries will give us something to work with as we continue to develop Learning
Log.
"""
