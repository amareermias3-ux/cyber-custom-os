# Python 3.11 Debian-based base image
FROM python:3.11-slim-bullseye

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Essential system tools መጫን
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    procps \
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Working directory ማዘጋጀት
WORKDIR /app

# Python dependencies (psutil) መጫን
RUN pip install --no-cache-dir psutil

# የፕሮጀክቱን ፋይሎች ኮፒ ማድረግ
COPY . /app

# የ Shell ስክሪፕቶች Executable እንዲሆኑ ማድረግ
RUN chmod +x modules/privacy/*.sh \
    modules/security/*.sh \
    modules/forensics/*.sh \
    modules/offensive/*.sh \
    install.sh \
    tests/test_modules.sh 2>/dev/null || true

# Container ሲነሳ በነባሪነት CLI Dashboard እንዲከፈት ማድረግ
CMD ["python", "modules/dashboard.py"]