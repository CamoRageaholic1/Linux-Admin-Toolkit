#!/usr/bin/env python3
"""
Performance Tuner Tool
System optimization and performance tuning.

Author: David Osisek
Book: Linux Basics and Cheat Sheets
"""

import subprocess
import click
from rich.console import Console

console = Console()

class PerformanceTuner:
    """System performance tuning tool."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
    
    def optimize_swappiness(self, value: int = 10):
        """Optimize swappiness value."""
        console.print(f"\n[cyan]Setting swappiness to {value}...[/cyan]")
        
        cmd = f"sysctl vm.swappiness={value}"
        
        if self.dry_run:
            console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
        else:
            subprocess.run(cmd, shell=True)
            console.print("[green]✓ Swappiness optimized[/green]")
    
    def tune_network(self):
        """Tune network performance."""
        console.print("\n[cyan]Tuning network parameters...[/cyan]")
        
        commands = [
            "sysctl -w net.core.rmem_max=16777216",
            "sysctl -w net.core.wmem_max=16777216",
            "sysctl -w net.ipv4.tcp_rmem='4096 87380 16777216'",
            "sysctl -w net.ipv4.tcp_wmem='4096 65536 16777216'",
        ]
        
        for cmd in commands:
            if self.dry_run:
                console.print(f"[yellow]DRY RUN: {cmd}[/yellow]")
            else:
                subprocess.run(cmd, shell=True)
        
        console.print("[green]✓ Network tuned[/green]")
    
    def clear_cache(self):
        """Clear system caches."""
        console.print("\n[cyan]Clearing system caches...[/cyan]")
        
        if self.dry_run:
            console.print("[yellow]DRY RUN: sync && echo 3 > /proc/sys/vm/drop_caches[/yellow]")
        else:
            subprocess.run("sync", shell=True)
            subprocess.run("echo 3 > /proc/sys/vm/drop_caches", shell=True)
            console.print("[green]✓ Caches cleared[/green]")

@click.command()
@click.option('--swappiness', type=int, help='Set swappiness value')
@click.option('--network', is_flag=True, help='Tune network performance')
@click.option('--cache', is_flag=True, help='Clear system caches')
@click.option('--dry-run', is_flag=True, help='Dry run mode')
def main(swappiness, network, cache, dry_run):
    """Linux Performance Tuner Tool."""
    tuner = PerformanceTuner(dry_run=dry_run)
    
    if swappiness:
        tuner.optimize_swappiness(swappiness)
    elif network:
        tuner.tune_network()
    elif cache:
        tuner.clear_cache()
    else:
        console.print("[yellow]Use --swappiness, --network, or --cache[/yellow]")

if __name__ == '__main__':
    main()
