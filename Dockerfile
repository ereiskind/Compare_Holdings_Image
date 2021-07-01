FROM ubuntu

# Update Ubuntu
RUN apt update
RUN apt-get update

# Install Python
RUN apt-get update && apt-get install -y python3

# Install Java
RUN apt-get update && apt-get install -y default-jre