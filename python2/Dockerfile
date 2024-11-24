# Use a lightweight Python image
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Copy requirements first (for layer caching)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python application
COPY app.py /app/

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
