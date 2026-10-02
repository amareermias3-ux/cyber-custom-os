from flask import Flask, render_template_string, jsonify
import psutil
import socket

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Custom OS - Web Dashboard</title>
    <style>
        body { background-color: #0d1117; color: #58a6ff; font-family: 'Courier New', monospace; padding: 20px; }
        .card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin-bottom: 20px; }
        h1 { color: #2ea043; text-align: center; }
        .metric { font-size: 1.2rem; margin: 10px 0; color: #c9d1d9; }
        .val { color: #79c0ff; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🛡️ Cyber Custom OS - Real-Time Web Dashboard</h1>
    <div class="card">
        <h3>📍 System Info</h3>
        <p class="metric">Hostname: <span class="val" id="hostname">-</span></p>
        <p class="metric">Local IP: <span class="val" id="ip">-</span></p>
    </div>
    <div class="card">
        <h3>📊 Resource Monitor</h3>
        <p class="metric">CPU Usage: <span class="val" id="cpu">-</span>%</p>
        <p class="metric">RAM Usage: <span class="val" id="ram">-</span>%</p>
        <p class="metric">Disk Space: <span class="val" id="disk">-</span>%</p>
    </div>

    <script>
        async function fetchMetrics() {
            try {
                const res = await fetch('/api/stats');
                const data = await res.json();
                document.getElementById('hostname').innerText = data.hostname;
                document.getElementById('ip').innerText = data.ip;
                document.getElementById('cpu').innerText = data.cpu;
                document.getElementById('ram').innerText = data.ram;
                document.getElementById('disk').innerText = data.disk;
            } catch (e) {
                console.error("Error fetching stats:", e);
            }
        }
        setInterval(fetchMetrics, 2000);
        fetchMetrics();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/stats')
def get_stats():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    except Exception:
        hostname = "localhost"
        ip = "127.0.0.1"

    return jsonify({
        'hostname': hostname,
        'ip': ip,
        'cpu': psutil.cpu_percent(interval=0.1),
        'ram': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    })

if __name__ == '__main__':
    print("[+] Starting Web Dashboard on http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)