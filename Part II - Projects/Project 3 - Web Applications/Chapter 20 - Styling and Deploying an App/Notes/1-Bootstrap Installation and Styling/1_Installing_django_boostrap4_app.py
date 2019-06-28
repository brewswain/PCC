"""
We'll use django-boostrap4 to integrate Boostrap into our project. This app downloads the 
required Bootstrap files, places them in an appropriate location in your project, and makes
styling directives available in your project's templates.

To install django-bootstrap4, issue the following command in an active virtual environment:
"""
$ pip install django-boostrap4
--snip--
Successfully installed django-bootstrap4-0.0.8

"""
Next, we need to add the following code to include django-bootstrap4 in INSTALLED_APPS in 
settings.py:
"""

# settings.py
INSTALLED_APPS = [
    # My apps.
    'learning_logs',
    'users',

    # Third party apps.
    'bootstrap4',

    # Default Django apps.
    --snip--
]

"""
Start a new section called Third Part apps for apps created by other developers and add
'bootstrap4' to this section. Make sure you place this section after # My apps but before the
section containing Django's default apps.
"""
