# Contributing to DevOps Demo App

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

---

## 🚀 Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/Complete-DevOps-Mini-Project-on-Azure.git
cd Complete-DevOps-Mini-Project-on-Azure
```

### 3. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r src/requirements.txt
pip install pytest flake8 black

# Or use Make
make install
```

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

---

## 📝 Development Workflow

### Running Locally

```bash
# With Python
make run

# With Docker
make dev

# With Docker Compose
docker-compose up
```

### Running Tests

```bash
# Run all tests
make test

# Run quick tests (stop on first failure)
make test-quick
```

### Linting

```bash
# Check code style
make lint

# Format code with Black
make format
```

---

## 📋 Pull Request Process

### 1. Update Your Fork

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/Complete-DevOps-Mini-Project-on-Azure.git
git fetch upstream
git merge upstream/main
```

### 2. Make Your Changes

- Write clean, readable code
- Follow existing code style
- Add tests for new features
- Update documentation if needed

### 3. Test Your Changes

```bash
make test
make lint
```

### 4. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git commit -m "feat: add new endpoint for user profiles"
git commit -m "fix: resolve health check timeout issue"
git commit -m "docs: update deployment guide for Azure"
```

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

---

## 📖 Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

| Type       | Description                     |
| ---------- | ------------------------------- |
| `feat`     | New feature                     |
| `fix`      | Bug fix                         |
| `docs`     | Documentation changes           |
| `style`    | Code style changes (formatting) |
| `refactor` | Code refactoring                |
| `test`     | Adding/updating tests           |
| `chore`    | Maintenance tasks               |

---

## 🧪 Testing Guidelines

- Write tests for new features
- Maintain or improve code coverage
- Tests should be independent and repeatable
- Use meaningful test names

Example:

```python
def test_health_endpoint_returns_200():
    """Test that health endpoint returns 200 status."""
    response = client.get('/health')
    assert response.status_code == 200
```

---

## 📁 Project Structure

```
├── src/                 # Application source code
├── docker/              # Docker configuration
├── scripts/             # Utility scripts
├── tests/               # Test files
├── docs/                # Documentation
└── .github/workflows/   # CI/CD pipelines
```

---

## ❓ Questions?

- Open an issue for discussion
- Tag your issue with appropriate labels
- Be respectful and constructive

---

## 📜 Code of Conduct

- Be respectful and inclusive
- Constructive feedback only
- Help others learn and grow

Thank you for contributing! 🎉
