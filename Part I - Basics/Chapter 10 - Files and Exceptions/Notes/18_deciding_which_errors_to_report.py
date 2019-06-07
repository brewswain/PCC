"""
How do you know when to report an error to your users and when to fail
silently? If users know which texts are supposed to be analyzed, they
might appreciate a message informing them why some texts were not
analyzed. Ig users expect to see some results but don't know which
books are supposed to be analyzed, they might not need to know that some 
texts were unavailable.

Giving users information they aren't looking for can decrease the usability 
of your program. Python's error-handling structures give you finegrained 
control over how much to share with users when things go wrong; it's up to
you to decide how much information to share. Well-written, properly tested 
code is not very prone to internal errors, such as syntax or logical errors.
But every time your program depends on something external, such as user input, 
the existence of a file, or the availability of a network connection, there is 
a possibility of an exception being raised. A little experience will help you
know where to include exception handling blocks in your program and how much 
to report to users about errors that arise.
"""
