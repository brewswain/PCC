"""
To work with Django, we'll first set up a virtual environment. A virtual environment is a place
where you can install packages and isolate them from all other Python packages. Separating one's
project libraries from other projects is beneficial and will be necessary when we deploy
Learning Log to a server.

Create a new directory for your project called learning_log, switch to that directory in a
terminal, and enter the following code to create a virtual environment:
"""

python - m venv ll_env

"""
Here's we're running the venv virtual environment module and using it to create a virtual
environment named ll_env. If you use a command such as python3 when running programs or
installing packages, make sure to use that command here.
"""

# Activating the Virtual Environment

"""
Now we need to activate the virtual environment using the following command:
(This assumes you're using the bash terminal on windows.)
"""

source ll_env/Scripts/activate

"""
This command runs the script activate in ll_env\Scripts. When the environment is active, you'll
see the name of the environment in parentheses: "(ll-env)"; then you can install packages to the 
environment and use packages that have already been installed. Packages you install in ll_env 
will be available only while the environment is active.

To stop using a virtual environment, enter deactivate.

The environment also becomes inactive when you close the terminal it's running in.
"""
