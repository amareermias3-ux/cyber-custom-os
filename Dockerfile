# የሊኑክስ (Ubuntu) መሰረትን እንጠቀማለን
FROM ubuntu:22.04

# አላስፈላጊ ጥያቄዎችን ለማስቀረት
ENV DEBIAN_FRONTEND=noninteractive

# አስፈላጊ የሆኑ የሊኑክስ ቱሎችን እና ፓይዘንን መጫን
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nmap \
    tor \
    proxychains4 \
    curl \
    wget \
    iproute2 \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# የስራ ማውጫ (Working Directory)
WORKDIR /app

# ፕሮጀክቱን ወደ ኮንቴይነሩ ማስገባት
COPY . /app

# የፓይዘን ላይብረሪዎችን መጫን
RUN pip3 install --no-cache-dir -r requirements.txt

# ነባሪ ትዕዛዝ
CMD ["python3", "dashboard.py"]