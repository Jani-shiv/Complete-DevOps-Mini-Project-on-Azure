# 🚀 Complete DevOps Mini Project on Azure

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure/actions/workflows/deploy.yml/badge.svg)](https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure/actions/workflows/deploy.yml)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://docker.com)
[![Azure](https://img.shields.io/badge/Azure-Deployed-blue.svg)](https://azure.microsoft.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A complete end-to-end DevOps project demonstrating CI/CD pipeline implementation using **GitHub Actions**, **Docker**, and **Azure VM** deployment. Built for learning and interview demonstration purposes.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Development](#-development)
- [Deployment](#-deployment)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

### Problem Statement

Manual deployment processes are error-prone, time-consuming, and don't scale. This project demonstrates how to automate the entire deployment workflow from code commit to production deployment.

### What This Project Demonstrates

- ✅ Professional folder structure following best practices
- ✅ Containerization with Docker (multi-stage builds)
- ✅ CI/CD Pipeline with GitHub Actions
- ✅ Automated testing with pytest
- ✅ Automated deployment to Azure VM
- ✅ SSH-based secure deployment
- ✅ Production-ready application architecture

### Skills Proven

- Linux system administration
- Docker containerization
- CI/CD pipeline design
- Cloud infrastructure (Azure)
- Security best practices (SSH keys, secrets management)
- Version control with Git
- Python/Flask development
- Test-driven development

---

## 🏗 Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Developer     │────▶│    GitHub        │────▶│   Azure VM      │
│   (Git Push)    │     │    Actions       │     │   (Docker)      │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                              │
                              ▼
                        ┌──────────────────┐
                        │  Build & Test    │
                        │  Docker Image    │
                        │  Deploy via SSH  │
                        └──────────────────┘
```

### Workflow

1. **Developer** pushes code to `main` branch
2. **GitHub Actions** triggers automatically
3. **Build Job**: Lint, test, build Docker image
4. **Deploy Job**: SSH into Azure VM, pull code, rebuild and run container
5. **Verification**: Health check confirms successful deployment

---

## 🛠️ Tech Stack

| Component        | Technology                          |
| ---------------- | ----------------------------------- |
| Application      | Python 3.11 + Flask                 |
| Web Server       | Gunicorn (Production WSGI)          |
| Containerization | Docker                              |
| CI/CD            | GitHub Actions                      |
| Cloud            | Microsoft Azure (Student Free Tier) |
| OS               | Ubuntu 22.04 LTS                    |
| Version Control  | Git + GitHub                        |

---

## 📁 Project Structure

```
Complete-DevOps-Mini-Project-on-Azure/
│
├── 📁 .github/workflows/
│   └── deploy.yml              # CI/CD Pipeline configuration
│
├── 📁 src/                     # Application source code
│   ├── app.py                  # Flask application entry
│   ├── config.py               # Configuration management
│   ├── requirements.txt        # Python dependencies
│   ├── templates/              # Jinja2 HTML templates
│   │   ├── base.html
│   │   └── index.html
│   └── static/                 # Static assets
│       ├── css/style.css
│       └── js/main.js
│
├── 📁 docker/                  # Container configuration
│   ├── Dockerfile              # Production Dockerfile
│   ├── Dockerfile.dev          # Development Dockerfile
│   └── .dockerignore
│
├── 📁 scripts/                 # Utility scripts
│   ├── setup.sh                # Local setup script
│   ├── run-local.sh            # Run locally
│   └── run-docker.sh           # Run with Docker
│
├── 📁 tests/                   # Test files
│   ├── conftest.py             # Pytest fixtures
│   ├── test_app.py             # Application tests
│   └── test_health.py          # Health endpoint tests
│
├── 📁 docs/                    # Documentation
│   ├── ARCHITECTURE.md         # System architecture
│   ├── DEPLOYMENT.md           # Deployment guide
│   ├── API.md                  # API documentation
│   └── TROUBLESHOOTING.md      # Common issues
│
├── 📁 infra/                   # Infrastructure
│   └── azure/vm-setup.md       # Azure VM setup guide
│
├── 📄 docker-compose.yml       # Local development
├── 📄 docker-compose.prod.yml  # Production
├── 📄 Makefile                 # Common commands
├── 📄 .env.example             # Environment template
├── 📄 .gitignore               # Git ignore rules
├── 📄 CONTRIBUTING.md          # Contribution guidelines
├── 📄 CHANGELOG.md             # Version history
├── 📄 LICENSE                  # MIT License
└── 📄 README.md                # This file
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker
- Git

### Option 1: Run with Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure.git
cd Complete-DevOps-Mini-Project-on-Azure

# Start application
docker-compose up

# Access at http://localhost:5000
```

### Option 2: Run with Make

```bash
# Setup and run
make install
make run

# Or with Docker
make docker-build
make docker-run
```

### Option 3: Run with Python

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r src/requirements.txt

# Run application
cd src && python app.py
```

---

## 💻 Development

### Available Commands

```bash
make help          # Show all available commands
make install       # Install dependencies
make run           # Run locally with Python
make dev           # Run with Docker Compose (hot-reload)
make test          # Run tests
make lint          # Lint code
make clean         # Clean temporary files
```

### Project Configuration

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

---

## 🚀 Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for complete deployment instructions.

### Quick Deploy

1. **Set up Azure VM** - Follow [infra/azure/vm-setup.md](infra/azure/vm-setup.md)
2. **Configure GitHub Secrets**:
   - `AZURE_VM_HOST` - VM public IP
   - `AZURE_VM_USERNAME` - SSH username
   - `AZURE_VM_SSH_KEY` - Private SSH key
3. **Push to main branch**:
   ```bash
   git push origin main
   ```

GitHub Actions will automatically deploy!

---

## 📡 API Documentation

See [docs/API.md](docs/API.md) for complete API documentation.

### Endpoints

| Method | Endpoint    | Description      |
| ------ | ----------- | ---------------- |
| GET    | `/`         | Home page        |
| GET    | `/health`   | Health check     |
| GET    | `/api/info` | Application info |

### Example

```bash
# Health check
curl http://localhost:5000/health

# Response
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.123456",
  "hostname": "devops-vm",
  "version": "1.0.0"
}
```

---

## 🧪 Testing

```bash
# Run all tests
make test

# Run with coverage
pytest tests/ -v --cov=src

# Run specific test file
pytest tests/test_health.py -v
```

---

## 🔧 Troubleshooting

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for common issues.

### Quick Fixes

```bash
# Docker permission issues
sudo usermod -aG docker $USER
# Then logout and login

# Container not starting
docker logs flask-app-container

# Port already in use
docker stop flask-app-container
docker rm flask-app-container
```

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- ✅ CI/CD pipeline design and implementation
- ✅ Docker containerization from scratch
- ✅ Linux server administration basics
- ✅ Cloud VM deployment on Azure
- ✅ SSH key-based authentication
- ✅ GitHub Actions workflow syntax
- ✅ Secrets management in CI/CD

### What to Learn Next

- Kubernetes for container orchestration
- Terraform for Infrastructure as Code
- Monitoring with Prometheus/Grafana
- Multi-environment deployments

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## ⭐ Show Your Support

Give a ⭐ if this project helped you learn DevOps!

---

<p align="center">
  Built with ❤️ for DevOps Learning
</p>
