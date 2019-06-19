"""
Django stores most of the information for a project in a database, so next we need to create a
database that Django can work with. Enter the following command, while still in an active
environment:
"""

python manage.py migrate

"""
Operations to perform:
Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
--snip--
Applying sessions.0001_initial... OK
"""

ls
'db.sqlite3  learning_log/  ll_env/  manage.py*'

"""
Any time we modify a database, we say we're migrating the database. Issuing the migrate command
tells Django to make sure the database matches the current state of the project. The first time
we run this command in a new project using SQLite(more about SQLite in a moment), Django will
create a new database for us.

At line 10, Django reports that it will prepare the database to store information it needs to 
handle administrative and authentication tasks.

Running the ls command shows that Django created another file called db.sqlite3 (line 21).
SQLite is a database that runs off a single file; it's ideal for writing simple apps because 
you won't have to pay much attention to managing the database.

Note that in an an Active Virtual Environment, you have to use the command 'python' to run
manage.py commands, even if you use something different, like python3, to run other programs.
In a virtual environment, the command 'python' refers to the version of Python that created
the virtual environment.
"""
