#!/usr/bin/env python3
"""
User Management Tool
Bulk user operations and auditing for Linux systems.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import os
import sys
import csv
import subprocess
import click
from rich.console import Console
from rich.table import Table
from typing import List, Dict

console = Console()

class UserManagement:
    """User management automation."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
    
    def create_user(self, username: str, groups: List[str] = None, shell: str = "/bin/bash") -> bool:
        """Create a new user."""
        cmd = f"useradd -m -s {shell} {username}"
        
        if groups:
            cmd += f" -G {','.join(groups)}"
        
        if self.dry_run:
            console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
            return True
        
        result = subprocess.run(cmd, shell=True, capture_output=True)
        return result.returncode == 0
    
    def delete_user(self, username: str, remove_home: bool = True) -> bool:
        """Delete a user."""
        cmd = f"userdel {'-r ' if remove_home else ''}{username}"
        
        if self.dry_run:
            console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
            return True
        
        result = subprocess.run(cmd, shell=True, capture_output=True)
        return result.returncode == 0
    
    def list_users(self) -> List[Dict]:
        """List all users on the system."""
        users = []
        with open('/etc/passwd', 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) >= 7:
                    users.append({
                        'username': parts[0],
                        'uid': parts[2],
                        'gid': parts[3],
                        'home': parts[5],
                        'shell': parts[6]
                    })
        return users
    
    def audit_users(self):
        """Audit user accounts."""
        console.print("\n[cyan]User Account Audit[/cyan]\n")
        
        users = self.list_users()
        
        # Filter to real users (UID >= 1000)
        real_users = [u for u in users if int(u['uid']) >= 1000]
        
        table = Table(title="System Users")
        table.add_column("Username", style="cyan")
        table.add_column("UID", style="green")
        table.add_column("Home", style="yellow")
        table.add_column("Shell", style="blue")
        
        for user in real_users:
            table.add_row(
                user['username'],
                user['uid'],
                user['home'],
                user['shell']
            )
        
        console.print(table)
        console.print(f"\nTotal users: {len(real_users)}")

@click.command()
@click.option('--create', help='Create new user')
@click.option('--delete', help='Delete user')
@click.option('--audit', is_flag=True, help='Audit user accounts')
@click.option('--dry-run', is_flag=True, help='Dry run mode')
def main(create, delete, audit, dry_run):
    """Linux User Management Tool."""
    mgmt = UserManagement(dry_run=dry_run)
    
    if audit:
        mgmt.audit_users()
    elif create:
        success = mgmt.create_user(create)
        console.print(f"[green]User {create} created[/green]" if success else f"[red]Failed to create user[/red]")
    elif delete:
        success = mgmt.delete_user(delete)
        console.print(f"[green]User {delete} deleted[/green]" if success else f"[red]Failed to delete user[/red]")

if __name__ == '__main__':
    main()
