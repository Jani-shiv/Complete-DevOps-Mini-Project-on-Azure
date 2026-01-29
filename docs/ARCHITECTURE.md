# System Architecture

## Overview

The DevOps Demo App is a complete CI/CD demonstration project showcasing automated deployment workflows using industry-standard tools.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              ARCHITECTURE DIAGRAM                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Developer  │────▶│     GitHub      │────▶│    Azure VM     │
│  Workstation│     │   Repository    │     │   (Production)  │
└─────────────┘     └────────┬────────┘     └────────┬────────┘
                             │                       │
                             ▼                       ▼
                    ┌─────────────────┐     ┌─────────────────┐
                    │  GitHub Actions │     │  Docker Engine  │
                    │   (CI/CD)       │────▶│   Container     │
                    └─────────────────┘     └─────────────────┘
```

---

## Components

### 1. Application Layer (`src/`)

| Component    | Description                                |
| ------------ | ------------------------------------------ |
| `app.py`     | Flask web application entry point          |
| `config.py`  | Environment-based configuration management |
| `templates/` | Jinja2 HTML templates                      |
| `static/`    | CSS, JavaScript, and images                |

### 2. Containerization (`docker/`)

| Component        | Description                  |
| ---------------- | ---------------------------- |
| `Dockerfile`     | Production multi-stage build |
| `Dockerfile.dev` | Development with hot-reload  |
| `.dockerignore`  | Build context exclusions     |

### 3. CI/CD Pipeline (`.github/workflows/`)

```yaml
Pipeline Flow:
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  Checkout   │──▶│  Build &    │──▶│   Deploy    │
│   Code      │   │   Test      │   │  to Azure   │
└─────────────┘   └─────────────┘   └─────────────┘
```

### 4. Infrastructure (`infra/`)

- Azure VM configuration
- Network security rules
- SSH key management

---

## Data Flow

1. **Development**: Developer writes code locally
2. **Version Control**: Code pushed to GitHub `main` branch
3. **CI Trigger**: GitHub Actions workflow automatically triggers
4. **Build & Test**: Application is linted, tested, and Docker image built
5. **Deploy**: SSH into Azure VM, pull latest code, restart container
6. **Verification**: Health check confirms successful deployment

---

## Technology Stack

| Layer       | Technology          | Purpose                 |
| ----------- | ------------------- | ----------------------- |
| Application | Python 3.11 + Flask | Web framework           |
| Server      | Gunicorn            | Production WSGI server  |
| Container   | Docker              | Containerization        |
| CI/CD       | GitHub Actions      | Automation              |
| Cloud       | Azure VM            | Hosting                 |
| OS          | Ubuntu 22.04 LTS    | Server operating system |

---

## Security Considerations

1. **SSH Key Authentication**: Password-less, secure access
2. **GitHub Secrets**: Encrypted credential storage
3. **Non-root Container User**: Reduced attack surface
4. **Health Checks**: Continuous monitoring
5. **HTTPS Ready**: Nginx reverse proxy support (future)
