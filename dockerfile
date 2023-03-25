FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY fastap_sqlite_survey /app

# Install any necessary dependencies
RUN pip install -r /app/requirements.txt

# Expose the port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
