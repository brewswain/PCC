"""
Django includes some models in the admin site automatically such as User and Group, but the
models we create need to be added manually.

When we started the learning_logs app, Django created an admin.py file in the same directory as
models.py. Open the admin.py file:
"""

# admin.py


from django.contrib import admin

# Register your models here.

"""
To register Topic with the admin site, enter the following:
"""

# from django.contrib import admin
# from .models import Topic

# # Register your models here.
# admin.site.register(Topic)

"""
This code first imports the model we want to register, Topic (line 21). The dot in front of 
models tells Django to look for models.py in the same directory as admin.py. 
The code admin.site.register() tells Django to manage our model through the admin site(line 24).

Now use the superuser account to access the admin site. Go to http://localhost:8000/admin/, and 
enter the username and password for the superuser you just created. This page allows you to add
new users and groups, and change existing ones. You can also work with data related to the 
Topic model we just defined.
"""
