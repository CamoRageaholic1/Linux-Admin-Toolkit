# Quick Start Guide

Get up and running with the Linux Admin Toolkit.

## Installation

```bash
# Clone repository
git clone https://github.com/CamoRageaholic1/Linux-Admin-Toolkit.git
cd Linux-Admin-Toolkit

# Install dependencies
pip install -r requirements.txt

# Or install as package
pip install -e .
```

## Basic Usage

### System Hardening

Harden your system security:

```bash
# Run full hardening (requires root)
sudo linux-harden

# Audit current security
sudo linux-harden --audit

# Dry run to see what would be done
sudo linux-harden --dry-run
```

### User Management

Manage users efficiently:

```bash
# Create new user
sudo linux-users --create john

# Delete user
sudo linux-users --delete john

# Audit all users
sudo linux-users --audit
```

### Log Analysis

Analyze system logs:

```bash
# Find failed login attempts
linux-logs --failed-logins --hours 24

# Analyze errors
linux-logs --errors --log-type syslog --hours 48
```

### Backup Automation

Automate backups:

```bash
# Create backup
sudo linux-backup --backup /home --destination /backup

# List backups
linux-backup --list --destination /backup
```

### Service Monitoring

Monitor services:

```bash
# Monitor specific services
linux-monitor --services nginx,mysql,ssh

# Check system resources
linux-monitor --system

# Monitor critical services
linux-monitor --critical
```

### Performance Tuning

Optimize system performance:

```bash
# Set swappiness
sudo linux-tune --swappiness 10

# Tune network
sudo linux-tune --network

# Clear caches
sudo linux-tune --cache
```

### Security Auditing

Audit security:

```bash
# Full security audit
sudo linux-audit --full

# Find SUID files
sudo linux-audit --suid

# Scan open ports
linux-audit --ports
```

### Package Management

Manage packages:

```bash
# Update system
sudo linux-packages --update

# List installed packages
linux-packages --list
```

### Quick Reference

Access command cheatsheets:

```bash
# Show file commands
linux-ref --category file

# Search for commands
linux-ref --search "network"

# Show all categories
linux-ref --all
```

## Tips

1. **Always use --dry-run first** - Test commands safely
2. **Run as root when needed** - Many commands require sudo
3. **Check --help** - Every command has detailed help
4. **Backup before hardening** - Create system backup first
5. **Test in staging** - Test on non-production systems

## Next Steps

- Read [Security Guide](security.md) for hardening best practices
- Check [Examples](../examples/) for Python integration
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute

## Support

- **Book**: [Linux Basics and Cheat Sheets](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)
- **GitHub Issues**: https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues
