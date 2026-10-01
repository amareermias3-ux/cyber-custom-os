FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    net-tools \
    procps \
    bash \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || pip install --no-cache-dir psutil

COPY . .

RUN chmod +x build_iso.sh install.sh modules/dashboard.py tests/*.sh || true

CMD ["python3", "modules/dashboard.py"]