#!/usr/bin/env python3
"""
Linux Admin Toolkit
Professional Linux administration tools with automation and monitoring.

Author: David Osisek
Book: Linux Basics and Cheat Sheets (Amazon)
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='linux-admin-toolkit',
    version='1.0.0',
    description='Professional Linux administration toolkit with automation and monitoring tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CamoRageaholic1/Linux-Admin-Toolkit',
    author='David Osisek',
    author_email='david.osisek@example.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='linux, system administration, automation, security, monitoring, devops',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'click>=8.1.0',
        'rich>=13.0.0',
        'psutil>=5.9.0',
        'pyyaml>=6.0',
        'python-dateutil>=2.8.0',
        'paramiko>=3.0.0',
        'cryptography>=41.0.0',
        'tabulate>=0.9.0',
        'colorama>=0.4.6',
    ],
    entry_points={
        'console_scripts': [
            'linux-harden=linux_toolkit.system_hardening:main',
            'linux-users=linux_toolkit.user_management:main',
            'linux-logs=linux_toolkit.log_analyzer:main',
            'linux-backup=linux_toolkit.backup_tool:main',
            'linux-monitor=linux_toolkit.service_monitor:main',
            'linux-tune=linux_toolkit.performance_tuner:main',
            'linux-audit=linux_toolkit.security_auditor:main',
            'linux-packages=linux_toolkit.package_manager:main',
            'linux-ref=linux_toolkit.quick_ref:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/CamoRageaholic1/Linux-Admin-Toolkit/issues',
        'Source': 'https://github.com/CamoRageaholic1/Linux-Admin-Toolkit',
        'Author Book': 'https://www.amazon.com/Linux-Basics-Cheat-Sheets-Osisek/dp/B0CGL65W3J/',
    },
)
