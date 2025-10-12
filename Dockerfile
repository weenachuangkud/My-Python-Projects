# HAHAHAAHAHAAAAHAHAAHAHAA
FROM python:3.13.8-slim

WORKDIR /app

# Copy requirements file for all dependencies
COPY requirements.txt .

# Install tkinter and other dependencies
RUN apt-get update && apt-get install -y python3-tk || echo "tkinter not installed"
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Do not run any script, just echo a message
CMD ["echo", "Finished building the Docker image :D"]
