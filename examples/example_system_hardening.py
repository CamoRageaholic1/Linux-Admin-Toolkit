#!/usr/bin/env python3
"""
Example: System Security Hardening

Demonstrates programmatic usage of the SystemHardening tool.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

from linux_toolkit import SystemHardening

def example_basic_hardening():
    """Example 1: Basic system hardening."""
    print("\n=== Example 1: Basic System Hardening ===")
    
    # Create hardening instance with dry_run=True for safe testing
    hardening = SystemHardening(dry_run=True)
    
    # Run individual hardening tasks
    ssh_result = hardening.harden_ssh()
    print(f"SSH Hardening: {ssh_result['status']}")
    
    firewall_result = hardening.configure_firewall()
    print(f"Firewall: {firewall_result['status']}")
    
    services_result = hardening.disable_unused_services()
    print(f"Services disabled: {services_result['services_disabled']}")

def example_full_hardening():
    """Example 2: Complete system hardening."""
    print("\n=== Example 2: Complete System Hardening ===")
    
    # For actual hardening, set dry_run=False and run with sudo
    hardening = SystemHardening(dry_run=True)
    
    # Run full hardening suite
    results = hardening.run_full_hardening()
    
    # Display results
    print("\nHardening Results:")
    for task, result in results.items():
        print(f"  {task}: {result['status']}")

def example_security_audit():
    """Example 3: Security audit only."""
    print("\n=== Example 3: Security Audit ===")
    
    hardening = SystemHardening(dry_run=False)
    
    # Run security audit (doesn't modify system)
    audit_results = hardening.audit_security()
    
    # Process audit results
    print("\nAudit Summary:")
    print(f"  Firewall Active: {audit_results['firewall_active']}")
    print(f"  SSH Root Disabled: {audit_results['ssh_root_disabled']}")
    print(f"  World-writable Files: {audit_results['world_writable_files']}")
    
    # Alert if issues found
    if not audit_results['firewall_active']:
        print("\n[!] WARNING: Firewall is not active!")
    
    if audit_results['world_writable_files'] > 0:
        print(f"\n[!] WARNING: Found {audit_results['world_writable_files']} world-writable files!")

if __name__ == '__main__':
    print("Linux Admin Toolkit - System Hardening Examples")
    print("Author: David Osisek")
    print("Book: Linux Basics and Cheat Sheets")
    print("="*50)
    
    # Run examples
    example_basic_hardening()
    example_full_hardening()
    example_security_audit()
    
    print("\n" + "="*50)
    print("Examples completed!")
    print("\nTo run actual hardening (not dry-run), use:")
    print("  sudo python -m linux_toolkit.system_hardening")
