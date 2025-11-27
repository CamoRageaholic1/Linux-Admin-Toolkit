# Linux Toolkit - Core Tools

This directory contains 9 professional Linux administration tools for system management, security, and automation.

## 🛠️ Tools

### 1. System Hardening (`system_hardening.py`)
Automated security hardening:
- SSH configuration hardening (disable root, key-only auth)
- Firewall setup (ufw/iptables)
- Disable unused services
- File permissions audit
- Kernel security parameters

**CLI:** `linux-harden`

### 2. User Management (`user_management.py`)
Bulk user operations:
- Create/delete users
- User auditing and reporting
- Permission analysis
- Group management

**CLI:** `linux-users`

### 3. Log Analyzer (`log_analyzer.py`)
System log analysis:
- Parse auth.log, syslog, kern.log
- Failed login detection
- Error pattern recognition
- Security event analysis

**CLI:** `linux-logs`

### 4. Backup Tool (`backup_tool.py`)
Automated backup solutions:
- Compressed backups (tar.gz)
- Backup listing and management
- Destination management
- Progress tracking

**CLI:** `linux-backup`

### 5. Service Monitor (`service_monitor.py`)
Service health monitoring:
- Check service status
- Resource usage monitoring (CPU, memory, disk)
- Load average tracking
- Critical service monitoring

**CLI:** `linux-monitor`

### 6. Performance Tuner (`performance_tuner.py`)
System optimization:
- Swappiness optimization
- Network performance tuning
- Cache management
- Memory optimization

**CLI:** `linux-tune`

### 7. Security Auditor (`security_auditor.py`)
Security compliance checks:
- SUID/SGID file detection
- Open port scanning
- World-writable file search
- Full security audit reporting

**CLI:** `linux-audit`

### 8. Package Manager (`package_manager.py`)
Automated package management:
- System updates (apt/yum/dnf)
- Package listing
- Auto-detection of package manager
- Cleanup and maintenance

**CLI:** `linux-packages`

### 9. Quick Reference (`quick_ref.py`)
Interactive command cheatsheets:
- File operations commands
- Network commands
- Process management
- System information
- User management
- Search functionality

**CLI:** `linux-ref`

## 🚀 Usage

All tools can be used via command-line:

```bash
# System hardening
sudo linux-harden

# User management
sudo linux-users --audit

# Log analysis
linux-logs --failed-logins --hours 24

# Backup
sudo linux-backup --backup /home --destination /backup

# Service monitoring
linux-monitor --system

# Performance tuning
sudo linux-tune --swappiness 10

# Security audit
sudo linux-audit --full

# Package management
sudo linux-packages --update

# Quick reference
linux-ref --category network
```

Or import as Python modules:

```python
from linux_toolkit.system_hardening import SystemHardening
from linux_toolkit.log_analyzer import LogAnalyzer
from linux_toolkit.service_monitor import ServiceMonitor

# Use in your code
hardening = SystemHardening(dry_run=False)
results = hardening.run_full_hardening()
```

## 🔒 Security Best Practices

- **CIS Benchmarks** - Center for Internet Security standards
- **NIST Guidelines** - National Institute of Standards
- **Principle of Least Privilege** - Minimal permissions
- **Defense in Depth** - Multiple security layers

## 📖 Documentation

See the [main README](../README.md) and [docs/](../docs/) folder for comprehensive documentation.

---

**Built by David Osisek**  
**Author of ["Linux Basics and Cheat Sheets"](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)**
