# Security Guide

Security hardening best practices for Linux systems.

## Overview

This toolkit implements industry-standard security practices based on:

- **CIS Benchmarks** - Center for Internet Security
- **NIST Guidelines** - National Institute of Standards and Technology  
- **Linux Security Modules** - SELinux and AppArmor
- **OWASP** - Open Web Application Security Project

## System Hardening Checklist

### SSH Security

- ☐ Disable root login
- ☐ Use key-based authentication only
- ☐ Change default port (optional)
- ☐ Limit max authentication attempts
- ☐ Set client alive intervals
- ☐ Disable X11 forwarding

```bash
sudo linux-harden --mode ssh
```

### Firewall Configuration

- ☐ Enable firewall (ufw/iptables)
- ☐ Default deny incoming
- ☐ Default allow outgoing
- ☐ Allow only required ports
- ☐ Log dropped packets

```bash
sudo linux-harden --mode firewall
```

### File Permissions

- ☐ Set correct permissions on /etc/passwd (644)
- ☐ Set correct permissions on /etc/shadow (640)
- ☐ Find and fix world-writable files
- ☐ Audit SUID/SGID files

```bash
sudo linux-audit --writable
sudo linux-audit --suid
```

### Kernel Parameters

- ☐ Disable IP forwarding (unless router)
- ☐ Enable SYN cookies
- ☐ Disable ICMP redirects
- ☐ Enable reverse path filtering
- ☐ Log martian packets

```bash
sudo linux-harden
```

## Security Monitoring

### Log Analysis

Regularly check logs for suspicious activity:

```bash
# Failed login attempts
linux-logs --failed-logins --hours 24

# System errors
linux-logs --errors --log-type syslog
```

### Service Monitoring

Monitor critical services:

```bash
# Monitor SSH, firewall, cron
linux-monitor --critical
```

### Security Audits

Run regular security audits:

```bash
# Full audit
sudo linux-audit --full
```

## Incident Response

### If You Detect Intrusion

1. **Isolate** - Disconnect from network
2. **Document** - Save all logs
3. **Analyze** - Review logs for entry point
4. **Remediate** - Patch vulnerabilities
5. **Monitor** - Watch for re-infection

### Recovery Steps

```bash
# 1. Check for unauthorized users
linux-users --audit

# 2. Review failed login attempts
linux-logs --failed-logins --hours 72

# 3. Audit SUID files
sudo linux-audit --suid

# 4. Check open ports
linux-audit --ports

# 5. Re-harden system
sudo linux-harden
```

## Best Practices

### Regular Maintenance

1. **Updates** - Keep system updated
   ```bash
   sudo linux-packages --update
   ```

2. **Backups** - Regular automated backups
   ```bash
   sudo linux-backup --backup /etc --destination /backup
   ```

3. **Audits** - Weekly security audits
   ```bash
   sudo linux-audit --full
   ```

4. **Logs** - Daily log review
   ```bash
   linux-logs --failed-logins --hours 24
   ```

### Defense in Depth

Implement multiple layers of security:

- **Network** - Firewall, IDS/IPS
- **System** - Hardening, updates, monitoring
- **Application** - Secure coding, input validation
- **Data** - Encryption, backups
- **Physical** - Access control

## Compliance

### CIS Benchmarks

This toolkit helps meet CIS Level 1 and Level 2 benchmarks:

- Initial Setup
- Services
- Network Configuration  
- Logging and Auditing
- Access, Authentication and Authorization
- System Maintenance

### NIST Guidelines

Aligns with NIST Cybersecurity Framework:

- **Identify** - Asset management
- **Protect** - Access control, hardening
- **Detect** - Monitoring, logging
- **Respond** - Incident response
- **Recover** - Backups, recovery plans

## Further Reading

- **Author's Book**: [Linux Basics and Cheat Sheets](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)
- **CIS Benchmarks**: https://www.cisecurity.org/cis-benchmarks
- **NIST Cybersecurity Framework**: https://www.nist.gov/cyberframework
- **Linux Security Modules**: https://www.kernel.org/doc/html/latest/admin-guide/LSM/index.html
