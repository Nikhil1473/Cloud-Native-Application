FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install system dependencies required for psutil
RUN apt-get update && apt-get install -y gcc python3-dev

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
# Expose the Flask port
EXPOSE 5001

# Command to run the application
CMD ["flask", "run"]
