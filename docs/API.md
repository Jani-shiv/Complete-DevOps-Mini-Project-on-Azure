# API Documentation

## Base URL

```
http://YOUR_VM_IP:5000
```

---

## Endpoints

### GET /

**Description**: Home page with server information and deployment status.

**Response**: HTML page

**Example**:

```bash
curl http://localhost:5000/
```

---

### GET /health

**Description**: Health check endpoint for monitoring and load balancers.

**Response**: `application/json`

**Response Schema**:

```json
{
  "status": "string", // "healthy" or "unhealthy"
  "timestamp": "string", // ISO 8601 format
  "hostname": "string", // Server hostname
  "version": "string" // Application version
}
```

**Example**:

```bash
curl http://localhost:5000/health
```

**Response**:

```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.123456",
  "hostname": "devops-vm",
  "version": "1.0.0"
}
```

**Use Cases**:

- Kubernetes liveness probe
- Load balancer health checks
- Monitoring systems (Prometheus, Datadog)

---

### GET /api/info

**Description**: API endpoint returning detailed application and server information.

**Response**: `application/json`

**Response Schema**:

```json
{
  "application": "string", // Application name
  "version": "string", // Application version
  "environment": "string", // development/production
  "hostname": "string", // Server hostname
  "server_time": "string", // ISO 8601 timestamp
  "endpoints": {
    "home": "string",
    "health": "string",
    "info": "string"
  },
  "tech_stack": {
    "framework": "string",
    "language": "string",
    "container": "string",
    "ci_cd": "string",
    "cloud": "string"
  }
}
```

**Example**:

```bash
curl http://localhost:5000/api/info
```

**Response**:

```json
{
  "application": "DevOps Demo App",
  "version": "1.0.0",
  "environment": "production",
  "hostname": "devops-vm",
  "server_time": "2024-01-15T10:30:00.123456",
  "endpoints": {
    "home": "/",
    "health": "/health",
    "info": "/api/info"
  },
  "tech_stack": {
    "framework": "Flask",
    "language": "Python 3.11",
    "container": "Docker",
    "ci_cd": "GitHub Actions",
    "cloud": "Azure VM"
  }
}
```

---

## Error Responses

### 404 Not Found

**Response**:

```json
{
  "error": "Not Found",
  "message": "The requested resource was not found.",
  "status_code": 404
}
```

### 500 Internal Server Error

**Response**:

```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred.",
  "status_code": 500
}
```

---

## HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 404  | Not Found             |
| 500  | Internal Server Error |

---

## Rate Limiting

Currently, no rate limiting is implemented. For production deployment, consider adding Flask-Limiter.

---

## CORS

Cross-Origin Resource Sharing is not enabled by default. Add Flask-CORS for API access from browsers.
