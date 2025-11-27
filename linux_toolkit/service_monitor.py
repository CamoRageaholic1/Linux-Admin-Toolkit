#!/usr/bin/env python3
"""
Service Monitor Tool
Monitor system services and health checks.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import subprocess
import click
import psutil
from rich.console import Console
from rich.table import Table
from typing import List

console = Console()

class ServiceMonitor:
    """Service monitoring tool."""
    
    def check_service(self, service_name: str) -> dict:
        """Check if a service is running."""
        result = subprocess.run(
            f"systemctl is-active {service_name}",
            shell=True,
            capture_output=True,
            text=True
        )
        
        is_active = result.returncode == 0
        
        return {
            'name': service_name,
            'active': is_active,
            'status': result.stdout.strip()
        }
    
    def monitor_services(self, services: List[str]):
        """Monitor multiple services."""
        console.print("\n[cyan]Service Status Monitor[/cyan]\n")
        
        table = Table(title="Service Status")
        table.add_column("Service", style="cyan")
        table.add_column("Status", style="green")
        
        for service in services:
            info = self.check_service(service)
            status = "✓ Active" if info['active'] else "✗ Inactive"
            style = "green" if info['active'] else "red"
            table.add_row(info['name'], f"[{style}]{status}[/{style}]")
        
        console.print(table)
    
    def system_resources(self):
        """Display system resource usage."""
        console.print("\n[cyan]System Resource Usage[/cyan]\n")
        
        # CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        console.print(f"CPU Usage: {cpu_percent}%")
        
        # Memory
        memory = psutil.virtual_memory()
        console.print(f"Memory Usage: {memory.percent}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)")
        
        # Disk
        disk = psutil.disk_usage('/')
        console.print(f"Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)")
        
        # Load average
        load_avg = psutil.getloadavg()
        console.print(f"Load Average: {load_avg[0]:.2f}, {load_avg[1]:.2f}, {load_avg[2]:.2f}")

@click.command()
@click.option('--services', help='Comma-separated list of services to monitor')
@click.option('--system', is_flag=True, help='Show system resource usage')
@click.option('--critical', is_flag=True, help='Monitor critical services')
def main(services, system, critical):
    """Linux Service Monitor Tool."""
    monitor = ServiceMonitor()
    
    if system:
        monitor.system_resources()
    elif critical:
        critical_services = ['sshd', 'systemd', 'cron']
        monitor.monitor_services(critical_services)
    elif services:
        service_list = [s.strip() for s in services.split(',')]
        monitor.monitor_services(service_list)
    else:
        console.print("[yellow]Use --services, --system, or --critical[/yellow]")

if __name__ == '__main__':
    main()
