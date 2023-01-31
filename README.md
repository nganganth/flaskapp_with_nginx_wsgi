# flaskapp_with_nginx_wsgi
a web application using Flask framework with Nginx web server and WSGI

OS: Windows

Env: Python 3.8.5


### Create Virtual Environment
>The purpose of a Python virtual environments is to allow one to create multiple distinct Python environments for the same version of Python, but with different sets of Python modules and packages installed. It is recommended that you always use Python virtual environments and not install additional Python packages direct into your Python installation.

1. Install virtualenv
```
> pip install virtualenv
```

2. Create a virtualenv in which ever directory you are
```
> virtualenv myenv
```

3. By using the below command to activate it and then you are in a Python virtual environment
```
> myenv\Scripts\activate
```

4. Deactivate it
```
> $ deactivate
```

### Install Python dependencies
```
> pip3 install flask gunicorn requests
```

*Since Gunicorn is for a UNIX environment and is incompatible with Windows, I will use waitress instead of gunicorn*
```
> pip3 install flask waitress requests
```

### Test Waitress's ability
```
> waitress-serve --listen=127.0.0.1:5000 wsgi:app
```

### Install Nginx
1. Download nginx version for Windows
```
https://nginx.org/en/download.html
```

2. Unzip folder and execute nginx.exe
3. Go to http://localhost/ and we should see the "Welcome to Nginx" default page. If we see that page, then we can be sure that Nginx has been installed properly.

### Configure Nginx
According to Waitress documentation:
> unix_socket Path of Unix socket(string). If a socket path is specified, a Unix domain socket is made instead of the usual inet domain socket
> Not available on Windows

Because of that, instead of running it from a named pipe you can run it in a local port and reverse proxy that port with nginx.

```
location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $host:$server_port;
    proxy_set_header X-Forwarded-Port $server_port;
}
```

###### Restart Nginx
Stop and restart after updating nginx.conf in order to reflect the changes
```
> nginx.exe -s quit
```
or 

Go to Task Manager and end nginx.exe running processes

### Result
Go to http://localhost/ and we can see the running flask application (http://localhost:5000)
