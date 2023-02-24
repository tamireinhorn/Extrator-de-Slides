# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the current directory contents into the container at /app
COPY . /app

RUN ls -la /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r app/requirements.txt

# Set the working directory to /src
WORKDIR app/src/ExtratorSlides

# Run the program
CMD ["python", "SlideExtractor.py"]



