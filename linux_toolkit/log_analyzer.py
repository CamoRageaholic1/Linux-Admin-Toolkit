#!/usr/bin/env python3
"""
Log Analyzer Tool
Parse and analyze system logs for security events and errors.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import re
import click
from datetime import datetime, timedelta
from pathlib import Path
from rich.console import Console
from rich.table import Table
from collections import Counter

console = Console()

class LogAnalyzer:
    """System log analysis tool."""
    
    def __init__(self):
        self.log_paths = {
            'auth': '/var/log/auth.log',
            'syslog': '/var/log/syslog',
            'kernel': '/var/log/kern.log',
        }
    
    def parse_log_file(self, log_type: str, hours: int = 24):
        """Parse log file for recent entries."""
        log_path = self.log_paths.get(log_type)
        
        if not log_path or not Path(log_path).exists():
            console.print(f"[red]Log file not found: {log_path}[/red]")
            return []
        
        cutoff_time = datetime.now() - timedelta(hours=hours)
        entries = []
        
        with open(log_path, 'r') as f:
            for line in f:
                entries.append(line.strip())
        
        return entries
    
    def find_failed_logins(self, hours: int = 24):
        """Find failed login attempts."""
        console.print("\n[cyan]Analyzing failed login attempts...[/cyan]\n")
        
        entries = self.parse_log_file('auth', hours)
        failed_logins = []
        
        for entry in entries:
            if 'Failed password' in entry or 'authentication failure' in entry:
                failed_logins.append(entry)
        
        # Extract IP addresses
        ips = []
        for entry in failed_logins:
            ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', entry)
            if ip_match:
                ips.append(ip_match.group())
        
        # Count by IP
        ip_counts = Counter(ips)
        
        table = Table(title=f"Failed Logins (Last {hours} hours)")
        table.add_column("IP Address", style="cyan")
        table.add_column("Attempts", style="red")
        
        for ip, count in ip_counts.most_common(10):
            table.add_row(ip, str(count))
        
        console.print(table)
        console.print(f"\nTotal failed attempts: {len(failed_logins)}")
        console.print(f"Unique IPs: {len(ip_counts)}")
    
    def analyze_errors(self, log_type: str = 'syslog', hours: int = 24):
        """Analyze error messages."""
        console.print(f"\n[cyan]Analyzing errors in {log_type}...[/cyan]\n")
        
        entries = self.parse_log_file(log_type, hours)
        errors = [e for e in entries if 'error' in e.lower() or 'failed' in e.lower()]
        
        console.print(f"Found {len(errors)} error entries in last {hours} hours")
        
        if errors:
            console.print("\n[yellow]Recent errors:[/yellow]")
            for error in errors[:10]:
                console.print(f"  {error[:100]}...")

@click.command()
@click.option('--log-type', type=click.Choice(['auth', 'syslog', 'kernel']), default='auth',
              help='Log file to analyze')
@click.option('--failed-logins', is_flag=True, help='Find failed login attempts')
@click.option('--errors', is_flag=True, help='Find error messages')
@click.option('--hours', default=24, help='Hours to look back')
def main(log_type, failed_logins, errors, hours):
    """Linux Log Analyzer Tool."""
    analyzer = LogAnalyzer()
    
    if failed_logins:
        analyzer.find_failed_logins(hours)
    elif errors:
        analyzer.analyze_errors(log_type, hours)
    else:
        console.print("[yellow]Use --failed-logins or --errors to analyze logs[/yellow]")

if __name__ == '__main__':
    main()
