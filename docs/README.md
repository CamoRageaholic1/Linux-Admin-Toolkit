# Documentation

Comprehensive documentation for the Linux Admin Toolkit.

## 📄 Available Documentation

### [Quick Start Guide](quick-start.md)
Get up and running quickly:
- Installation instructions
- Basic usage examples for all 9 tools
- Common workflows
- Tips and best practices

**Start here if you're new to the toolkit!**

### [Security Guide](security.md)
Security hardening best practices:
- CIS Benchmarks compliance
- System hardening checklist
- Security monitoring procedures
- Incident response guidelines
- Compliance frameworks (CIS, NIST)

**Essential for production deployments!**

## 🎯 Quick Reference

### Common Commands

```bash
# System Hardening
sudo linux-harden --audit

# User Management
sudo linux-users --audit

# Log Analysis
linux-logs --failed-logins --hours 24

# Backups
sudo linux-backup --backup /home --destination /backup

# Monitoring
linux-monitor --system

# Security Audit
sudo linux-audit --full
```

### Tool Categories

| Category | Tools |
|----------|-------|
| Security | system_hardening, security_auditor |
| Management | user_management, package_manager |
| Monitoring | log_analyzer, service_monitor |
| Maintenance | backup_tool, performance_tuner |
| Reference | quick_ref |

## 📚 Additional Resources

### Example Code
See [../examples/](../examples/) for Python code examples demonstrating:
- Programmatic tool usage
- System hardening automation
- Monitoring and alerting
- Integration examples

### Contributing
See [../CONTRIBUTING.md](../CONTRIBUTING.md) for:
- Code contribution guidelines
- Security requirements
- Documentation standards

### Author's Book
**["Linux Basics and Cheat Sheets"](https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/)** by David Osisek

This toolkit is a practical companion to the book, implementing commands and concepts with automated tools.

## 🔗 External Resources

- **CIS Benchmarks:** https://www.cisecurity.org/cis-benchmarks
- **NIST Cybersecurity Framework:** https://www.nist.gov/cyberframework
- **Linux Security Modules:** https://www.kernel.org/doc/html/latest/admin-guide/LSM/

## 💡 Need Help?

1. Check the [Quick Start Guide](quick-start.md)
2. Review [Security Guide](security.md)
3. Look at [Examples](../examples/)
4. Open a [GitHub Issue](https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues)

---

**Comprehensive Linux administration toolkit by published author** 🐧
