# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added

- Professional folder structure reorganization
- Separate `src/`, `docker/`, `scripts/`, `tests/`, `docs/`, `infra/` directories
- HTML templates separated from Python code
- Static files organization (CSS, JS)
- Configuration management with environment variables
- Docker Compose for local development
- Makefile for common commands
- Pytest test suite
- Contributing guidelines
- Comprehensive documentation

### Changed

- Application structure moved from `app/` to `src/`
- Dockerfile moved to `docker/` directory
- Improved CSS with modern dark theme design
- Enhanced README with new project structure

### Removed

- Inline HTML templates from Python code
- Old `app/` directory structure

---

## [1.0.0] - 2024-01-15

### Added

- Initial Flask application
- Docker containerization
- GitHub Actions CI/CD pipeline
- Azure VM deployment
- Health check endpoint
- API info endpoint
- Basic documentation

### Security

- SSH key authentication
- GitHub Secrets for credentials
- Non-root Docker user

---

## Version History

| Version | Date       | Description                 |
| ------- | ---------- | --------------------------- |
| 1.0.0   | 2024-01-15 | Initial release             |
| 2.0.0   | TBD        | Professional reorganization |
