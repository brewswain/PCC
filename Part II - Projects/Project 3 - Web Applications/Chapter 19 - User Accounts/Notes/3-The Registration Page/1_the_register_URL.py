"""
Next, we'll build a page so new users can't register. We'll use Django's default 
UserCreationForm but write our own view function and template.

The following code provides the URL pattern for the registration page, again in users/urls.py:
"""

# users/urls.py

"""Defines URL patterns for users."""


from django.urls import path, include
from . import views
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration Page.
    path('register/', views.register, name='register'),
]

"""
We import the views module from users, which we need because we're writing our own view for the
registration page. PThe pattern for the registration page matches the URL 
http://localhost:8000/users/register/ and sends requests to the register() function we're about 
to write.
"""

# # The register() View Function

"""
The register() view function needs to display a blank registration form when the registration 
page is first requested and then process completed registration forms when they're submitted.
When a registration is successful, the function also needs to log in the new user. Add the 
following code to users/views.py:
"""

# users/views.py


# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the use in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


"""
We import the render() and redirect() functions. Then we import the login() function to log the
user in if their registration information is correct. We also import the default 
UserCreationForm. In the register() function, we check whether or not we're responding to a
POST request. If we're not, we make an instance of UserCreationForm with no initial data
(line 57). 

If we're responding to a POST request, we make an instance of UserCreationForm based on the 
submitted data(line 60). We check that the data is valid(line 62)-- in this case, that the
username has the appropriate characters, the passwords match, and the user isn't trying to do 
anything malicious in their submission.

If the submitted data is valid, we call the form's save() method to save the username and the 
hash of the password to the database(line 63). The save() method returns the newly created user
object, which we assign to new_user. When the user's information is saved, we log them in by 
calling the login() function with the request and new_user objects(line 65), which creates a
valid session for the new user. Finally, we redirect the user to the home page(line 66), where a
personalized greeting in the header tells them their registration was successful.

At the end of the function we render the page, which will either be a blank form or a submitted 
form that is invalid.
"""
