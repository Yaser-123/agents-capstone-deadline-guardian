# Base image
FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir google-generativeai

# Expose port for Cloud Run (even though this is a CLI tool)
EXPOSE 8080

# Run your program
CMD ["python", "run.py"]
