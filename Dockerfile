FROM ubuntu

# Update Ubuntu
RUN apt update
RUN apt-get update

# Install Python
RUN apt-get update && apt-get install -y python3

# Install Java
RUN apt-get update && apt-get install -y default-jre

# Install OpenRefine
RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/OpenRefine/OpenRefine/releases/download/3.4.1/openrefine-linux-3.4.1.tar.gz
RUN tar xzvf openrefine-linux-3.4.1.tar.gz