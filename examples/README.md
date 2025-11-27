# Examples

Python code examples demonstrating programmatic usage of the Linux Admin Toolkit.

## Overview

All tools can be used programmatically from Python code, not just from the command line.

## Example Files

- **example_system_hardening.py** - System security hardening
- **example_monitoring.py** - Service monitoring and alerts
- **example_automation.py** - Automated maintenance tasks

## Quick Start

### Import Tools

```python
from linux_toolkit import (
    SystemHardening,
    UserManagement,
    LogAnalyzer,
    BackupTool,
    ServiceMonitor,
    PerformanceTuner,
    SecurityAuditor,
    PackageManager,
    QuickRef
)
```

### System Hardening

```python
# Create hardening instance
hardening = SystemHardening(dry_run=False)

# Run specific hardening tasks
hardening.harden_ssh()
hardening.configure_firewall()
hardening.set_file_permissions()

# Or run full hardening
results = hardening.run_full_hardening()
print(results)
```

### User Management

```python
# Create user management instance
mgmt = UserManagement(dry_run=False)

# Create user
success = mgmt.create_user('john', groups=['sudo', 'docker'])

# List all users
users = mgmt.list_users()
for user in users:
    print(f"{user['username']}: {user['home']}")
```

### Log Analysis

```python
# Create log analyzer
analyzer = LogAnalyzer()

# Parse auth logs
entries = analyzer.parse_log_file('auth', hours=24)

# Find failed logins
analyzer.find_failed_logins(hours=24)
```

### Backup Automation

```python
# Create backup tool
backup = BackupTool(dry_run=False)

# Create compressed backup
backup.create_backup(
    source='/home',
    destination='/backup',
    compress=True
)

# List backups
backup.list_backups('/backup')
```

### Service Monitoring

```python
# Create service monitor
monitor = ServiceMonitor()

# Check services
services = ['nginx', 'mysql', 'ssh']
monitor.monitor_services(services)

# Check system resources
monitor.system_resources()
```

### Security Auditing

```python
# Create security auditor
auditor = SecurityAuditor()

# Run full audit
auditor.full_audit()

# Or specific checks
auditor.find_suid_files()
auditor.scan_open_ports()
auditor.check_world_writable()
```

## Integration Examples

### Automated Nightly Maintenance

```python
import schedule
import time
from linux_toolkit import BackupTool, PackageManager, SecurityAuditor

def nightly_maintenance():
    # Backup critical directories
    backup = BackupTool()
    backup.create_backup('/etc', '/backup', compress=True)
    
    # Update packages
    packages = PackageManager()
    packages.update_system()
    
    # Security audit
    auditor = SecurityAuditor()
    auditor.full_audit()

# Schedule for 2 AM daily
schedule.every().day.at("02:00").do(nightly_maintenance)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Monitoring Dashboard

```python
from linux_toolkit import ServiceMonitor, LogAnalyzer
import time

def monitoring_loop():
    monitor = ServiceMonitor()
    analyzer = LogAnalyzer()
    
    while True:
        # Check services
        monitor.monitor_services(['nginx', 'mysql'])
        
        # Check logs
        analyzer.find_failed_logins(hours=1)
        
        # Wait 5 minutes
        time.sleep(300)

monitoring_loop()
```

## Resources

- **Main Documentation**: [../docs/](../docs/)
- **Author's Book**: [Linux Basics and Cheat Sheets](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)
- **GitHub Repository**: https://github.com/CamoRageaholic1/Linux-Admin-Toolkit
