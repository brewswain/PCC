"""
Because we've added a new model, we need to migrate the database again. This process will
become quite familiar: you modify models.py, run the command :

"python manage.py makemigrations app_name" 

and then run the command :

"python manage.py migrate".

Migrate the database and check the output by entering the following commands:
"""

python manage.py makemigrations learning_logs
# Migrations for 'learning_logs':
#   learning_logs\migrations\0002_entry.py
#     - Create model Entry

python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
# Running migrations:
#   Applying learning_logs.0002_entry... OK

"""
A new migration called 0002_entry.py is generated, which tells Django how to modify the 
database to store information related to the model Entry(line 15). When we issue the migrate
command, we see that Django applied this migration, and everything was ok(line 23).
"""
