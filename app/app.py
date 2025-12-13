"""
Flask Web Application for DevOps Demo Project
Author: DevOps Engineer
Purpose: Simple web app to demonstrate CI/CD pipeline with Docker deployment on Azure
"""

from flask import Flask, jsonify, render_template_string
import os
import socket
from datetime import datetime

app = Flask(__name__)

# HTML Template for the main page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Demo App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        .info-card {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 15px 0;
            border-left: 4px solid #667eea;
        }
        .info-card h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        .info-card p {
            color: #555;
            font-family: monospace;
            font-size: 1em;
        }
        .status {
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            margin-top: 20px;
            font-weight: bold;
        }
        .tech-stack {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .tech-badge {
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 0.9em;
        }
        footer {
            margin-top: 30px;
            color: #888;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Demo App</h1>
        <p class="subtitle">Deployed via GitHub Actions CI/CD Pipeline</p>
        
        <div class="info-card">
            <h3>📡 Server Information</h3>
            <p><strong>Hostname:</strong> {{ hostname }}</p>
            <p><strong>Server Time:</strong> {{ server_time }}</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
        </div>
        
        <div class="info-card">
            <h3>🔧 Deployment Details</h3>
            <p><strong>Version:</strong> {{ version }}</p>
            <p><strong>Container:</strong> Docker</p>
            <p><strong>Cloud:</strong> Azure VM</p>
        </div>
        
        <span class="status">✅ Application Running</span>
        
        <div class="tech-stack">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Flask</span>
            <span class="tech-badge">Docker</span>
            <span class="tech-badge">GitHub Actions</span>
            <span class="tech-badge">Azure</span>
        </div>
        
        <footer>
            <p>Built for DevOps Learning | Azure Student Free Tier</p>
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Main page showing server information and deployment status"""
    return render_template_string(
        HOME_TEMPLATE,
        hostname=socket.gethostname(),
        server_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment=os.getenv('ENVIRONMENT', 'development'),
        version=os.getenv('APP_VERSION', '1.0.0')
    )

@app.route('/health')
def health():
    """Health check endpoint for monitoring and load balancers"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'hostname': socket.gethostname()
    }), 200

@app.route('/api/info')
def api_info():
    """API endpoint returning server and application information"""
    return jsonify({
        'application': 'DevOps Demo App',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'hostname': socket.gethostname(),
        'server_time': datetime.now().isoformat(),
        'endpoints': {
            'home': '/',
            'health': '/health',
            'info': '/api/info'
        }
    })

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    # Run the application
    # In production, this will be behind Gunicorn
    app.run(host='0.0.0.0', port=port, debug=False)
