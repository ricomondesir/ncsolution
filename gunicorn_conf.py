# gunicorn_conf.py

# The IP and port Gunicorn will bind to inside the container. This should be accessible by the Nginx container.
bind = "0.0.0.0:8000"

# The number of worker processes. A common rule of thumb is `(2 * CPU_CORES) + 1`. Adjust this based on container's resources.
workers = 3

# The path to the WSGI application object.
# This is typically 'project_name.wsgi:application'. In this case, it's 'Schedule_int.wsgi:application'.
wsgi_app = "ncsolution.wsgi:application"

# The directory where Gunicorn will look for the WSGI file. This should be the root of your Django project.
chdir = "/usr/src/app"

# User and group for Gunicorn processes. It's good practice to run Gunicorn as a non-root user.
# user = "gunicorn"
# group = "gunicorn"

# Logging settings
loglevel = "info"
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr

# Timeout settings
timeout = 30
keepalive = 2