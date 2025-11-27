#!/usr/bin/env python3
"""
Linux Admin Toolkit - Main CLI Entry Point

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Linux Admin Toolkit - Professional system administration tools."""
    pass

@cli.command()
def tools():
    """List all available tools."""
    console.print(Panel.fit(
        "[bold cyan]Linux Admin Toolkit[/bold cyan]\n"
        "Professional system administration tools\n\n"
        "Author: David Osisek\n"
        "Book: Linux Basics and Cheat Sheets (Amazon)",
        border_style="cyan"
    ))
    
    table = Table(title="\nAvailable Tools")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="green")
    
    tools_list = [
        ('linux-harden', 'System security hardening'),
        ('linux-users', 'User management'),
        ('linux-logs', 'Log analysis'),
        ('linux-backup', 'Backup automation'),
        ('linux-monitor', 'Service monitoring'),
        ('linux-tune', 'Performance tuning'),
        ('linux-audit', 'Security auditing'),
        ('linux-packages', 'Package management'),
        ('linux-ref', 'Quick reference'),
    ]
    
    for cmd, desc in tools_list:
        table.add_row(cmd, desc)
    
    console.print(table)
    console.print("\n[yellow]Run any command with --help for usage details[/yellow]")

@cli.command()
def about():
    """About this toolkit and the author."""
    console.print(Panel.fit(
        "[bold cyan]Linux Admin Toolkit v1.0.0[/bold cyan]\n\n"
        "[green]Professional Linux administration tools with automation and monitoring.[/green]\n\n"
        "[bold]Author:[/bold] David Osisek\n"
        "  • Bachelor's Degree - Software Development\n"
        "  • Master's Degree - IT Security\n"
        "  • Published Author - Linux Basics and Cheat Sheets\n"
        "  • US Army Combat Veteran\n\n"
        "[bold]Book:[/bold] Linux Basics and Cheat Sheets\n"
        "  Amazon: https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/\n\n"
        "[bold]GitHub:[/bold] https://github.com/CamoRageaholic1/Linux-Admin-Toolkit\n\n"
        "[bold]License:[/bold] MIT\n",
        border_style="cyan"
    ))

if __name__ == '__main__':
    cli()
