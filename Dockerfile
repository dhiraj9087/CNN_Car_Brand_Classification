# Use an official Python runtime as a base image
FROM python:3.10-slim



# Install HDF5 library
RUN apt-get update && apt-get install -y libhdf5-dev


# Install pkg-config
RUN apt-get update && apt-get install -y pkg-config

# # Install HDF5 library
# RUN apt-get update && apt-get install -y libhdf5-dev

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . /app/

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
