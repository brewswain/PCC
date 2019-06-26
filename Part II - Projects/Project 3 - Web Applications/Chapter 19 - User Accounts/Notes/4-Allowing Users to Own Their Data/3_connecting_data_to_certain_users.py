"""
Next, we need to connect the data to the user who submitted it. We need to connect only the
data highest in the hierarchy to a user, and the lower-level data will follow. For example, in
Learning Log, topics are the highest level of data in the app, and all entries are connected to
a topic. As long as each topic belongs to a specific user, we can trace the ownership of each 
entry in the database.

We'll modify the Topic model by adding a foreign key relationship to a user. We'll then have to
migrate the database. Finally, we'll modify some of the views so they only show the data 
associated with the currently logged in user.
"""

# # Modifying the Topic Model

"""
The modification to models.py is just two lines:
"""

# learning_logs/models.py

from django.db import models
from django contrib.auth.models import User #

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #

"""
We import the User model from django contrib.auth. Then we add an owner field to Topic, which
establishes a foreign key relationship to the User model. If a user is deleted, all the topics
associated with that user will be deleted as well.
"""

# # Identifying Existing Users

"""
When we migrate the database, Django will modify the database so it can store a connection 
between each topic and a user. To make the migration, Django needs to know which user to 
associate with each existing topic. The simplest approach is to start by giving all existing
topics to one user--for example, the superuser. But first we need to know that user's ID.

Let's look at the IDs of all users created so far. Start a Django shell session and issue the
following commands:
"""

python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: admin>, <User: Kirby_says_Poyo>]>

>>> for user in User.objects.all():
...     print(user.username, user.id)
...
admin 1
Kirby_says_Poyo 2

"""
At line 52 we import the User model into the shell session. We then look at all the users that 
have been created so far (line 53). The output shows two users: admin, and Kirby_says_Poyo.

At line 56 we loop through the list of users and print each user's username and ID. When Django
asks which user to associate the existing topics with, we'll use one of these ID values.
"""