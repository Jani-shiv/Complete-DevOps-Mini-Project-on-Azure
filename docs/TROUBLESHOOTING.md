# Troubleshooting Guide

Common issues and their solutions.

---

## SSH Connection Issues

### Error: `Connection timed out`

```
ssh: connect to host X.X.X.X port 22: Connection timed out
```

**Solutions**:

1. Verify VM is running in Azure Portal
2. Check Network Security Group allows port 22
3. Confirm the IP address is correct

### Error: `Permission denied (publickey)`

**Solutions**:

```bash
# Fix key file permissions
chmod 400 ~/path/to/key.pem

# Verify correct username
ssh -i ~/path/to/key.pem azureuser@YOUR_IP
```

### Error: `WARNING: UNPROTECTED PRIVATE KEY FILE!`

**Solution**:

```bash
chmod 400 ~/path/to/key.pem
```

---

## Docker Issues

### Error: `permission denied while trying to connect to the Docker daemon`

**Solution**:

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Logout and login again
exit
ssh -i ~/path/to/key.pem azureuser@YOUR_IP
```

### Error: `port is already allocated`

**Solution**:

```bash
# Find and stop conflicting container
docker ps -a
docker stop CONTAINER_ID
docker rm CONTAINER_ID

# Or use different port
docker run -d -p 5001:5000 devops-flask-app
```

### Error: `no space left on device`

**Solution**:

```bash
# Remove unused Docker resources
docker system prune -a

# Check disk space
df -h
```

---

## Application Issues

### Container Starts but App Not Accessible

**Check**:

```bash
# Verify container is running
docker ps

# Check container logs
docker logs flask-app-container

# Test locally on VM
curl http://localhost:5000/health

# Check port mapping
docker port flask-app-container
```

### Health Check Failing

**Check**:

```bash
# View container logs
docker logs flask-app-container --tail 50

# Check if app is listening
docker exec flask-app-container curl http://localhost:5000/health
```

### Application Returns 500 Error

**Check**:

```bash
# View application logs
docker logs flask-app-container

# Enter container for debugging
docker exec -it flask-app-container /bin/bash
```

---

## GitHub Actions Issues

### Workflow Not Triggering

**Check**:

1. Workflow file in `.github/workflows/`
2. Push to correct branch (`main`)
3. Workflow syntax is valid
4. Repository has Actions enabled

### SSH Step Fails

**Check**:

1. Secrets are correctly set:
   - `AZURE_VM_HOST`
   - `AZURE_VM_USERNAME`
   - `AZURE_VM_SSH_KEY`
2. VM is running and accessible
3. SSH key includes full content (BEGIN to END lines)

### Build Step Fails

**Check**:

```bash
# Test locally
docker build -t test-app -f docker/Dockerfile .

# Check for syntax errors
python -m py_compile src/app.py
```

---

## Azure VM Issues

### VM Not Starting

**Solutions**:

1. Check subscription quota/limits
2. Verify region availability
3. Try different VM size

### Cannot Access Application from Internet

**Check**:

1. Network Security Group rules:
   - Port 5000 must be open
   - Source: Any (or your IP)
   - Destination: Any
   - Action: Allow

2. VM has public IP assigned

3. Application is bound to `0.0.0.0`:
   ```python
   app.run(host='0.0.0.0', port=5000)
   ```

---

## Quick Diagnostic Commands

```bash
# On VM - Full system check
docker ps -a                  # All containers
docker images                 # All images
docker logs CONTAINER_NAME    # Container logs
curl http://localhost:5000/health  # Health check
sudo systemctl status docker  # Docker service
df -h                         # Disk space
free -h                       # Memory usage
```

---

## Getting Help

1. Check container logs first
2. Review GitHub Actions logs
3. Test locally with Docker
4. Open an issue with:
   - Error message
   - Steps to reproduce
   - Environment details
