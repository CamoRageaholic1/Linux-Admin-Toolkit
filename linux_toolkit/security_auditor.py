#!/usr/bin/env python3
"""
Security Auditor Tool
Security compliance checks and vulnerability scanning.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import os
import subprocess
import click
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

class SecurityAuditor:
    """Security auditing tool."""
    
    def find_suid_files(self):
        """Find SUID/SGID files."""
        console.print("\n[cyan]Scanning for SUID/SGID files...[/cyan]\n")
        
        result = subprocess.run(
            "find / -type f \\( -perm -4000 -o -perm -2000 \\) 2>/dev/null",
            shell=True,
            capture_output=True,
            text=True
        )
        
        files = result.stdout.strip().split('\n')
        files = [f for f in files if f]  # Remove empty strings
        
        console.print(f"Found {len(files)} SUID/SGID files:")
        for f in files[:20]:  # Show first 20
            console.print(f"  {f}")
        
        if len(files) > 20:
            console.print(f"  ... and {len(files) - 20} more")
    
    def scan_open_ports(self):
        """Scan for open ports."""
        console.print("\n[cyan]Scanning open ports...[/cyan]\n")
        
        result = subprocess.run(
            "ss -tuln | grep LISTEN",
            shell=True,
            capture_output=True,
            text=True
        )
        
        console.print("Listening ports:")
        console.print(result.stdout)
    
    def check_world_writable(self):
        """Find world-writable files."""
        console.print("\n[cyan]Scanning for world-writable files in /etc...[/cyan]\n")
        
        result = subprocess.run(
            "find /etc -type f -perm -002 2>/dev/null",
            shell=True,
            capture_output=True,
            text=True
        )
        
        files = result.stdout.strip().split('\n')
        files = [f for f in files if f]
        
        if files:
            console.print(f"[red]Found {len(files)} world-writable files:[/red]")
            for f in files:
                console.print(f"  {f}")
        else:
            console.print("[green]✓ No world-writable files found[/green]")
    
    def full_audit(self):
        """Run complete security audit."""
        console.print("\n[bold cyan]Security Audit Report[/bold cyan]\n")
        
        self.find_suid_files()
        self.scan_open_ports()
        self.check_world_writable()
        
        console.print("\n[green]✓ Audit complete[/green]")

@click.command()
@click.option('--suid', is_flag=True, help='Find SUID/SGID files')
@click.option('--ports', is_flag=True, help='Scan open ports')
@click.option('--writable', is_flag=True, help='Find world-writable files')
@click.option('--full', is_flag=True, help='Run full security audit')
def main(suid, ports, writable, full):
    """Linux Security Auditor Tool."""
    auditor = SecurityAuditor()
    
    if full:
        auditor.full_audit()
    elif suid:
        auditor.find_suid_files()
    elif ports:
        auditor.scan_open_ports()
    elif writable:
        auditor.check_world_writable()
    else:
        console.print("[yellow]Use --suid, --ports, --writable, or --full[/yellow]")

if __name__ == '__main__':
    main()
