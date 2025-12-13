# 🚀 Complete DevOps Mini Project on Azure

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure/actions/workflows/deploy.yml/badge.svg)](https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure/actions/workflows/deploy.yml)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://docker.com)
[![Azure](https://img.shields.io/badge/Azure-Deployed-blue.svg)](https://azure.microsoft.com)

A complete end-to-end DevOps project demonstrating CI/CD pipeline implementation using **GitHub Actions**, **Docker**, and **Azure VM** deployment. Built for learning and interview demonstration purposes.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Local Development Setup](#-local-development-setup)
- [Azure VM Setup](#️-azure-vm-setup)
- [GitHub Secrets Configuration](#-github-secrets-configuration)
- [CI/CD Pipeline Explanation](#-cicd-pipeline-explanation)
- [Deployment Verification](#-deployment-verification)
- [Troubleshooting](#-troubleshooting)
- [Learning Outcomes](#-learning-outcomes)
- [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

### Problem Statement
Manual deployment processes are error-prone, time-consuming, and don't scale. This project demonstrates how to automate the entire deployment workflow from code commit to production deployment.

### What This Project Demonstrates
- ✅ Containerization with Docker
- ✅ CI/CD Pipeline with GitHub Actions
- ✅ Automated deployment to Azure VM
- ✅ SSH-based secure deployment
- ✅ Infrastructure setup on cloud
- ✅ Production-ready application architecture

### Skills Proven
- Linux system administration
- Docker containerization
- CI/CD pipeline design
- Cloud infrastructure (Azure)
- Security best practices (SSH keys, secrets management)
- Version control with Git

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

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Application | Python 3.11 + Flask |
| Web Server | Gunicorn (Production WSGI) |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | Microsoft Azure (Student Free Tier) |
| OS | Ubuntu 22.04 LTS |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
Complete-DevOps-Mini-Project-on-Azure/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD Pipeline configuration
├── app/
│   ├── app.py                  # Flask application
│   ├── Dockerfile              # Docker configuration
│   └── requirements.txt        # Python dependencies
├── docs/
│   └── COMPLETE_PROJECT_GUIDE.json  # Full documentation
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

---

## 📋 Prerequisites

### On Your Local Machine
- Git installed
- GitHub account
- Azure Student account (free tier)

### On Azure VM
- Ubuntu 22.04 LTS
- Docker installed
- Git installed
- SSH access enabled

---

## 💻 Local Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure.git
cd Complete-DevOps-Mini-Project-on-Azure
```

### 2. Run Locally with Python
```bash
cd app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Access at: http://localhost:5000

### 3. Run Locally with Docker
```bash
cd app
docker build -t devops-flask-app .
docker run -d -p 5000:5000 --name flask-app devops-flask-app
```
Access at: http://localhost:5000

---

## ☁️ Azure VM Setup

### Step 1: Create Azure VM

```bash
# Login to Azure Portal (portal.azure.com)
# Navigate to: Virtual Machines > Create

# Configuration:
# - Subscription: Azure for Students
# - Resource Group: devops-project-rg (create new)
# - VM Name: devops-vm
# - Region: Choose nearest (e.g., Central India)
# - Image: Ubuntu Server 22.04 LTS
# - Size: Standard_B1s (free tier eligible)
# - Authentication: SSH public key
# - Username: azureuser
# - Inbound ports: SSH (22), HTTP (80), Custom (5000)
```

### Step 2: Connect to VM
```bash
# Connect via SSH
ssh -i ~/.ssh/your-key.pem azureuser@YOUR_VM_PUBLIC_IP
```

### Step 3: Prepare VM (Run these commands on VM)

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (avoid using sudo for docker)
sudo usermod -aG docker $USER

# Install Git
sudo apt install -y git

# Verify installations
docker --version
git --version

# IMPORTANT: Log out and log back in for group changes
exit
```

### Step 4: Open Firewall Port
```bash
# On Azure Portal:
# VM > Networking > Add inbound port rule
# - Port: 5000
# - Protocol: TCP
# - Action: Allow
# - Priority: 1010
# - Name: Allow-Flask-5000
```

---

## 🔐 GitHub Secrets Configuration

Navigate to: **Repository > Settings > Secrets and variables > Actions**

Add these secrets:

| Secret Name | Value | How to Get |
|-------------|-------|------------|
| `AZURE_VM_HOST` | Your VM's public IP | Azure Portal > VM > Overview |
| `AZURE_VM_USERNAME` | `azureuser` | The username you set during VM creation |
| `AZURE_VM_SSH_KEY` | Your private SSH key | Contents of your `.pem` or private key file |

### Getting SSH Private Key
```bash
# On your local machine
cat ~/.ssh/your-key.pem
# Copy entire content including BEGIN and END lines
```

---

## 🔄 CI/CD Pipeline Explanation

### Pipeline Triggers
```yaml
on:
  push:
    branches: [main]     # Triggers on push to main
  pull_request:
    branches: [main]     # Triggers on PR to main
  workflow_dispatch:     # Manual trigger option
```

### Job 1: Build and Test
1. **Checkout code** - Gets latest code from repository
2. **Setup Python** - Installs Python 3.11
3. **Install dependencies** - Installs Flask, pytest, flake8
4. **Lint code** - Checks for syntax errors
5. **Smoke test** - Verifies app can import
6. **Build Docker** - Creates Docker image
7. **Test container** - Runs container and tests endpoints

### Job 2: Deploy
1. **SSH into Azure VM** - Secure connection using secrets
2. **Pull latest code** - Gets newest version from GitHub
3. **Stop old container** - Removes previous deployment
4. **Build new image** - Creates fresh Docker image
5. **Start new container** - Runs application
6. **Verify deployment** - Health check confirmation

---

## ✅ Deployment Verification

### Check Application
```bash
# From your browser
http://YOUR_VM_IP:5000

# Health check endpoint
http://YOUR_VM_IP:5000/health

# API endpoint
http://YOUR_VM_IP:5000/api/info
```

### Check on VM
```bash
# SSH into VM
ssh azureuser@YOUR_VM_IP

# Check running containers
docker ps

# Check container logs
docker logs flask-app-container

# Test locally on VM
curl http://localhost:5000/health
```

---

## 🔧 Troubleshooting

### Pipeline Fails at SSH Step
```
Error: ssh: connect to host X.X.X.X port 22: Connection timed out
```
**Solution:** 
- Check VM is running
- Verify NSG allows port 22
- Confirm IP address is correct

### Container Won't Start
```bash
# Check logs
docker logs flask-app-container

# Check if port is in use
sudo lsof -i :5000
```

### Permission Denied (Docker)
```bash
# Add user to docker group
sudo usermod -aG docker $USER
# Log out and log back in
```

### Application Not Accessible
1. Check container is running: `docker ps`
2. Check firewall: Port 5000 must be open in Azure NSG
3. Check application logs: `docker logs flask-app-container`

---

## 📚 Learning Outcomes

### After Completing This Project, You Will Understand:
- ✅ How CI/CD pipelines work in real projects
- ✅ Docker containerization from scratch
- ✅ Linux server administration basics
- ✅ SSH key-based authentication
- ✅ GitHub Actions workflow syntax
- ✅ Cloud VM deployment on Azure
- ✅ Secrets management in CI/CD

### What to Learn Next:
- Kubernetes for container orchestration
- Terraform for Infrastructure as Code
- Monitoring with Prometheus/Grafana
- Multi-environment deployments (staging/production)
- Database integration and migrations

---

## 🚀 Future Enhancements

- [ ] Add database (PostgreSQL)
- [ ] Implement HTTPS with Let's Encrypt
- [ ] Add monitoring and alerting
- [ ] Multi-stage Docker builds
- [ ] Kubernetes deployment
- [ ] Terraform infrastructure
- [ ] Nginx reverse proxy

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## ⭐ Show Your Support

Give a ⭐ if this project helped you learn DevOps!

---

**Built with ❤️ for DevOps Learners**
