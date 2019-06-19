"""
Django makes it easy to work with your models through the admin site. Only the site's 
administrators use the admin site, not general users. In this section, we'll set up the admin 
site and use it to add some topics through the Topic model.

Django allows you to create a superuser, a user who has all privileges available on the site. A
user's privileges control the actions that user can take. The most restrictive privilege 
settings allow a user to only read public information on the site. Registered users typically
have the privilege of reading their own private data and some selected information available
only to members. To effectively administer a web application, the site owner usually needs 
access to all information stored on the site. A good administrator is careful with their user's
sensitive information, because users put a lot of trust into the apps they access.

To create a superuser in Django, enter the following command and respond to the prompts:
"""
python manage.py createsuperuser

# Username (leave blank to use 'brand'): admin
# Email address:
# Password:
# Password (again):
# Superuser created successfully.
# (ll_env)

"""
When you issue the command createsuperuser, Django prompts you to enter a username for the 
superuser(line 18). I chose to use 'admin'. You can enter an email address if you want or leave
this filed blank(line 19). You'll need to enter your password twice(line20).

NB. Some sensitive information can be hidden from a site's administrators. For example, Django
doesn't store the password you enter; instead, it stores a string derived from the password,
called a hash. Each time you enter your password, Django hashes your entry and compares it to
the stored hash. If the two hashes match, you're authenticated. By requiring hashes to match,
if an attacker gains access to a site's database, they'll be able to read its stored hashes but
not the passwords. When a site is set up properly, it's almost timpossible to get the original
passwords from the hashes.
"""
