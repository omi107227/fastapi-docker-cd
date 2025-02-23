# Use Ubuntu as the base image
FROM ubuntu:latest

# Install Python and dependencies
RUN apt update && apt install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install required dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
