# FROM python:3.11-slim
# RUN apt-get update && apt-get install -y python3-tk
# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .
# # Set DISPLAY environment variable for X11
# ENV DISPLAY=host.docker.internal:0.0

# CMD ["python", "main.py"]


FROM python:3.13-slim

# Install Tkinter and X11 dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files from src directory
COPY src/ .

# Install Python dependencies (if any)
# RUN pip install -r requirements.txt (uncomment if requirements.txt exists)

# Expose port (if HTTP is used, placeholder)
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]
