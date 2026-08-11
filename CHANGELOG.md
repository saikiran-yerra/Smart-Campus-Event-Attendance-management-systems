# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Features currently under development will be documented here

### Changed
- Ongoing improvements to existing features

### Fixed
- Bug fixes for unreleased features

### Deprecated
- Features planned for removal in a future release

### Removed
- Removed features from previous releases

### Security
- Security vulnerability fixes

---

## [0.1.0] - 2026-08-04

### Added
- **Backend:** Flask REST API with modular blueprint architecture
  - User authentication and authorization endpoints (`auth_api.py`)
  - Event management endpoints (`events_api.py`)
  - Attendance tracking endpoints (`attendance_api.py`)
  - Notification service endpoints (`notification_api.py`)
  - Recommendation engine endpoints (`recommendation_api.py`)
- **Database:** MySQL schema for users, events, attendance records, and notifications
- **Frontend:** Static HTML/CSS/JavaScript dashboard with login, event listing, and attendance tracking
- **AI Recommendation Engine:** Scikit-learn model for personalized event recommendations
- **Unit tests:** Comprehensive test suite covering authentication, events, attendance, notifications, and recommendations
- **Configuration:** Modular config system for development, production, and security settings
- **Documentation:** Initial project documentation and API references

### Technical Details
- Backend framework: Flask 3.0.0
- Database: MySQL with Python connector
- ML framework: Scikit-learn for recommendation engine
- Testing: Python unittest framework
- CI: GitHub Actions workflow for automated testing on push and pull request

---

## Versioning Convention

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backward-compatible feature additions
- **PATCH** version for backward-compatible bug fixes

Tags are created in the format: `vMAJOR.MINOR.PATCH` (e.g., `v0.1.0`, `v0.2.0`, `v1.0.0`)

When releasing a new version:
1. Update this CHANGELOG.md with an entry for the new version
2. Create an annotated git tag: `git tag -a vX.Y.Z -m "Release message"`
3. Push the tag to the repository: `git push origin vX.Y.Z`

---

## Releases

Official releases follow the versioning convention and are marked with Git tags.

**Current Release:** [v0.1.0](https://github.com/saikiran-yerra/Smart-Campus-Event-Attendance-management-systems/releases/tag/v0.1.0)

All released versions are listed on the [Releases page](https://github.com/saikiran-yerra/Smart-Campus-Event-Attendance-management-systems/releases) with release notes and downloadable artifacts.

To reference a specific release, use the tag name in the format: `vMAJOR.MINOR.PATCH`
Example: `git checkout v0.1.0`
