FROM python:3.11-slim
RUN apt-get update && apt-get install -y python3-tk
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
# Set DISPLAY environment variable for X11
ENV DISPLAY=host.docker.internal:0.0

CMD ["python", "main.py"]
