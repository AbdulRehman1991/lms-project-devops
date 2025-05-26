# FROM python:3.11-slim

# # Install required packages
# RUN apt-get update && apt-get install -y \
#     python3-tk \
#     xfce4 \
#     x11vnc \
#     xvfb \
#     wget \
#     supervisor \
#     && rm -rf /var/lib/apt/lists/*

# # Set environment
# ENV DISPLAY=:1
# ENV GEOMETRY=1280x800

# # Create workspace
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy your code
# COPY . .

# # Copy supervisord config
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# # Expose VNC port
# EXPOSE 5901

# # Start supervisor to launch VNC + app
# CMD ["/usr/bin/supervisord"]



# FROM python:3.11-slim

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code
# COPY . .

# # Expose port (adjust according to your app)
# EXPOSE 5000

# # Run the app (update as needed)
# CMD ["python", "main.py"]

# FROM python:3.11-slim
# RUN apt-get update && apt-get install -y python3-tk
# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .
# # Set DISPLAY environment variable for X11
# ENV DISPLAY=host.docker.internal:0.0

# CMD ["python", "main.py"]


# FROM python:3.13-slim

# Install Tkinter and X11 dependencies
# RUN apt-get update && apt-get install -y \
#     python3-tk \
#     libx11-6 \
#     libxext6 \
#     libxrender1 \
#     && rm -rf /var/lib/apt/lists/*

# # Set working directory
# WORKDIR /app

# # Copy application files from src directory
# COPY . .

# # Install Python dependencies (if any)
# # RUN pip install -r requirements.txt (uncomment if requirements.txt exists)

# # Expose port (if HTTP is used, placeholder)
# EXPOSE 8080

# # Run the application
# CMD ["python", "main.py"]

# FROM python:3.11-slim
# RUN apt-get update && apt-get install -y python3-tk
# WORKDIR /app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .
# # Set DISPLAY environment variable for X11
# ENV DISPLAY=host.docker.internal:0.0

# CMD ["python", "main.py"]# Use an official Python 3.13 runtime as a base image

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
#EXPOSE 8080

# Run the application
CMD ["python", "main.py"]