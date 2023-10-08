# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add current directory files to /app in container
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download model
RUN python instructor_api/model.py

# Open port 80 for the app
EXPOSE 8000

# Run the application
CMD ["uvicorn", "instructor_api.api:app", "--host", "0.0.0.0", "--port", "8000"]