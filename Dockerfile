FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY custom-scaling.py /app/custom-scaling.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Install dependencies
RUN pip install requests psutil schedule

# Set the command to run the script
CMD ["python", "custom-scaling.py"]

