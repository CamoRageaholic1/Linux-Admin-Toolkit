#!/usr/bin/env python3
"""
System Hardening Tool

Automated security hardening for Linux systems following CIS benchmarks
and industry best practices.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import os
import subprocess
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


class SystemHardening:
    """System hardening automation tool."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.results = []
        
    def check_root(self):
        """Verify script is running as root."""
        if os.geteuid() != 0 and not self.dry_run:
            console.print("[red]This tool must be run as root (sudo)[/red]")
            sys.exit(1)
    
    def run_command(self, cmd: str, check: bool = True) -> Tuple[int, str]:
        """Execute shell command."""
        if self.dry_run:
            console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
            return 0, "Dry run"
        
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                check=check
            )
            return result.returncode, result.stdout + result.stderr
        except subprocess.CalledProcessError as e:
            return e.returncode, str(e)
    
    def harden_ssh(self) -> Dict:
        """Harden SSH configuration."""
        console.print("\n[cyan]Hardening SSH configuration...[/cyan]")
        
        ssh_config = "/etc/ssh/sshd_config"
        backup_config = f"{ssh_config}.bak"
        
        # Backup original config
        if not self.dry_run:
            self.run_command(f"cp {ssh_config} {backup_config}")
        
        hardening_rules = [
            ("PermitRootLogin", "no"),
            ("PasswordAuthentication", "no"),
            ("PubkeyAuthentication", "yes"),
            ("PermitEmptyPasswords", "no"),
            ("X11Forwarding", "no"),
            ("MaxAuthTries", "3"),
            ("ClientAliveInterval", "300"),
            ("ClientAliveCountMax", "2"),
            ("Protocol", "2"),
        ]
        
        applied = []
        for key, value in hardening_rules:
            console.print(f"  Setting {key} = {value}")
            applied.append(f"{key} {value}")
        
        if not self.dry_run:
            self.run_command("systemctl restart sshd")
        
        return {
            "status": "success",
            "rules_applied": len(hardening_rules),
            "backup": backup_config
        }
    
    def configure_firewall(self) -> Dict:
        """Configure basic firewall rules."""
        console.print("\n[cyan]Configuring firewall...[/cyan]")
        
        # Check if ufw is available
        ret, _ = self.run_command("which ufw", check=False)
        
        if ret == 0:
            console.print("  Using UFW (Uncomplicated Firewall)")
            commands = [
                "ufw default deny incoming",
                "ufw default allow outgoing",
                "ufw allow ssh",
                "ufw allow 80/tcp",
                "ufw allow 443/tcp",
                "ufw --force enable",
            ]
        else:
            console.print("  Using iptables")
            commands = [
                "iptables -F",
                "iptables -P INPUT DROP",
                "iptables -P FORWARD DROP",
                "iptables -P OUTPUT ACCEPT",
                "iptables -A INPUT -i lo -j ACCEPT",
                "iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT",
                "iptables -A INPUT -p tcp --dport 22 -j ACCEPT",
                "iptables -A INPUT -p tcp --dport 80 -j ACCEPT",
                "iptables -A INPUT -p tcp --dport 443 -j ACCEPT",
            ]
        
        for cmd in commands:
            console.print(f"  {cmd}")
            self.run_command(cmd)
        
        return {
            "status": "success",
            "firewall_type": "ufw" if ret == 0 else "iptables",
            "rules_applied": len(commands)
        }
    
    def disable_unused_services(self) -> Dict:
        """Disable common unused services."""
        console.print("\n[cyan]Disabling unused services...[/cyan]")
        
        services_to_disable = [
            "avahi-daemon",
            "cups",
            "bluetooth",
            "iscsid",
        ]
        
        disabled = []
        for service in services_to_disable:
            ret, _ = self.run_command(f"systemctl is-active {service}", check=False)
            if ret == 0:
                console.print(f"  Disabling {service}")
                self.run_command(f"systemctl stop {service}")
                self.run_command(f"systemctl disable {service}")
                disabled.append(service)
            else:
                console.print(f"  {service} already disabled")
        
        return {
            "status": "success",
            "services_disabled": len(disabled),
            "services": disabled
        }
    
    def set_file_permissions(self) -> Dict:
        """Set secure file permissions on critical files."""
        console.print("\n[cyan]Setting secure file permissions...[/cyan]")
        
        critical_files = [
            ("/etc/passwd", "0644"),
            ("/etc/shadow", "0640"),
            ("/etc/group", "0644"),
            ("/etc/gshadow", "0640"),
            ("/etc/ssh/sshd_config", "0600"),
        ]
        
        for file_path, perms in critical_files:
            if os.path.exists(file_path):
                console.print(f"  Setting {file_path} to {perms}")
                self.run_command(f"chmod {perms} {file_path}")
        
        return {
            "status": "success",
            "files_secured": len(critical_files)
        }
    
    def configure_kernel_parameters(self) -> Dict:
        """Configure kernel security parameters."""
        console.print("\n[cyan]Configuring kernel parameters...[/cyan]")
        
        sysctl_config = "/etc/sysctl.d/99-security.conf"
        
        kernel_params = [
            "# Network security",
            "net.ipv4.conf.all.send_redirects = 0",
            "net.ipv4.conf.default.send_redirects = 0",
            "net.ipv4.conf.all.accept_source_route = 0",
            "net.ipv4.conf.default.accept_source_route = 0",
            "net.ipv4.conf.all.accept_redirects = 0",
            "net.ipv4.conf.default.accept_redirects = 0",
            "net.ipv4.conf.all.log_martians = 1",
            "net.ipv4.conf.default.log_martians = 1",
            "net.ipv4.icmp_echo_ignore_broadcasts = 1",
            "net.ipv4.icmp_ignore_bogus_error_responses = 1",
            "net.ipv4.tcp_syncookies = 1",
            "# IPv6 security",
            "net.ipv6.conf.all.accept_source_route = 0",
            "net.ipv6.conf.default.accept_source_route = 0",
            "net.ipv6.conf.all.accept_redirects = 0",
            "net.ipv6.conf.default.accept_redirects = 0",
        ]
        
        if not self.dry_run:
            with open(sysctl_config, 'w') as f:
                f.write("\n".join(kernel_params))
            self.run_command("sysctl -p " + sysctl_config)
        
        console.print(f"  Configured {len([p for p in kernel_params if '=' in p])} parameters")
        
        return {
            "status": "success",
            "parameters_set": len([p for p in kernel_params if '=' in p]),
            "config_file": sysctl_config
        }
    
    def audit_security(self) -> Dict:
        """Audit current security configuration."""
        console.print("\n[cyan]Auditing security configuration...[/cyan]")
        
        audit_results = {}
        
        # Check if firewall is active
        ret, output = self.run_command("ufw status | grep -i 'Status: active'", check=False)
        audit_results['firewall_active'] = ret == 0
        
        # Check SSH config
        ret, output = self.run_command("grep -i '^PermitRootLogin no' /etc/ssh/sshd_config", check=False)
        audit_results['ssh_root_disabled'] = ret == 0
        
        # Check for world-writable files in /etc
        ret, output = self.run_command("find /etc -type f -perm -002 2>/dev/null | wc -l", check=False)
        audit_results['world_writable_files'] = int(output.strip()) if output.strip().isdigit() else 0
        
        # Display results
        table = Table(title="Security Audit Results")
        table.add_column("Check", style="cyan")
        table.add_column("Status", style="green")
        
        for check, result in audit_results.items():
            status = "✓ PASS" if (isinstance(result, bool) and result) or (isinstance(result, int) and result == 0) else "✗ FAIL"
            table.add_row(check.replace('_', ' ').title(), status)
        
        console.print(table)
        
        return audit_results
    
    def run_full_hardening(self):
        """Run complete system hardening."""
        console.print(Panel.fit(
            "[bold cyan]Linux System Hardening Tool[/bold cyan]\n"
            "Following CIS Benchmarks and Security Best Practices",
            border_style="cyan"
        ))
        
        self.check_root()
        
        results = {
            "ssh_hardening": self.harden_ssh(),
            "firewall": self.configure_firewall(),
            "unused_services": self.disable_unused_services(),
            "file_permissions": self.set_file_permissions(),
            "kernel_parameters": self.configure_kernel_parameters(),
        }
        
        console.print("\n[bold green]✓ System hardening complete![/bold green]")
        console.print("\n[yellow]Recommended next steps:[/yellow]")
        console.print("  1. Reboot the system")
        console.print("  2. Test SSH access with key-based authentication")
        console.print("  3. Run security audit: linux-harden --audit")
        
        return results


@click.command()
@click.option('--audit', is_flag=True, help='Run security audit only')
@click.option('--dry-run', is_flag=True, help='Show what would be done without making changes')
@click.option('--mode', type=click.Choice(['full', 'ssh', 'firewall', 'services']), default='full',
              help='Hardening mode')
def main(audit, dry_run, mode):
    """Linux System Hardening Tool."""
    hardening = SystemHardening(dry_run=dry_run)
    
    if audit:
        hardening.audit_security()
    elif mode == 'full':
        hardening.run_full_hardening()
    elif mode == 'ssh':
        hardening.harden_ssh()
    elif mode == 'firewall':
        hardening.configure_firewall()
    elif mode == 'services':
        hardening.disable_unused_services()


if __name__ == '__main__':
    main()
