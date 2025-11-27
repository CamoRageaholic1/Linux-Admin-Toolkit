# Linux Admin Toolkit 🐧

[![Author - Published Writer](https://img.shields.io/badge/Author-Published_Writer-blue)](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Bash](https://img.shields.io/badge/bash-5.0+-green.svg)](https://www.gnu.org/software/bash/)

Professional Linux administration toolkit with 9 automation tools for system hardening, monitoring, and management.

**Author:** David Osisek | [Published Book on Amazon](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)

---

## 📚 Learn More About Linux Administration

> **Check out the author's book: ["Linux Basics and Cheat Sheets"](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)** 
> This toolkit was built as a practical companion to the book, providing automated tools that implement the concepts and commands covered in the text.

---

## 🎯 Overview

This toolkit provides 9 professional-grade tools for Linux system administration, covering security hardening, automation, monitoring, and management. Built by an experienced Linux administrator with software development and IT security background.

### ✨ Features

- 🔒 **System Hardening** - Automated security configurations
- 👥 **User Management** - Bulk user operations and auditing
- 📊 **Log Analysis** - Parse and analyze system logs
- 💾 **Backup Automation** - Scheduled backup solutions
- 📡 **Service Monitoring** - Health checks and alerting
- ⚡ **Performance Tuning** - System optimization scripts
- 🔍 **Security Auditing** - Compliance and vulnerability checks
- 📦 **Package Management** - Automated updates and patching
- 📖 **Quick Reference** - CLI cheat sheets from the book

---

## 🛠️ Tools Included

### 1. System Hardening Tool
Automated security hardening:
- SSH configuration hardening
- Firewall setup (iptables/ufw)
- Disable unused services
- File permissions audit
- Password policy enforcement
- SELinux/AppArmor configuration

### 2. User Management Tool
Bulk user operations:
- Create/delete multiple users
- Password management
- Group management
- User audit reports
- Permission analysis
- Home directory management

### 3. Log Analyzer
System log analysis:
- Parse syslog, auth.log, kern.log
- Failed login detection
- Error pattern recognition
- Security event analysis
- Export to JSON/CSV
- Generate reports

### 4. Backup Automation
Automated backup solutions:
- Incremental and full backups
- Compression and encryption
- Remote backup support (rsync, scp)
- Backup verification
- Retention policy management
- Email notifications

### 5. Service Monitor
Service health monitoring:
- Check service status
- Resource usage monitoring
- Automatic restart on failure
- Email/SMS alerts
- Performance metrics
- Uptime tracking

### 6. Performance Tuner
System optimization:
- Memory optimization
- Disk I/O tuning
- Network performance
- CPU governor settings
- Swap configuration
- Cache management

### 7. Security Auditor
Security compliance checks:
- CIS benchmark checks
- Open port scanning
- SUID/SGID file detection
- World-writable file search
- Weak password detection
- Kernel security settings

### 8. Package Manager
Automated package management:
- System updates (apt/yum/dnf)
- Security patches
- Kernel updates
- Package cleanup
- Update scheduling
- Rollback capability

### 9. Quick Reference CLI
Interactive cheat sheets:
- File operations commands
- Network commands
- User management
- Process management
- System information
- Search functionality

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/CamoRageaholic1/Linux-Admin-Toolkit.git
cd Linux-Admin-Toolkit

# Install dependencies
pip install -r requirements.txt

# Or install as package
pip install -e .
```

---

## 🚀 Quick Start

### System Hardening
```bash
# Run security hardening
sudo python -m linux_toolkit.system_hardening --mode interactive

# Audit current security
sudo python -m linux_toolkit.system_hardening --audit
```

### User Management
```bash
# Create multiple users from CSV
sudo python -m linux_toolkit.user_management --create-from-csv users.csv

# Audit user permissions
sudo python -m linux_toolkit.user_management --audit
```

### Log Analysis
```bash
# Analyze auth logs
python -m linux_toolkit.log_analyzer --log-type auth --last 24h

# Find failed login attempts
python -m linux_toolkit.log_analyzer --failed-logins --export report.json
```

### Backup Automation
```bash
# Create backup
sudo python -m linux_toolkit.backup_tool --backup /home --destination /backup

# Schedule automated backups
sudo python -m linux_toolkit.backup_tool --schedule daily --time 02:00
```

### Service Monitoring
```bash
# Monitor services
python -m linux_toolkit.service_monitor --watch nginx mysql ssh

# Check all critical services
python -m linux_toolkit.service_monitor --check-critical
```

### Quick Reference
```bash
# Search cheat sheets
python -m linux_toolkit.quick_ref --search "find files"

# Browse by category
python -m linux_toolkit.quick_ref --category network
```

---

## 📚 Documentation

- **[Quick Start Guide](docs/quick-start.md)** - Get up and running
- **[Security Guide](docs/security.md)** - Hardening best practices
- **[Examples](examples/)** - Python code examples
- **[Contributing](CONTRIBUTING.md)** - Contribution guidelines

---

## 🔒 Security Best Practices

This toolkit implements industry best practices:

- **CIS Benchmarks** - Center for Internet Security standards
- **NIST Guidelines** - National Institute of Standards recommendations
- **Linux Security Modules** - SELinux and AppArmor support
- **Principle of Least Privilege** - Minimal permissions approach

---

## 👨‍💻 About the Author

**David Osisek** is an experienced Linux administrator with extensive background in software development (Bachelor's degree) and IT security (Master's degree). He brings practical field experience in system administration, security, and automation.

### Published Work
**["Linux Basics and Cheat Sheets"](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)** - Available on Amazon

This toolkit serves as a practical companion to the book, providing automated tools that implement the commands and concepts covered in the text.

### Credentials
- **Bachelor's Degree** - Software Development
- **Master's Degree** - IT Security
- **Published Author** - Linux Basics and Cheat Sheets
- **US Army Combat Veteran**

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

All contributions must:
- Follow security best practices
- Include documentation
- Pass code quality checks
- Include examples where appropriate

---

## 📖 Recommended Reading

1. **["Linux Basics and Cheat Sheets" by David Osisek](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)** - The companion book to this toolkit
2. **The Linux Command Line** by William Shotts
3. **Linux Bible** by Christopher Negus
4. **UNIX and Linux System Administration Handbook**

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🔗 Links

- **GitHub Repository**: https://github.com/CamoRageaholic1/Linux-Admin-Toolkit
- **Author's Book**: https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/
- **Issues**: https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues

---

## 💡 Use Cases

- **System Administration** - Daily admin tasks automation
- **Security Hardening** - Implement security best practices
- **Compliance** - Meet CIS/NIST requirements
- **DevOps** - Infrastructure automation
- **Learning** - Understand Linux administration
- **Disaster Recovery** - Automated backup solutions

---

**Built by a published author with software development and IT security expertise** 🐧
