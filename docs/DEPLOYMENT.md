# Deployment Guide

Complete guide for deploying the DevOps Demo App to Azure VM.

---

## Prerequisites

### Local Machine

- Git installed
- GitHub account with repository access
- SSH client

### Azure

- Azure account (Student or Free Tier)
- Virtual Machine (Ubuntu 22.04 LTS)
- Network Security Group with ports 22, 80, 5000 open

---

## Step 1: Azure VM Setup

### 1.1 Create Virtual Machine

1. Login to [Azure Portal](https://portal.azure.com)
2. Navigate to **Virtual Machines** → **Create**
3. Configure:
   - **Resource Group**: `devops-project-rg` (create new)
   - **VM Name**: `devops-vm`
   - **Region**: Choose nearest
   - **Image**: Ubuntu Server 22.04 LTS
   - **Size**: Standard_B1s (free tier eligible)
   - **Authentication**: SSH public key
   - **Username**: `azureuser`

### 1.2 Configure Networking

Add inbound port rules:

| Priority | Port | Protocol | Action | Name  |
| -------- | ---- | -------- | ------ | ----- |
| 1000     | 22   | TCP      | Allow  | SSH   |
| 1010     | 80   | TCP      | Allow  | HTTP  |
| 1020     | 5000 | TCP      | Allow  | Flask |

### 1.3 Download SSH Key

Save the `.pem` file securely. This cannot be recovered!

---

## Step 2: Prepare VM

### 2.1 Connect via SSH

```bash
# Set correct permissions on key file
chmod 400 ~/Downloads/devops-vm_key.pem

# Connect to VM
ssh -i ~/Downloads/devops-vm_key.pem azureuser@YOUR_VM_IP
```

### 2.2 Install Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER

# Install Git
sudo apt install -y git

# Logout and login again for group changes
exit
```

### 2.3 Verify Installation

```bash
# Reconnect
ssh -i ~/Downloads/devops-vm_key.pem azureuser@YOUR_VM_IP

# Check versions
docker --version
git --version
```

---

## Step 3: GitHub Secrets

Navigate to: **Repository** → **Settings** → **Secrets and variables** → **Actions**

Add these secrets:

| Secret Name         | Value                                                    |
| ------------------- | -------------------------------------------------------- |
| `AZURE_VM_HOST`     | Your VM's public IP address                              |
| `AZURE_VM_USERNAME` | `azureuser`                                              |
| `AZURE_VM_SSH_KEY`  | Contents of your `.pem` file (including BEGIN/END lines) |

---

## Step 4: Deploy

### Automatic Deployment

Push code to `main` branch:

```bash
git add .
git commit -m "Deploy: update application"
git push origin main
```

GitHub Actions will automatically:

1. Run tests
2. Build Docker image
3. SSH into Azure VM
4. Deploy the container

### Manual Deployment (on VM)

```bash
# SSH into VM
ssh -i ~/Downloads/devops-vm_key.pem azureuser@YOUR_VM_IP

# Navigate to app directory
cd ~/devops-flask-app

# Pull latest code
git pull origin main

# Rebuild and restart container
cd docker
docker build -t devops-flask-app -f Dockerfile ../
docker stop flask-app-container || true
docker rm flask-app-container || true
docker run -d --name flask-app-container -p 5000:5000 devops-flask-app
```

---

## Step 5: Verify Deployment

### Check Application

```bash
# Browser
http://YOUR_VM_IP:5000

# Health check
curl http://YOUR_VM_IP:5000/health

# API info
curl http://YOUR_VM_IP:5000/api/info
```

### Check Container Status

```bash
# On VM
docker ps
docker logs flask-app-container
```

---

## Rollback Procedure

If deployment fails:

```bash
# SSH into VM
ssh -i ~/path/to/key.pem azureuser@YOUR_VM_IP

# Check container logs
docker logs flask-app-container

# Rollback to previous commit
cd ~/devops-flask-app
git log --oneline -5  # Find previous working commit
git checkout COMMIT_HASH

# Rebuild and restart
./scripts/run-docker.sh
```

---

## Monitoring

### GitHub Actions

- Check workflow status in **Actions** tab
- Review logs for failed deployments

### Application Health

- Endpoint: `/health`
- Returns: `{"status": "healthy", ...}`

### Container Metrics

```bash
docker stats flask-app-container
```
