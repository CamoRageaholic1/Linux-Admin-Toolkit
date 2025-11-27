#!/usr/bin/env python3
"""
Package Manager Tool
Automated package management and updates.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import subprocess
import click
from rich.console import Console

console = Console()

class PackageManager:
    """Package management automation."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.detect_package_manager()
    
    def detect_package_manager(self):
        """Detect which package manager is available."""
        if subprocess.run("which apt", shell=True, capture_output=True).returncode == 0:
            self.pm = 'apt'
        elif subprocess.run("which yum", shell=True, capture_output=True).returncode == 0:
            self.pm = 'yum'
        elif subprocess.run("which dnf", shell=True, capture_output=True).returncode == 0:
            self.pm = 'dnf'
        else:
            self.pm = None
    
    def update_system(self):
        """Update system packages."""
        if not self.pm:
            console.print("[red]No supported package manager found[/red]")
            return
        
        console.print(f"\n[cyan]Updating system using {self.pm}...[/cyan]\n")
        
        if self.pm == 'apt':
            commands = [
                "apt update",
                "apt upgrade -y",
                "apt autoremove -y",
            ]
        elif self.pm in ['yum', 'dnf']:
            commands = [
                f"{self.pm} check-update",
                f"{self.pm} update -y",
                f"{self.pm} autoremove -y",
            ]
        
        for cmd in commands:
            if self.dry_run:
                console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
            else:
                console.print(f"Running: {cmd}")
                subprocess.run(cmd, shell=True)
        
        console.print("\n[green]✓ System updated[/green]")
    
    def list_installed(self):
        """List installed packages."""
        if not self.pm:
            console.print("[red]No supported package manager found[/red]")
            return
        
        console.print("\n[cyan]Installed packages:[/cyan]\n")
        
        if self.pm == 'apt':
            cmd = "dpkg -l | tail -n +6"
        elif self.pm in ['yum', 'dnf']:
            cmd = f"{self.pm} list installed"
        
        subprocess.run(cmd, shell=True)

@click.command()
@click.option('--update', is_flag=True, help='Update all packages')
@click.option('--list', 'list_packages', is_flag=True, help='List installed packages')
@click.option('--dry-run', is_flag=True, help='Dry run mode')
def main(update, list_packages, dry_run):
    """Linux Package Manager Tool."""
    manager = PackageManager(dry_run=dry_run)
    
    if update:
        manager.update_system()
    elif list_packages:
        manager.list_installed()
    else:
        console.print("[yellow]Use --update or --list[/yellow]")

if __name__ == '__main__':
    main()
