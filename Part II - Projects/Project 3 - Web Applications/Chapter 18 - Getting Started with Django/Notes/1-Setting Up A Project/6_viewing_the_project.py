"""
Let's make sure that Django haws set up the project properly. Enter the runserver command as 
follows to view the project in its current state:
"""
python manage.py runserver

# Watching for file changes with StatReloader
# [19/Jun/2019 11:58:37] "GET / HTTP/1.1" 200 16348
# [19/Jun/2019 11:58:38] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
# [19/Jun/2019 11:58:38] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
# [19/Jun/2019 11:58:38] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
# [19/Jun/2019 11:58:38] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
# Not Found: /favicon.ico
# [19/Jun/2019 11:58:38] "GET /favicon.ico HTTP/1.1" 404 1978

# System check identified no issues (0 silenced).
# June 19, 2019 - 11:55:32
# Django version 2.2.2, using settings 'learning_log.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.

"""
Django should start a server called the development server, so you can view the project on your
system to see how well it works. When you request a page by entering a URL in a browser, the
Django server responds to that request by building the appropriate page and sending it to the
browser.

At line 17, Django checks to make sure the project is set up properly; at line 19 it reports the
version of Django in use and the name of the settings file in use, and at line 20 it reports the
URL where the project is being served. The URL http://127.0.0.1:8000/ indicates that the project
is listening for requests on port 8000 on your computer, which is called a localhost.

The term localhost refers to a server that only processes requests on your system; it doesn't
allow anyone else to see the pages you're developing.

Open a web browser and enter the URL http://localhost:8000/ or http://127.0.0.1:8000/ if the 
first one doesn't work. You should see a page that Django creates to let you know that all is 
working properly for now, but when you want to stop the server, press CTRL-C in the terminal
where the runserver command was issued.
"""
