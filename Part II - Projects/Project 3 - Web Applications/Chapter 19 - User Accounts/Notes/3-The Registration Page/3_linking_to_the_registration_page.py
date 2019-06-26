"""
Next we'll add the code to show the registration page link to any user who isn't currently
logged in:
"""

# base.html
--snip--
{% if user.is_authenticated % } 
Hello, {{user.username}}.
{% else % }
<a href = "{% url 'users:register' %}" > Register < /a >
<a href = "{% url 'users:login' %}" > Log in < /a >
{% endif % }
--snip--

"""
Now users who are logged in see a personalized greeting and a logout link. Users who aren't 
logged in see a registration page link and a login link. Try out the registration page by making
several user accounts with different usernames.

In the next section, we'll restrict some of the pages so they're available only to registered 
users, and we'll make sure every topic belongs to a specific user.

NB. The registration system we've set up allows anyone to make any number of accounts for 
Learning Log. But some systems require users to confirm their identity by sending a confirmation 
email the user must reply to. By doing so, the system generates fewer spam accounts that the 
simple system we're using here. Hoever, when you're learning to build apps, it's perfectly 
appropriate to practise with a simple user registration system like the one we're using.
"""
