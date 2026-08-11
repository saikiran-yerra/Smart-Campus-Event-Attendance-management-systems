# Security Policy

## Supported Versions

This project follows [Semantic Versioning](https://semver.org/).

| Version | Status | Supported |
|---------|--------|-----------|
| 0.1.x   | Initial Release | ✅ Yes |

## Reporting Security Vulnerabilities

**Do not open a public issue for security vulnerabilities.**

If you discover a security vulnerability, please report it **privately** using GitHub's Security Advisory feature:

1. Navigate to the repository's "Security" tab
2. Click "Report a vulnerability"
3. Provide a detailed description of the vulnerability, affected components, and reproduction steps
4. Submit the report

### What to include in your report:
- Description of the vulnerability
- Affected component(s) (backend, frontend, AI recommendation, database, etc.)
- Steps to reproduce
- Potential impact
- Suggested fix (if known)

### Expected Response Timeline:
- **Initial response:** Within 48 hours
- **Assessment and patch plan:** Within 5 business days
- **Security patch release:** Within 10 business days (or as soon as possible for critical vulnerabilities)

## Security Best Practices

### Secret Management

**Never commit secrets or credentials to the repository.**

#### Rules:
- Database credentials (host, user, password, database name) must **never** be committed
- Flask secret keys must **never** be hardcoded in the application
- API keys and authentication tokens must **never** be in source code

#### Proper approach:
1. Use environment variables for all sensitive configuration
2. Create a `.env` file locally with your configuration (this file is excluded via `.gitignore`)
3. Load environment variables in your application using a tool like `python-dotenv`
4. Reference the `.env.example` file for required variables

#### Example:
```python
import os
from dotenv import load_dotenv

load_dotenv()

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
```

### Code Review
All code changes must be reviewed before merging to the main branch. See [CONTRIBUTING.md](CONTRIBUTING.md) for pull request guidelines.

### Dependency Updates
Keep dependencies up-to-date to minimize exposure to known vulnerabilities. Regularly review:
- `backend/requirements.txt`
- `ai_recommendation/requirements.txt`
- `requirements-lock.txt` (regenerate after updating dependencies)

### Testing
Run the full test suite before committing: `python -m unittest discover -s test -p "test_*.py"`

---

Thank you for helping us keep this project secure!
