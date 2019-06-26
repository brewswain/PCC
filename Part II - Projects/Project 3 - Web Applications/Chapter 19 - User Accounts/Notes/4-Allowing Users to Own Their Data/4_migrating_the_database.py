"""
Now that we know the IDs, we can migrate the database. When we do this, Python will ask us to
connect the Topic model to a particular owner temporarily or to add a default to our models.py
file to tell it what to do.
Choose option 1:
"""

$ python manage.py makemigrations learning_logs

You are trying to add a non-nullable field 'owner' to topic without a default; we can't do that
(the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now(will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>> > 1
Migrations for 'learning_logs':
  learning_logs\migrations\0003_topic_owner.py
    - Add field owner to topic

"""
We start by issuing the makemigrations command(line 8). In the output at line 10, Django
indicates that we're trying to add a required (non-nullable) field to an existing model(topic)
with no default value specified. Django gives us two options at line 12: We can provide a
default right now, or we can quit and add a default value in models.py. At line 15 we've chosen
the first option. Django then asks us to enter the default value(line 16).

To associate all existing topics with the original admin user, admin, I entered the user ID of
1 at line 19. You can use the ID of any user you've created; it doesn't have to be a superuser.
Django then migrates the database using this value and generates the migration file
003_topic_owner.py, which adds the field owner to the Topic model.

Now we can execute the migration. Enter the following in an active virtual environment:
"""

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0003_topic_owner... OK
(ll_env)

"""
Django applies the enw migration, and the result is OK(line 43).

We can verify the migration worked as expected in the shell session, like this:
"""

>> > for topic in Topic.objects.all():
... print(topic, topic.owner)
...
Chess admin
Rock Climbing admin
dfdfds admin
test admin
test4 admin
Test Adding Entries to This Topic admin

"""
We import Topic from learning_logs.models(line 52), and then loop through all existing topics,
printing each topic and the user it belongs to(line 52). You can see that each topic now belongs
to the user admin.

NB. You can simply reset the database instead of migrating, but that will lose all existing
data. It's good practice to learn how to migrate a database while maintaining the integrity of
users' data. If you do want to start with a fresh database, issue the command:
"python manage.py flush"
to rebuild the database structure. You'll have to create a new superuser, and all of your data
will be gone.
"""
