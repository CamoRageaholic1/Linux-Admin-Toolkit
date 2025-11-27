#!/usr/bin/env python3
"""
Quick Reference Tool
Interactive command-line cheat sheets from 'Linux Basics and Cheat Sheets' book.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

CHEAT_SHEETS = {
    'file': [
        ('ls -la', 'List all files with details'),
        ('cp file1 file2', 'Copy file1 to file2'),
        ('mv file1 file2', 'Move/rename file1 to file2'),
        ('rm file', 'Remove file'),
        ('mkdir dir', 'Create directory'),
        ('rmdir dir', 'Remove empty directory'),
        ('find / -name file', 'Find file by name'),
        ('chmod 755 file', 'Change file permissions'),
        ('chown user:group file', 'Change file owner'),
    ],
    'network': [
        ('ip addr show', 'Show IP addresses'),
        ('ping host', 'Ping a host'),
        ('netstat -tuln', 'Show listening ports'),
        ('ss -tuln', 'Show socket statistics'),
        ('curl url', 'Download from URL'),
        ('wget url', 'Download file'),
        ('ssh user@host', 'SSH to remote host'),
        ('scp file user@host:/path', 'Secure copy to remote'),
    ],
    'process': [
        ('ps aux', 'List all processes'),
        ('top', 'Interactive process viewer'),
        ('htop', 'Enhanced process viewer'),
        ('kill PID', 'Kill process by PID'),
        ('killall name', 'Kill processes by name'),
        ('nice -n 10 command', 'Run with lower priority'),
        ('bg', 'Send job to background'),
        ('fg', 'Bring job to foreground'),
    ],
    'system': [
        ('uname -a', 'System information'),
        ('df -h', 'Disk space usage'),
        ('du -sh dir', 'Directory size'),
        ('free -h', 'Memory usage'),
        ('uptime', 'System uptime'),
        ('systemctl status service', 'Service status'),
        ('journalctl -xe', 'System logs'),
        ('dmesg', 'Kernel messages'),
    ],
    'user': [
        ('useradd user', 'Create user'),
        ('userdel user', 'Delete user'),
        ('passwd user', 'Change password'),
        ('su - user', 'Switch user'),
        ('sudo command', 'Run as superuser'),
        ('whoami', 'Current user'),
        ('w', 'Who is logged in'),
        ('last', 'Last logins'),
    ],
}

class QuickRef:
    """Quick reference tool."""
    
    def show_category(self, category: str):
        """Show commands for a category."""
        if category not in CHEAT_SHEETS:
            console.print(f"[red]Category '{category}' not found[/red]")
            console.print(f"Available: {', '.join(CHEAT_SHEETS.keys())}")
            return
        
        table = Table(title=f"{category.title()} Commands")
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")
        
        for cmd, desc in CHEAT_SHEETS[category]:
            table.add_row(cmd, desc)
        
        console.print(table)
    
    def search(self, query: str):
        """Search for commands."""
        results = []
        
        for category, commands in CHEAT_SHEETS.items():
            for cmd, desc in commands:
                if query.lower() in cmd.lower() or query.lower() in desc.lower():
                    results.append((category, cmd, desc))
        
        if not results:
            console.print(f"[yellow]No results found for '{query}'[/yellow]")
            return
        
        table = Table(title=f"Search Results for '{query}'")
        table.add_column("Category", style="yellow")
        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")
        
        for cat, cmd, desc in results:
            table.add_row(cat, cmd, desc)
        
        console.print(table)
    
    def show_all(self):
        """Show all categories."""
        console.print(Panel.fit(
            "[bold cyan]Linux Command Quick Reference[/bold cyan]\n"
            f"From 'Linux Basics and Cheat Sheets' by David Osisek\n\n"
            f"Categories: {', '.join(CHEAT_SHEETS.keys())}",
            border_style="cyan"
        ))

@click.command()
@click.option('--category', type=click.Choice(list(CHEAT_SHEETS.keys())),
              help='Show commands for category')
@click.option('--search', help='Search for commands')
@click.option('--all', 'show_all', is_flag=True, help='Show all categories')
def main(category, search, show_all):
    """Linux Quick Reference Tool - Interactive cheat sheets from the book."""
    ref = QuickRef()
    
    if category:
        ref.show_category(category)
    elif search:
        ref.search(search)
    elif show_all:
        ref.show_all()
    else:
        console.print("[yellow]Use --category, --search, or --all[/yellow]")
        console.print(f"\nAvailable categories: {', '.join(CHEAT_SHEETS.keys())}")

if __name__ == '__main__':
    main()
