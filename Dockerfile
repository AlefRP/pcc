# Use Alpine Linux version 3.16 as the base image
FROM alpine:3.16

# Set the maintainer label
LABEL maintainer="alefrodrigopereira@yahoo.com.br"

# Install Python3 and pip
RUN apk add --no-cache python3 py3-pip

# Ensure the directory is created first (if not already present)
RUN mkdir -p /src

# Set the working directory to the location of the script
WORKDIR /src

# Copy the Python script into the container
COPY car_v2.py /src/

# Ensure Python script is executable
RUN chmod +x car_v2.py

# Command to run the script when the container starts
CMD ["python3", "car_v2.py"]