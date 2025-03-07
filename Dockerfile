# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    cmake \
    curl \
    #fluxbox \
    g++ \
    gnupg2 \
    libasound2 \
    libcurl4-openssl-dev \
    libgbm1 \
    libgconf-2-4 \
    libgtk-3-0 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxinerama1 \
    libxkbcommon-x11-0 \
    libxkbcommon0 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    make \
    python3-pip \
    python3.8 \
    unzip \
    #wmctrl \
    xvfb \
    && apt-get clean

# Install Chrome and Chromedriver
RUN curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.108/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.108/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /opt/ && \
    unzip /tmp/chrome-linux64.zip -d /opt/ && \
    mv /opt/chrome-linux64 /opt/chrome && \
    mv /opt/chromedriver-linux64 /opt/chromedriver

# Set the working directory
WORKDIR /src

# Install Python packages
COPY requirements.txt ./
RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

# Copy the function code
COPY pyproject.toml pyproject.toml run.py gunicorn_logging.conf ./
COPY src/ ./src/

EXPOSE 5000

# Set the entrypoint to the run.py script
#ENTRYPOINT ["python3.8", "src/run.py"]
#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--pythonpath=./src", "--worker-class=gthread", "--threads=4", "--timeout=30", "--log-level=debug", "--log-config=gunicorn_logging.conf", "run:app"]

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint to the entrypoint.sh script
ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--pythonpath=./", "--worker-class=gthread", "--threads=4", "--timeout=30", "--log-level=debug", "--log-config=gunicorn_logging.conf", "run:app"]