# Use python base slim image
FROM python:3.9-slim

# Add metadata to our image
LABEL maintainer="Hassan Ali"
LABEL version="1.0"
LABEL description="This is a base image for Python 3.9."

# Set the working directory
WORKDIR /app

# Copy our python script
COPY main.py .

# Run the python script
CMD ["python", "main.py"]