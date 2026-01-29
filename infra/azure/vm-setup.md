# Azure VM Setup Guide

Step-by-step guide for creating and configuring an Azure Virtual Machine for this project.

---

## Prerequisites

- Azure account (Student or Free Tier)
- SSH client installed locally

---

## Step 1: Create Resource Group

1. Login to [Azure Portal](https://portal.azure.com)
2. Search for "Resource groups"
3. Click "+ Create"
4. Configure:
   - **Subscription**: Azure for Students
   - **Resource group**: `devops-project-rg`
   - **Region**: Choose nearest location

---

## Step 2: Create Virtual Machine

### Basic Configuration

| Setting              | Value                             |
| -------------------- | --------------------------------- |
| Subscription         | Azure for Students                |
| Resource group       | devops-project-rg                 |
| Virtual machine name | devops-vm                         |
| Region               | (Choose nearest)                  |
| Availability options | No infrastructure redundancy      |
| Image                | Ubuntu Server 22.04 LTS - Gen2    |
| VM architecture      | x64                               |
| Size                 | Standard_B1s (Free tier eligible) |

### Administrator Account

| Setting               | Value                 |
| --------------------- | --------------------- |
| Authentication type   | SSH public key        |
| Username              | azureuser             |
| SSH public key source | Generate new key pair |
| Key pair name         | devops-vm_key         |

### Inbound Port Rules

| Setting              | Value                |
| -------------------- | -------------------- |
| Public inbound ports | Allow selected ports |
| Select inbound ports | SSH (22), HTTP (80)  |

---

## Step 3: Configure Networking

### Network Security Group Rules

After VM creation, add custom port rules:

1. Go to VM → Networking
2. Click "Add inbound port rule"
3. Add rule:

| Setting                 | Value            |
| ----------------------- | ---------------- |
| Source                  | Any              |
| Source port ranges      | \*               |
| Destination             | Any              |
| Destination port ranges | 5000             |
| Protocol                | TCP              |
| Action                  | Allow            |
| Priority                | 1010             |
| Name                    | Allow-Flask-5000 |

---

## Step 4: Download SSH Key

**Important**: Download the `.pem` file when VM is created. This file cannot be recovered!

Store in a secure location:

- Linux/macOS: `~/.ssh/devops-vm_key.pem`
- Windows: `C:\Users\YourName\.ssh\devops-vm_key.pem`

Set permissions:

```bash
chmod 400 ~/.ssh/devops-vm_key.pem
```

---

## Step 5: Get Public IP

1. Go to VM Overview
2. Copy the **Public IP address**
3. Save this for GitHub Secrets

---

## Cost Optimization

### Free Tier Eligible

- Standard_B1s: ~$7.59/month (often free for students)
- 750 hours/month free for 12 months

### Stop VM When Not in Use

```bash
# Stop VM to avoid charges
az vm stop --resource-group devops-project-rg --name devops-vm

# Start when needed
az vm start --resource-group devops-project-rg --name devops-vm
```

---

## Quick Reference

| Resource       | Value             |
| -------------- | ----------------- |
| Resource Group | devops-project-rg |
| VM Name        | devops-vm         |
| Username       | azureuser         |
| Ports Open     | 22, 80, 5000      |
| OS             | Ubuntu 22.04 LTS  |
| Size           | Standard_B1s      |
