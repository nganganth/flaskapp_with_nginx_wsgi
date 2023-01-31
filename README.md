# flaskapp_with_nginx_wsgi
a web application using Flask framework with Nginx Nginx web server and WSGI

OS: Windows


#Create Virtual Environment
1. Install virtualenv
> pip install virtualenv

2. Create a virtualenv in which ever directory you are
> virtualenv myenv

3. By using the below command to activate it and then you are in a Python virtual environment
> myenv\Scripts\activate

4. Deactivate it
$ deactivate

# Install Python dependencies
> pip3 install flask gunicorn requests

※ Since Gunicorn is for a UNIX environment and is incompatible with Windows,
I will use waitress instead of gunicorn
> pip3 install flask waitress requests


# Test Waitress's ability
> waitress-serve --listen=127.0.0.1:5000 wsgi:app
