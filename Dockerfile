# Dockers are tools that can package software into containers that run reliably in any environment
# Dockers are similar to virtual machines, it virtualizes the OS. All apps or containers are run by a single container
# 3 elements in a docker
# 1. Dockerfile : Code that tells the docker how to build an image
# Start from an existing template like ubuntu or windows
# Run to install dependencies into image
# Set environment variables
# Set a default command that is executed when we start a container
# 2. Image : A snapshot of the software along with all the dependencies and OS
# Image file is created by running a Docker build command
# 3. Container : The image is brought to life as a container by a docker run command

FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]