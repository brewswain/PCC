"""
Without leaving the active virtual environment(remember to look for ll_env in parentheses in
the terminal prompt), enter the following commands to create a new project:
"""

django-admin startproject learning_log .

ls
'learning_log/  ll_env/  manage.py'

ls learning_log
'__init__.py  settings.py  urls.py  wsgi.py'
'

"""
The command at line 6 tells Django to set up a new project called learning_log. The dot at the
end of the command creates the new project with a directory structure that will make it easy 
to deploy the app to a server when we're finished developing it.

Don't forget the dot, or you might run into some configuration issues when you deploy the app.
If you forget the dot, delete the files and folders that were created (except ll_env), and
run the command again.

Running the ls command shows that Django has created a new directory called learning_log. It 
also created a manage.py file, which is a short program that takes in commands and feeds them 
to the relevant part of Django to run them. We'll use these commands to manage tasks, such as
working with databases and running server.

The learning_log directory contains four files(line 12); the most important are :
settings.py, urls.py, and wsgi.py. 

The settings.py file controls how Django interacts with your system and
manages your project. We'll modify a few of these settings and add some settings of our own
as the project evolves. 

The urls.py file tells Django which pages to build in response to browser requests.

The wsgi.py file helps Django serve the files it creates. The filename is an acronym for web
server gateway interface.
"""
