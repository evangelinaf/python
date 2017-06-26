############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Python
FROM python:3.5

# File Author / Maintainer
MAINTAINER Eva

# Set the default directory where CMD will execute
WORKDIR /usr/src/app

# Copy requirements to /usr/src/app and install 
COPY requirements.txt ./
RUN apt-get install -y python
RUN pip3 install gitsome
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application folder inside the container
ADD . .

# Expose ports
EXPOSE 80

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python server.py
