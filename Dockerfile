# Use an official Python runtime as a parent image
FROM python:3.12.2
#FROM python:3.14.3
#FROM python:3.12.3-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update \
    # && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Upgrade pip and Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Collect static files
# Need to configure STATIC_ROOT in settings.py
RUN python ./manage.py collectstatic --no-input

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run Gunicorn with the configuration file
CMD ["gunicorn", "-c", "gunicorn_conf.py"]