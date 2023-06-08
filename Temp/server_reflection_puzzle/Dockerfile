# Use a base Python image
FROM python:3.9

# Copy application files into the container
COPY app.py /app/app.py
COPY result.html /app/templates/result.html
COPY flag.txt /app/flag.txt 

# Install dependencies
RUN pip install flask

# Expose port 5000 for the application
EXPOSE 5000

# Set working dir
WORKDIR /app

# Set the cmd to run the app
CMD ["python", "app.py"]

