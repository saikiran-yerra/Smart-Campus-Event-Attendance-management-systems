# Contributing to Smart Campus Event & Attendance Management System

Thank you for your interest in contributing to this project! This document outlines the guidelines and workflow for contributing.

---

## Branch Naming Convention

Please use the following branch naming conventions when creating new branches:

- **Feature branches:** `feature/<name>` (e.g., `feature/event-notifications`)
- **Bug fixes:** `fix/<name>` (e.g., `fix/attendance-validation`)
- **Documentation:** `docs/<name>` (e.g., `docs/api-endpoints`)

---

## Commit Message Format

Write clear, descriptive commit messages in the imperative mood (e.g., "Add feature" not "Added feature").

### Format:
- **Short subject line** (50 characters or less)
- **Optional body** (wrapped at 72 characters, separated from subject by a blank line)

### Examples:
- `fix: resolve attendance marking conflict`
- `feat: add email notification service`
- `docs: update architecture documentation`

---

## Running Tests Locally

Before opening a pull request, ensure all tests pass locally:

```bash
# Install dependencies
pip install -r backend/requirements.txt
pip install -r ai_recommendation/requirements.txt

# Run all unit tests
python -m unittest discover -s test -p "test_*.py"
```

If any test fails, fix the issues before submitting your PR.

---

## Pull Request Guidelines

When opening a pull request:

1. **Ensure CI passes:** The GitHub Actions workflow must pass (all unit tests must succeed on Python 3.10 and 3.11).

2. **Request review:** Request at least one approval from a project maintainer before merging.

3. **Link related issues:** If your PR addresses an issue, reference it in the PR description (e.g., "Closes #42").

4. **Update documentation:** If you modify APIs, configuration, or features, update the relevant documentation in `docs/` and `README.md`.

5. **Use the PR template:** Fill out the pull request template completely with:
   - Description of changes
   - Type of change (bug fix, feature, documentation)
   - Testing performed
   - Checklist confirmation

---

## Code Review Expectations

- Reviews should be constructive and focused on code quality, maintainability, and correctness.
- Authors should be responsive to feedback and willing to make requested changes.
- Discussions should remain professional and collaborative.

Thank you for contributing!
