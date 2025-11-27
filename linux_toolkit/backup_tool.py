#!/usr/bin/env python3
"""
Backup Automation Tool
Automated backup solutions with compression and encryption.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import os
import subprocess
import click
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.progress import Progress

console = Console()

class BackupTool:
    """Automated backup tool."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
    
    def create_backup(self, source: str, destination: str, compress: bool = True):
        """Create backup of source directory."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"backup_{timestamp}.tar.gz" if compress else f"backup_{timestamp}"
        backup_path = Path(destination) / backup_name
        
        console.print(f"\n[cyan]Creating backup...[/cyan]")
        console.print(f"Source: {source}")
        console.print(f"Destination: {backup_path}\n")
        
        if compress:
            cmd = f"tar -czf {backup_path} {source}"
        else:
            cmd = f"cp -r {source} {backup_path}"
        
        if self.dry_run:
            console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
            return
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Backing up...", total=100)
            
            result = subprocess.run(cmd, shell=True, capture_output=True)
            progress.update(task, completed=100)
            
            if result.returncode == 0:
                # Get backup size
                size = backup_path.stat().st_size if backup_path.exists() else 0
                size_mb = size / (1024 * 1024)
                
                console.print(f"\n[green]✓ Backup completed successfully![/green]")
                console.print(f"Backup size: {size_mb:.2f} MB")
                console.print(f"Location: {backup_path}")
            else:
                console.print(f"[red]✗ Backup failed: {result.stderr.decode()}[/red]")
    
    def list_backups(self, destination: str):
        """List available backups."""
        backup_dir = Path(destination)
        
        if not backup_dir.exists():
            console.print(f"[red]Backup directory not found: {destination}[/red]")
            return
        
        backups = list(backup_dir.glob('backup_*'))
        
        if not backups:
            console.print("[yellow]No backups found[/yellow]")
            return
        
        console.print(f"\n[cyan]Available backups in {destination}:[/cyan]\n")
        
        for backup in sorted(backups, reverse=True):
            size = backup.stat().st_size / (1024 * 1024)
            mtime = datetime.fromtimestamp(backup.stat().st_mtime)
            console.print(f"  {backup.name} - {size:.2f} MB - {mtime.strftime('%Y-%m-%d %H:%M:%S')}")

@click.command()
@click.option('--backup', help='Create backup of directory')
@click.option('--destination', default='/backup', help='Backup destination')
@click.option('--list', 'list_backups_flag', is_flag=True, help='List available backups')
@click.option('--compress/--no-compress', default=True, help='Compress backup')
@click.option('--dry-run', is_flag=True, help='Dry run mode')
def main(backup, destination, list_backups_flag, compress, dry_run):
    """Linux Backup Automation Tool."""
    tool = BackupTool(dry_run=dry_run)
    
    if list_backups_flag:
        tool.list_backups(destination)
    elif backup:
        tool.create_backup(backup, destination, compress)
    else:
        console.print("[yellow]Use --backup to create a backup or --list to view backups[/yellow]")

if __name__ == '__main__':
    main()
