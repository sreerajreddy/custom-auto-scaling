FROM python:3.9-slim

WORKDIR /app

COPY custom-scaling.py /app/custom-scaling.py

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install requests psutil schedule

CMD ["python", "custom-scaling.py"]

