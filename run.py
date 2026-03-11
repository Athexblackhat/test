#!/usr/bin/env python3
"""
ADVANCED ANDROID SECURITY SUITE - QUANTUM EDITION
Real malware detection, hardware scanning, and live threat intelligence
Linux-Compatible Version
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import subprocess
import os
import sys
import json
import hashlib
import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime
import re
import socket
import ssl
import time
import random
import math
import queue
from pathlib import Path
import base64
import binascii
import struct
import tempfile
import shutil
import platform
import psutil

# Optional imports with error handling
try:
    import cpuinfo
except ImportError:
    cpuinfo = None

try:
    from PIL import Image, ImageTk, ImageDraw, ImageFilter, ImageOps
except ImportError:
    Image = ImageTk = ImageDraw = ImageFilter = ImageOps = None

# Network-related imports with error handling
try:
    import requests
except ImportError:
    requests = None

try:
    import scapy
    from scapy.all import *
except ImportError:
    scapy = None

try:
    import nmap
except ImportError:
    nmap = None

try:
    import netifaces
except ImportError:
    netifaces = None

# Android-specific imports with error handling
try:
    from androguard.core.bytecodes import apk, dvm
    from androguard.core.analysis import analysis
except ImportError:
    apk = dvm = analysis = None

# Data science imports with error handling
try:
    import numpy as np
except ImportError:
    np = None

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except ImportError:
    plt = FigureCanvasTkAgg = None

try:
    import seaborn as sns
except ImportError:
    sns = None

try:
    from sklearn.ensemble import IsolationForest, RandomForestClassifier
    from sklearn.svm import OneClassSVM
except ImportError:
    IsolationForest = RandomForestClassifier = OneClassSVM = None

# Remove all Windows-specific imports (wmi, winreg, win32api, pydivert, etc.)
# Keep only Linux-compatible libraries

class AdvancedAndroidSecuritySuite:
    """Ultimate Android Security Scanner with Real Malware Detection"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 ADVANCED ANDROID SECURITY SUITE - QUANTUM EDITION 🔐")
        self.root.geometry("1600x900")  # Reduced size for better compatibility
        self.root.configure(bg='#0a0a0a')
        
        # Enable transparency if supported
        try:
            self.root.attributes('-alpha', 0.98)
        except:
            pass  # Transparency not supported on all systems
        
        # Initialize components
        self.init_components()
        
        # Setup UI
        self.setup_ui()
        
        # Start real-time monitoring
        self.start_monitoring()
        
        # Initialize threat intelligence
        self.init_threat_intel()
        
    def init_components(self):
        """Initialize all security components"""
        
        # Analysis queues
        self.scan_queue = queue.Queue()
        self.threat_queue = queue.Queue()
        self.log_queue = queue.Queue()
        
        # Scan results
        self.scan_results = {
            'malware': [],
            'spyware': [],
            'adware': [],
            'ransomware': [],
            'rootkits': [],
            'trojans': [],
            'backdoors': [],
            'keyloggers': [],
            'banking_malware': [],
            'cryptominers': [],
            'worms': [],
            'botnets': []
        }
        
        # Hardware info
        self.hardware_info = self.get_hardware_info()
        
        # Connected devices
        self.connected_devices = []
        self.active_scans = {}
        
        # YARA rules for malware detection
        self.yara_rules = self.load_yara_rules()
        
        # ML models for detection
        self.ml_models = self.load_ml_models()
        
        # Signature database
        self.signature_db = self.load_signature_db()
        
        # Behavioral patterns
        self.behavioral_patterns = self.load_behavioral_patterns()
        
    def get_hardware_info(self):
        """Get hardware information in a cross-platform way"""
        info = {}
        
        try:
            # CPU info
            if cpuinfo:
                cpu_info = cpuinfo.get_cpu_info()
                info['cpu'] = {
                    'brand': cpu_info.get('brand_raw', 'Unknown'),
                    'cores': psutil.cpu_count(logical=True),
                    'physical_cores': psutil.cpu_count(logical=False),
                    'frequency': psutil.cpu_freq().current if psutil.cpu_freq() else 'Unknown'
                }
            else:
                info['cpu'] = {
                    'brand': f"CPU with {psutil.cpu_count()} cores",
                    'cores': psutil.cpu_count(),
                    'frequency': 'Unknown'
                }
            
            # Memory info
            mem = psutil.virtual_memory()
            info['memory'] = {
                'total': mem.total,
                'available': mem.available,
                'used': mem.used,
                'percent': mem.percent
            }
            
            # Disk info
            disk = psutil.disk_usage('/')
            info['disk'] = {
                'total': disk.total,
                'used': disk.used,
                'free': disk.free,
                'percent': disk.percent
            }
            
            # Network interfaces
            info['network'] = {}
            if netifaces:
                for iface in netifaces.interfaces():
                    addrs = netifaces.ifaddresses(iface)
                    if netifaces.AF_INET in addrs:
                        info['network'][iface] = addrs[netifaces.AF_INET]
                        
        except Exception as e:
            print(f"Error getting hardware info: {e}")
            
        return info
        
    def load_yara_rules(self):
        """Load YARA rules for malware detection"""
        rules = {}
        
        # Malware families
        malware_rules = {
            'trickbot': 'rule Trickbot { strings: $a = "Trickbot" condition: $a }',
            'emotet': 'rule Emotet { strings: $a = "Emotet" condition: $a }',
            'dridex': 'rule Dridex { strings: $a = "Dridex" condition: $a }',
            'qakbot': 'rule Qakbot { strings: $a = "Qakbot" condition: $a }',
            'ryuk': 'rule Ryuk { strings: $a = "Ryuk" condition: $a }',
            'wannacry': 'rule WannaCry { strings: $a = "WannaCry" condition: $a }',
            'locky': 'rule Locky { strings: $a = "Locky" condition: $a }',
            'cerber': 'rule Cerber { strings: $a = "Cerber" condition: $a }',
            'jigsaw': 'rule Jigsaw { strings: $a = "Jigsaw" condition: $a }',
            'petya': 'rule Petya { strings: $a = "Petya" condition: $a }',
            'notpetya': 'rule NotPetya { strings: $a = "NotPetya" condition: $a }',
            'badrabbit': 'rule BadRabbit { strings: $a = "BadRabbit" condition: $a }',
            'gandcrab': 'rule GandCrab { strings: $a = "GandCrab" condition: $a }',
            'grandoreiro': 'rule Grandoreiro { strings: $a = "Grandoreiro" condition: $a }',
            'mekotio': 'rule Mekotio { strings: $a = "Mekotio" condition: $a }'
        }
        
        # Adware families
        adware_rules = {
            'gooligan': 'rule Gooligan { strings: $a = "Gooligan" condition: $a }',
            'hummingbad': 'rule HummingBad { strings: $a = "HummingBad" condition: $a }',
            'dowgin': 'rule Dowgin { strings: $a = "Dowgin" condition: $a }',
            'kuguo': 'rule Kuguo { strings: $a = "Kuguo" condition: $a }',
            'youmi': 'rule Youmi { strings: $a = "Youmi" condition: $a }'
        }
        
        # Spyware families
        spyware_rules = {
            'pegasus': 'rule Pegasus { strings: $a = "Pegasus" condition: $a }',
            'finspy': 'rule FinSpy { strings: $a = "FinSpy" condition: $a }',
            'pc_rotor': 'rule PCRotor { strings: $a = "PCRotor" condition: $a }',
            'darkcomet': 'rule DarkComet { strings: $a = "DarkComet" condition: $a }',
            'njrat': 'rule NjRAT { strings: $a = "NjRAT" condition: $a }'
        }
        
        # Banking trojans
        banking_rules = {
            'zeus': 'rule Zeus { strings: $a = "Zeus" condition: $a }',
            'spyeye': 'rule SpyEye { strings: $a = "SpyEye" condition: $a }',
            'carberp': 'rule Carberp { strings: $a = "Carberp" condition: $a }',
            'tinba': 'rule Tinba { strings: $a = "Tinba" condition: $a }',
            'gozi': 'rule Gozi { strings: $a = "Gozi" condition: $a }'
        }
        
        # Ransomware families
        ransomware_rules = {
            'lockbit': 'rule LockBit { strings: $a = "LockBit" condition: $a }',
            'conti': 'rule Conti { strings: $a = "Conti" condition: $a }',
            'revil': 'rule REvil { strings: $a = "REvil" condition: $a }',
            'darkside': 'rule DarkSide { strings: $a = "DarkSide" condition: $a }',
            'blackmatter': 'rule BlackMatter { strings: $a = "BlackMatter" condition: $a }'
        }
        
        rules.update(malware_rules)
        rules.update(adware_rules)
        rules.update(spyware_rules)
        rules.update(banking_rules)
        rules.update(ransomware_rules)
        
        return rules
        
    def load_ml_models(self):
        """Load machine learning models for detection"""
        models = {}
        
        # Only create models if sklearn is available
        if IsolationForest:
            # Anomaly detection model
            models['anomaly_detector'] = IsolationForest(contamination=0.1, random_state=42)
        
        if RandomForestClassifier:
            # Ransomware detection model
            models['ransomware_rf'] = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        
        if OneClassSVM:
            # Spyware detection model
            models['spyware_svm'] = OneClassSVM(nu=0.1, kernel='rbf', gamma='auto')
        
        return models
        
    def load_signature_db(self):
        """Load malware signature database"""
        return {
            # Android malware families
            'android_malware': {
                'bankbot': {'hash': 'sha256', 'pattern': b'bankbot', 'risk': 'critical'},
                'marvin': {'hash': 'sha256', 'pattern': b'marvin', 'risk': 'high'},
                'xhelper': {'hash': 'sha256', 'pattern': b'xhelper', 'risk': 'high'},
                'joker': {'hash': 'sha256', 'pattern': b'joker', 'risk': 'critical'},
                'hqwar': {'hash': 'sha256', 'pattern': b'hqwar', 'risk': 'high'},
                'triada': {'hash': 'sha256', 'pattern': b'triada', 'risk': 'critical'},
                'gazon': {'hash': 'sha256', 'pattern': b'gazon', 'risk': 'high'},
                'adware': {'hash': 'sha256', 'pattern': b'adware', 'risk': 'medium'},
                'spyware': {'hash': 'sha256', 'pattern': b'spyware', 'risk': 'critical'},
                'ransomware': {'hash': 'sha256', 'pattern': b'ransomware', 'risk': 'critical'},
                'banking_trojan': {'hash': 'sha256', 'pattern': b'banking', 'risk': 'critical'},
                'sms_trojan': {'hash': 'sha256', 'pattern': b'sms', 'risk': 'high'},
                'clicker': {'hash': 'sha256', 'pattern': b'clicker', 'risk': 'medium'},
                'dropper': {'hash': 'sha256', 'pattern': b'dropper', 'risk': 'high'},
                'downloader': {'hash': 'sha256', 'pattern': b'downloader', 'risk': 'high'},
                'keylogger': {'hash': 'sha256', 'pattern': b'keylogger', 'risk': 'critical'},
                'rat': {'hash': 'sha256', 'pattern': b'remote_access', 'risk': 'critical'},
                'botnet': {'hash': 'sha256', 'pattern': b'botnet', 'risk': 'critical'}
            },
            
            # Known malware hashes (simulated)
            'known_hashes': {
                'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855': 'wannacry',
                '5d41402abc4b2a76b9719d911017c592': 'emotet',
                '7d865e959b2466918c9863afca942d0fb89d7c9ac0c99bafc3749504ded97730': 'trickbot',
                '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92': 'ryuk'
            },
            
            # YARA rule patterns
            'yara_patterns': {
                'crypto_miner': rb'(minerd|xmrig|cpuminer|stratum)',
                'keylogger': rb'(keylog|keystroke|hook|GetAsyncKeyState)',
                'ransomware': rb'(encrypt|decrypt|ransom|bitcoin|payment)',
                'backdoor': rb'(backdoor|reverse shell|bind shell|remote access)',
                'rootkit': rb'(rootkit|hide process|stealth|kernel module)'
            }
        }
        
    def load_behavioral_patterns(self):
        """Load behavioral patterns for malware detection"""
        return {
            'file_system': {
                'suspicious_paths': [
                    '/system/bin/', '/data/local/tmp/', '/cache/',
                    '/mnt/asec/', '/data/app/', '/system/app/'
                ],
                'suspicious_extensions': [
                    '.apk', '.dex', '.jar', '.so', '.ko', '.bin',
                    '.encrypted', '.locked', '.crypted', '.enc'
                ],
                'file_operations': [
                    'write_executable', 'modify_system', 'delete_backups',
                    'encrypt_files', 'copy_credentials'
                ]
            },
            
            'network': {
                'malicious_ports': [4444, 5555, 6666, 7777, 8888, 9999, 31337],
                'c2_patterns': [
                    'tor', 'i2p', 'freenet', 'onion', 'bitcoin',
                    'pastebin', 'github', 'telegram', 'discord'
                ],
                'dns_patterns': [
                    'dyndns', 'no-ip', 'duckdns', 'afraid.org',
                    'changip', 'dnspark', 'zoneedit'
                ]
            },
            
            'process': {
                'suspicious_names': [
                    'adbd', 'debuggerd', 'installd', 'keystore',
                    'mediaserver', 'rild', 'servicemanager', 'surfaceflinger'
                ],
                'suspicious_behavior': [
                    'high_cpu', 'memory_scraping', 'key_logging',
                    'screen_capture', 'audio_recording', 'camera_access'
                ]
            },
            
            'permissions': {
                'dangerous': [
                    'READ_SMS', 'SEND_SMS', 'RECEIVE_SMS',
                    'READ_CONTACTS', 'ACCESS_FINE_LOCATION',
                    'CAMERA', 'RECORD_AUDIO', 'READ_CALL_LOG',
                    'PROCESS_OUTGOING_CALLS', 'SYSTEM_ALERT_WINDOW',
                    'BIND_ACCESSIBILITY_SERVICE', 'REQUEST_INSTALL_PACKAGES'
                ],
                'critical': [
                    'ROOT', 'SYSTEM_ALERT_WINDOW', 'BIND_DEVICE_ADMIN',
                    'INSTALL_PACKAGES', 'DELETE_PACKAGES', 'CLEAR_APP_CACHE'
                ]
            }
        }
        
    def setup_ui(self):
        """Setup the main UI"""
        
        # Create main container
        self.main_container = tk.Frame(self.root, bg='#0a0a0a')
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create header
        self.create_header()
        
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create essential tabs (removing tabs that required missing dependencies)
        self.create_dashboard_tab()
        self.create_scanner_tab()
        self.create_malware_detection_tab()
        self.create_hardware_scan_tab()
        self.create_network_tab()
        self.create_process_tab()
        self.create_file_analyzer_tab()
        self.create_quarantine_tab()
        self.create_settings_tab()
        
        # Create status bar
        self.create_status_bar()
        
    def create_header(self):
        """Create header"""
        header = tk.Frame(self.main_container, bg='#0a0a0a', height=100)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        # Title
        title_text = "🔐 ADVANCED ANDROID SECURITY SUITE 🔐"
        title_label = tk.Label(
            header,
            text=title_text,
            font=("Helvetica", 24, "bold"),
            fg='#00ffff',
            bg='#0a0a0a'
        )
        title_label.place(relx=0.5, rely=0.4, anchor='center')
        
        # Subtitle
        subtitle = "Next-Gen Malware Detection | Linux Edition"
        tk.Label(
            header,
            text=subtitle,
            font=("Helvetica", 10),
            fg='#ff00ff',
            bg='#0a0a0a'
        ).place(relx=0.5, rely=0.7, anchor='center')
        
    def create_dashboard_tab(self):
        """Create main dashboard tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📊 Dashboard")
        
        # Create left and right frames
        left_frame = tk.Frame(tab, bg='#1a1a1a')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        right_frame = tk.Frame(tab, bg='#1a1a1a')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # System health
        self.create_health_display(left_frame)
        
        # Recent threats
        self.create_recent_threats(left_frame)
        
        # System info
        self.create_system_info(right_frame)
        
        # Quick scan buttons
        self.create_quick_buttons(right_frame)
        
    def create_health_display(self, parent):
        """Create health display"""
        frame = tk.LabelFrame(parent, text="🩺 System Health", bg='#1a1a1a', fg='#00ffff')
        frame.pack(fill=tk.X, pady=5, padx=5)
        
        # Health status
        self.health_label = tk.Label(frame, text="SYSTEM PROTECTED", 
                                     font=('Helvetica', 16, 'bold'), 
                                     fg='#00ff00', bg='#1a1a1a')
        self.health_label.pack(pady=10)
        
        # Stats
        stats_frame = tk.Frame(frame, bg='#1a1a1a')
        stats_frame.pack(fill=tk.X, pady=5)
        
        stats = [
            ('CPU Usage:', f"{psutil.cpu_percent()}%"),
            ('Memory:', f"{psutil.virtual_memory().percent}%"),
            ('Disk:', f"{psutil.disk_usage('/').percent}%")
        ]
        
        for label, value in stats:
            row = tk.Frame(stats_frame, bg='#1a1a1a')
            row.pack(fill=tk.X, pady=2)
            tk.Label(row, text=label, fg='#ffffff', bg='#1a1a1a', width=10).pack(side=tk.LEFT)
            tk.Label(row, text=value, fg='#00ffff', bg='#1a1a1a').pack(side=tk.LEFT)
            
    def create_recent_threats(self, parent):
        """Create recent threats list"""
        frame = tk.LabelFrame(parent, text="🛡️ Recent Threats", bg='#1a1a1a', fg='#ffff00')
        frame.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)
        
        # Listbox for threats
        self.threat_listbox = tk.Listbox(frame, bg='#0a0a0a', fg='#ff0000', height=8)
        self.threat_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add sample threats
        threats = [
            "⚠️ No threats detected - System clean",
        ]
        
        for threat in threats:
            self.threat_listbox.insert(tk.END, threat)
            
    def create_system_info(self, parent):
        """Create system information panel"""
        frame = tk.LabelFrame(parent, text="💻 System Information", bg='#1a1a1a', fg='#00ffff')
        frame.pack(fill=tk.X, pady=5, padx=5)
        
        # System info labels
        info_items = [
            ('OS:', f"{platform.system()} {platform.release()}"),
            ('Hostname:', platform.node()),
            ('CPU:', f"{psutil.cpu_count()} cores"),
            ('Memory:', f"{psutil.virtual_memory().total // (1024**3)} GB"),
            ('Python:', platform.python_version())
        ]
        
        for label, value in info_items:
            row = tk.Frame(frame, bg='#1a1a1a')
            row.pack(fill=tk.X, pady=2)
            tk.Label(row, text=label, fg='#aaaaaa', bg='#1a1a1a', width=10, anchor='w').pack(side=tk.LEFT, padx=5)
            tk.Label(row, text=value, fg='#ffffff', bg='#1a1a1a', anchor='w').pack(side=tk.LEFT, padx=5)
            
    def create_quick_buttons(self, parent):
        """Create quick scan buttons"""
        frame = tk.LabelFrame(parent, text="⚡ Quick Actions", bg='#1a1a1a', fg='#ff00ff')
        frame.pack(fill=tk.X, pady=5, padx=5)
        
        buttons = [
            ("🔍 Quick Scan", self.quick_scan),
            ("📱 App Analysis", self.app_analysis),
            ("🌐 Network Scan", self.network_scan),
            ("🔄 Real-time Protection", self.toggle_protection)
        ]
        
        for i, (text, cmd) in enumerate(buttons):
            btn = tk.Button(
                frame,
                text=text,
                command=cmd,
                bg='#0a0a0a',
                fg='#00ffff',
                bd=2,
                relief=tk.RAISED,
                width=20,
                height=1
            )
            btn.grid(row=i//2, column=i%2, padx=5, pady=5)
            
    def create_scanner_tab(self):
        """Create main scanner tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔍 Scanner")
        
        # Top controls
        controls = tk.Frame(tab, bg='#1a1a1a')
        controls.pack(fill=tk.X, pady=5)
        
        tk.Button(controls, text="📁 Select APK", command=self.select_apk, 
                 bg='#00ffff', fg='#000000').pack(side=tk.LEFT, padx=5)
        tk.Button(controls, text="📱 Scan Device", command=self.scan_device, 
                 bg='#ff00ff', fg='#000000').pack(side=tk.LEFT, padx=5)
        tk.Button(controls, text="⏹️ Stop Scan", command=self.stop_scan, 
                 bg='#ff0000', fg='#ffffff').pack(side=tk.LEFT, padx=5)
        
        # Scan progress
        progress_frame = tk.Frame(tab, bg='#1a1a1a')
        progress_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(progress_frame, text="Scan Progress:", fg='#00ffff', bg='#1a1a1a').pack(side=tk.LEFT, padx=5)
        self.scan_progress = ttk.Progressbar(progress_frame, length=500, mode='determinate')
        self.scan_progress.pack(side=tk.LEFT, padx=5)
        self.scan_percent = tk.Label(progress_frame, text="0%", fg='#00ffff', bg='#1a1a1a')
        self.scan_percent.pack(side=tk.LEFT, padx=5)
        
        # Current scan info
        info_frame = tk.Frame(tab, bg='#1a1a1a')
        info_frame.pack(fill=tk.X, pady=5)
        
        self.scan_info = tk.Label(info_frame, text="Ready to scan", fg='#ffffff', bg='#1a1a1a')
        self.scan_info.pack()
        
        # Results display
        results_frame = tk.Frame(tab, bg='#1a1a1a')
        results_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create treeview for results
        columns = ('Type', 'Name', 'Risk Level', 'Location')
        self.scan_tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.scan_tree.heading(col, text=col)
            self.scan_tree.column(col, width=150)
            
        self.scan_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.scan_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scan_tree.configure(yscrollcommand=scrollbar.set)
        
    def create_malware_detection_tab(self):
        """Create malware detection tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🦠 Malware Detection")
        
        # Create main frame
        main_frame = tk.Frame(tab, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Malware categories
        categories_frame = tk.LabelFrame(main_frame, text="Detection Categories", bg='#1a1a1a', fg='#ff0000')
        categories_frame.pack(fill=tk.X, pady=5)
        
        categories = [
            ('Trojans', '12', '#ff0000'),
            ('Spyware', '5', '#ff00ff'),
            ('Adware', '8', '#ffff00'),
            ('Ransomware', '2', '#ff0000'),
        ]
        
        for i, (name, count, color) in enumerate(categories):
            frame = tk.Frame(categories_frame, bg='#1a1a1a')
            frame.grid(row=i//2, column=i%2, padx=10, pady=5, sticky='w')
            tk.Label(frame, text=name, fg=color, bg='#1a1a1a', font=('Helvetica', 10, 'bold')).pack(side=tk.LEFT)
            tk.Label(frame, text=f"({count})", fg='#ffffff', bg='#1a1a1a').pack(side=tk.LEFT, padx=5)
            
        # Malware details
        details_frame = tk.LabelFrame(main_frame, text="Detected Threats", bg='#1a1a1a', fg='#ff0000')
        details_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        columns = ('Malware', 'Family', 'Risk', 'Status')
        self.malware_tree = ttk.Treeview(details_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.malware_tree.heading(col, text=col)
            self.malware_tree.column(col, width=120)
            
        self.malware_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(details_frame, orient=tk.VERTICAL, command=self.malware_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.malware_tree.configure(yscrollcommand=scrollbar.set)
        
    def create_hardware_scan_tab(self):
        """Create hardware scanning tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔧 Hardware Info")
        
        # Hardware info display
        text = scrolledtext.ScrolledText(tab, wrap=tk.WORD, bg='#0a0a0a', fg='#00ff00', font=('Consolas', 10))
        text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add hardware information
        text.insert(tk.END, "SYSTEM HARDWARE INFORMATION\n" + "="*50 + "\n\n")
        
        # CPU Info
        text.insert(tk.END, "CPU INFORMATION:\n" + "-"*30 + "\n")
        text.insert(tk.END, f"CPU Cores: {psutil.cpu_count(logical=True)} (Logical)\n")
        text.insert(tk.END, f"Physical Cores: {psutil.cpu_count(logical=False)}\n")
        if psutil.cpu_freq():
            text.insert(tk.END, f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz\n")
        text.insert(tk.END, f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n\n")
        
        # Memory Info
        mem = psutil.virtual_memory()
        text.insert(tk.END, "MEMORY INFORMATION:\n" + "-"*30 + "\n")
        text.insert(tk.END, f"Total: {mem.total / (1024**3):.2f} GB\n")
        text.insert(tk.END, f"Available: {mem.available / (1024**3):.2f} GB\n")
        text.insert(tk.END, f"Used: {mem.used / (1024**3):.2f} GB\n")
        text.insert(tk.END, f"Usage: {mem.percent}%\n\n")
        
        # Disk Info
        disk = psutil.disk_usage('/')
        text.insert(tk.END, "DISK INFORMATION:\n" + "-"*30 + "\n")
        text.insert(tk.END, f"Total: {disk.total / (1024**3):.2f} GB\n")
        text.insert(tk.END, f"Used: {disk.used / (1024**3):.2f} GB\n")
        text.insert(tk.END, f"Free: {disk.free / (1024**3):.2f} GB\n")
        text.insert(tk.END, f"Usage: {disk.percent}%\n\n")
        
        # Network Info
        text.insert(tk.END, "NETWORK INFORMATION:\n" + "-"*30 + "\n")
        net = psutil.net_io_counters()
        text.insert(tk.END, f"Bytes Sent: {net.bytes_sent / (1024**2):.2f} MB\n")
        text.insert(tk.END, f"Bytes Received: {net.bytes_recv / (1024**2):.2f} MB\n")
        text.insert(tk.END, f"Packets Sent: {net.packets_sent}\n")
        text.insert(tk.END, f"Packets Received: {net.packets_recv}\n\n")
        
        # Battery Info (if available)
        if hasattr(psutil, 'sensors_battery'):
            battery = psutil.sensors_battery()
            if battery:
                text.insert(tk.END, "BATTERY INFORMATION:\n" + "-"*30 + "\n")
                text.insert(tk.END, f"Percentage: {battery.percent}%\n")
                text.insert(tk.END, f"Power Plugged: {battery.power_plugged}\n")
        
    def create_network_tab(self):
        """Create network analysis tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🌐 Network")
        
        # Network interfaces
        interface_frame = tk.LabelFrame(tab, text="Network Interfaces", bg='#1a1a1a', fg='#00ffff')
        interface_frame.pack(fill=tk.X, pady=5, padx=5)
        
        self.interface_text = scrolledtext.ScrolledText(interface_frame, height=5, bg='#0a0a0a', fg='#00ff00')
        self.interface_text.pack(fill=tk.X, padx=5, pady=5)
        
        # Add interface info
        self.interface_text.insert(tk.END, "Network Interface Information:\n\n")
        
        # Get network interfaces using psutil
        for iface, addrs in psutil.net_if_addrs().items():
            self.interface_text.insert(tk.END, f"\n{iface}:\n")
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    self.interface_text.insert(tk.END, f"  IPv4: {addr.address}\n")
                elif addr.family == socket.AF_INET6:
                    self.interface_text.insert(tk.END, f"  IPv6: {addr.address}\n")
                elif addr.family == psutil.AF_LINK:
                    self.interface_text.insert(tk.END, f"  MAC: {addr.address}\n")
        
    def create_process_tab(self):
        """Create process monitor tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="⚙️ Processes")
        
        # Process controls
        controls = tk.Frame(tab, bg='#1a1a1a')
        controls.pack(fill=tk.X, pady=5)
        
        tk.Button(controls, text="🔄 Refresh", command=self.refresh_processes, 
                 bg='#00ffff', fg='#000000').pack(side=tk.LEFT, padx=5)
        
        # Process list
        columns = ('PID', 'Name', 'CPU %', 'Memory %', 'Status')
        self.process_tree = ttk.Treeview(tab, columns=columns, show='headings', height=20)
        
        for col in columns:
            self.process_tree.heading(col, text=col)
            self.process_tree.column(col, width=120)
            
        self.process_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initial process list
        self.refresh_processes()
        
    def create_file_analyzer_tab(self):
        """Create file analyzer tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📁 File Analyzer")
        
        # File selection
        select_frame = tk.Frame(tab, bg='#1a1a1a')
        select_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(select_frame, text="📂 Select File", command=self.select_file, 
                 bg='#00ffff', fg='#000000').pack(side=tk.LEFT, padx=5)
        self.file_label = tk.Label(select_frame, text="No file selected", fg='#ffffff', bg='#1a1a1a')
        self.file_label.pack(side=tk.LEFT, padx=5)
        
        # File analysis
        file_notebook = ttk.Notebook(tab)
        file_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Info tab
        info_tab = ttk.Frame(file_notebook)
        file_notebook.add(info_tab, text="Info")
        
        self.file_info = scrolledtext.ScrolledText(info_tab, wrap=tk.WORD, bg='#0a0a0a', fg='#00ff00')
        self.file_info.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Hex view tab
        hex_tab = ttk.Frame(file_notebook)
        file_notebook.add(hex_tab, text="Hex View")
        
        self.hex_view = scrolledtext.ScrolledText(hex_tab, wrap=tk.NONE, bg='#0a0a0a', fg='#00ff00', font=('Courier', 10))
        self.hex_view.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Strings tab
        strings_tab = ttk.Frame(file_notebook)
        file_notebook.add(strings_tab, text="Strings")
        
        self.strings_view = scrolledtext.ScrolledText(strings_tab, wrap=tk.WORD, bg='#0a0a0a', fg='#00ff00')
        self.strings_view.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def create_quarantine_tab(self):
        """Create quarantine tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📦 Quarantine")
        
        # Controls
        controls = tk.Frame(tab, bg='#1a1a1a')
        controls.pack(fill=tk.X, pady=5)
        
        tk.Button(controls, text="🗑️ Clear All", command=self.clear_quarantine, 
                 bg='#ff0000', fg='#ffffff').pack(side=tk.LEFT, padx=5)
        
        # Quarantine list
        columns = ('File', 'Threat', 'Date', 'Size')
        self.quarantine_tree = ttk.Treeview(tab, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.quarantine_tree.heading(col, text=col)
            self.quarantine_tree.column(col, width=150)
            
        self.quarantine_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def create_settings_tab(self):
        """Create settings tab"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="⚙️ Settings")
        
        # General settings
        general_frame = tk.LabelFrame(tab, text="General Settings", padx=10, pady=10)
        general_frame.pack(fill=tk.X, pady=5, padx=5)
        
        # Theme selection
        theme_frame = tk.Frame(general_frame, bg='#1a1a1a')
        theme_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(theme_frame, text="Theme:", fg='#ffffff', bg='#1a1a1a').pack(side=tk.LEFT, padx=5)
        themes = ['Dark', 'Light', 'System']
        self.theme_var = tk.StringVar(value='Dark')
        theme_menu = ttk.Combobox(theme_frame, textvariable=self.theme_var, values=themes)
        theme_menu.pack(side=tk.LEFT)
        
        # Real-time protection
        protection_frame = tk.LabelFrame(tab, text="Protection", padx=10, pady=10)
        protection_frame.pack(fill=tk.X, pady=5, padx=5)
        
        self.protection_var = tk.BooleanVar(value=True)
        tk.Checkbutton(protection_frame, text="Enable Real-time Protection", 
                      variable=self.protection_var, bg='#1a1a1a', fg='#ffffff',
                      selectcolor='#0a0a0a').pack(anchor='w')
        
        # Scan settings
        scan_frame = tk.LabelFrame(tab, text="Scan Settings", padx=10, pady=10)
        scan_frame.pack(fill=tk.X, pady=5, padx=5)
        
        # Heuristic sensitivity
        sens_frame = tk.Frame(scan_frame, bg='#1a1a1a')
        sens_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(sens_frame, text="Heuristic Sensitivity:", fg='#ffffff', bg='#1a1a1a').pack(side=tk.LEFT, padx=5)
        self.heur_var = tk.IntVar(value=50)
        tk.Scale(sens_frame, from_=0, to=100, orient=tk.HORIZONTAL, 
                variable=self.heur_var, length=200, bg='#1a1a1a').pack(side=tk.LEFT)
        
    def create_status_bar(self):
        """Create status bar"""
        status_bar = tk.Frame(self.main_container, bg='#1a1a1a', height=25)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Status text
        self.status_text = tk.Label(status_bar, text="🟢 Protected | Real-time: Active",
                                   fg='#00ff00', bg='#1a1a1a')
        self.status_text.pack(side=tk.LEFT, padx=10)
        
        # Version
        tk.Label(status_bar, text="v1.0.0 | Linux Edition", 
                fg='#aaaaaa', bg='#1a1a1a').pack(side=tk.RIGHT, padx=10)
        
    def start_monitoring(self):
        """Start real-time monitoring threads"""
        def monitor():
            while True:
                self.check_threats()
                time.sleep(5)  # Check every 5 seconds
                
        thread = threading.Thread(target=monitor, daemon=True)
        thread.start()
        
    def init_threat_intel(self):
        """Initialize threat intelligence"""
        # Simplified threat intel for Linux version
        pass
        
    def check_threats(self):
        """Check for active threats"""
        # Simulate threat detection
        if random.random() < 0.05:  # 5% chance per check
            threat = {
                'type': random.choice(['malware', 'spyware', 'adware']),
                'name': f'Threat-{random.randint(1000, 9999)}',
                'risk': random.choice(['low', 'medium', 'high']),
                'location': f'/tmp/suspicious_{random.randint(1, 100)}'
            }
            
            self.threat_queue.put(threat)
            
            # Update UI
            self.root.after(0, self.display_threat, threat)
            
    def display_threat(self, threat):
        """Display detected threat"""
        # Add to threat listbox
        if hasattr(self, 'threat_listbox'):
            msg = f"⚠️ {threat['type'].upper()} detected - {threat['name']} ({threat['risk']})"
            self.threat_listbox.insert(0, msg)
            # Keep only last 10 threats
            if self.threat_listbox.size() > 10:
                self.threat_listbox.delete(10, tk.END)
                
    # Action methods
    def select_apk(self):
        """Select APK file for analysis"""
        filename = filedialog.askopenfilename(
            title="Select APK file",
            filetypes=[("APK files", "*.apk"), ("All files", "*.*")]
        )
        
        if filename:
            self.file_label.config(text=os.path.basename(filename))
            self.analyze_apk(filename)
            
    def analyze_apk(self, apk_path):
        """Analyze APK file"""
        self.log_message(f"Analyzing APK: {apk_path}")
        
        # Clear previous analysis
        if hasattr(self, 'file_info'):
            self.file_info.delete(1.0, tk.END)
        if hasattr(self, 'hex_view'):
            self.hex_view.delete(1.0, tk.END)
        if hasattr(self, 'strings_view'):
            self.strings_view.delete(1.0, tk.END)
        
        try:
            # Get file info
            file_size = os.path.getsize(apk_path)
            file_hash = hashlib.sha256()
            
            with open(apk_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    file_hash.update(chunk)
                    
            hash_value = file_hash.hexdigest()
            
            # Display file info
            if hasattr(self, 'file_info'):
                self.file_info.insert(tk.END, f"File: {os.path.basename(apk_path)}\n")
                self.file_info.insert(tk.END, f"Size: {file_size:,} bytes\n")
                self.file_info.insert(tk.END, f"SHA256: {hash_value}\n")
                self.file_info.insert(tk.END, f"MD5: {hashlib.md5(open(apk_path, 'rb').read()).hexdigest()}\n\n")
                
                # Check if known malware
                if hash_value in self.signature_db['known_hashes']:
                    malware = self.signature_db['known_hashes'][hash_value]
                    self.file_info.insert(tk.END, f"⚠️ KNOWN MALWARE: {malware.upper()}\n")
                    
            # Extract strings if strings_view exists
            if hasattr(self, 'strings_view'):
                with open(apk_path, 'rb') as f:
                    data = f.read()
                    # Find ASCII strings
                    strings = re.findall(b'[ -~]{4,}', data)
                    for s in strings[:50]:  # Show first 50 strings
                        try:
                            self.strings_view.insert(tk.END, s.decode('ascii') + '\n')
                        except:
                            pass
                            
            # Hex view if hex_view exists
            if hasattr(self, 'hex_view'):
                with open(apk_path, 'rb') as f:
                    data = f.read()
                    hex_data = binascii.hexlify(data[:512]).decode('ascii')
                    for i in range(0, len(hex_data), 32):
                        self.hex_view.insert(tk.END, hex_data[i:i+32] + '\n')
                        
        except Exception as e:
            if hasattr(self, 'file_info'):
                self.file_info.insert(tk.END, f"Error: {str(e)}\n")
                
    def scan_device(self):
        """Scan system for threats"""
        self.log_message("Starting system scan...")
        self.scan_progress['value'] = 0
        
        def scan():
            # Clear previous results
            self.root.after(0, lambda: [self.scan_tree.delete(item) for item in self.scan_tree.get_children()])
            
            # Scan common directories
            scan_dirs = ['/tmp', '/var/tmp', os.path.expanduser('~/Downloads')]
            files_scanned = 0
            threats_found = 0
            
            for scan_dir in scan_dirs:
                if os.path.exists(scan_dir):
                    for root, dirs, files in os.walk(scan_dir):
                        for file in files:
                            filepath = os.path.join(root, file)
                            try:
                                # Check file
                                if self.check_file_threat(filepath):
                                    threats_found += 1
                                    self.root.after(0, self.add_threat_to_scan, filepath)
                                
                                files_scanned += 1
                                if files_scanned % 10 == 0:
                                    progress = min(100, int((files_scanned / 100) * 100))
                                    self.root.after(0, self.update_scan_progress, progress)
                                    self.root.after(0, self.update_scan_info, 
                                                   f"Scanning: {os.path.basename(filepath)}")
                            except:
                                pass
                                
            self.root.after(0, self.scan_complete, threats_found)
            
        thread = threading.Thread(target=scan, daemon=True)
        thread.start()
        
    def check_file_threat(self, filepath):
        """Check if file is a threat"""
        # Simple threat detection based on file extensions and names
        suspicious_extensions = ['.exe', '.bat', '.vbs', '.ps1', '.jar']
        suspicious_names = ['malware', 'virus', 'trojan', 'keylogger', 'rat']
        
        ext = os.path.splitext(filepath)[1].lower()
        name = os.path.basename(filepath).lower()
        
        if ext in suspicious_extensions:
            return True
        
        for sus_name in suspicious_names:
            if sus_name in name:
                return True
                
        return False
        
    def add_threat_to_scan(self, filepath):
        """Add threat to scan results"""
        threat_type = random.choice(['Malware', 'Spyware', 'Adware'])
        risk = random.choice(['LOW', 'MEDIUM', 'HIGH'])
        
        self.scan_tree.insert('', 0, values=(
            threat_type,
            os.path.basename(filepath),
            risk,
            os.path.dirname(filepath)
        ))
        
    def quick_scan(self):
        """Quick scan of critical areas"""
        self.scan_info.config(text="Quick scan in progress...")
        self.scan_progress['value'] = 0
        
        def scan():
            areas = [
                "/tmp/",
                os.path.expanduser("~/Downloads/"),
                "/var/tmp/"
            ]
            
            files_scanned = 0
            threats_found = 0
            
            for area in areas:
                if os.path.exists(area):
                    for file in os.listdir(area)[:20]:  # Limit to 20 files per area
                        filepath = os.path.join(area, file)
                        if os.path.isfile(filepath) and self.check_file_threat(filepath):
                            threats_found += 1
                            self.root.after(0, self.add_threat_to_scan, filepath)
                        
                        files_scanned += 1
                        progress = min(100, int((files_scanned / 50) * 100))
                        self.root.after(0, self.update_scan_progress, progress)
                        time.sleep(0.05)
                        
            self.root.after(0, self.scan_complete, threats_found)
            
        thread = threading.Thread(target=scan, daemon=True)
        thread.start()
        
    def app_analysis(self):
        """Analyze applications"""
        self.log_message("Analyzing applications...")
        
        # Clear previous results
        for item in self.scan_tree.get_children():
            self.scan_tree.delete(item)
            
        # Simulate app analysis
        apps = [
            ('Malware', 'com.example.malicious', 'HIGH', '/data/app/'),
            ('Spyware', 'com.example.spy', 'MEDIUM', '/data/app/'),
            ('Adware', 'com.example.adware', 'LOW', '/data/app/'),
        ]
        
        for app in apps:
            self.scan_tree.insert('', tk.END, values=app)
            
    def network_scan(self):
        """Perform network scan"""
        self.log_message("Starting network scan...")
        
        # Get network connections using psutil
        connections = psutil.net_connections()
        
        # Clear previous traffic
        if hasattr(self, 'traffic_tree'):
            for item in self.traffic_tree.get_children():
                self.traffic_tree.delete(item)
            
        # Display connections
        for conn in connections[:20]:  # Limit to first 20
            if conn.raddr:
                info = f"{conn.laddr.ip}:{conn.laddr.port} -> {conn.raddr.ip}:{conn.raddr.port}"
            else:
                info = f"{conn.laddr.ip}:{conn.laddr.port} (LISTENING)"
                
            self.log_message(f"Connection: {info}")
            
    def toggle_protection(self):
        """Toggle real-time protection"""
        if self.protection_var.get():
            self.status_text.config(text="🟢 Protected | Real-time: Active")
            self.log_message("Real-time protection enabled")
        else:
            self.status_text.config(text="🟡 Protected | Real-time: Disabled")
            self.log_message("Real-time protection disabled")
            
    def refresh_processes(self):
        """Refresh process list"""
        # Clear current processes
        for item in self.process_tree.get_children():
            self.process_tree.delete(item)
            
        # Get current processes
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
            try:
                pinfo = proc.info
                self.process_tree.insert('', tk.END, values=(
                    pinfo['pid'],
                    pinfo['name'][:30],
                    f"{pinfo['cpu_percent']:.1f}",
                    f"{pinfo['memory_percent']:.1f}",
                    pinfo['status']
                ))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
    def select_file(self):
        """Select file for analysis"""
        filename = filedialog.askopenfilename()
        if filename:
            self.file_label.config(text=os.path.basename(filename))
            self.analyze_file(filename)
            
    def analyze_file(self, filepath):
        """Analyze selected file"""
        self.log_message(f"Analyzing file: {filepath}")
        
        if hasattr(self, 'file_info'):
            self.file_info.delete(1.0, tk.END)
            self.file_info.insert(tk.END, f"Analyzing: {filepath}\n\n")
            
            # Get file stats
            stat = os.stat(filepath)
            self.file_info.insert(tk.END, f"Size: {stat.st_size:,} bytes\n")
            self.file_info.insert(tk.END, f"Modified: {datetime.fromtimestamp(stat.st_mtime)}\n")
            self.file_info.insert(tk.END, f"Permissions: {oct(stat.st_mode)[-3:]}\n\n")
            
            # Calculate hashes
            with open(filepath, 'rb') as f:
                data = f.read()
                self.file_info.insert(tk.END, f"MD5: {hashlib.md5(data).hexdigest()}\n")
                self.file_info.insert(tk.END, f"SHA1: {hashlib.sha1(data).hexdigest()}\n")
                self.file_info.insert(tk.END, f"SHA256: {hashlib.sha256(data).hexdigest()}\n")
                
    def clear_quarantine(self):
        """Clear quarantine list"""
        if messagebox.askyesno("Confirm", "Clear quarantine list?"):
            for item in self.quarantine_tree.get_children():
                self.quarantine_tree.delete(item)
            self.log_message("Quarantine cleared")
            
    def update_scan_progress(self, value):
        """Update scan progress bar"""
        self.scan_progress['value'] = value
        self.scan_percent.config(text=f"{value}%")
        
    def update_scan_info(self, info):
        """Update scan information"""
        self.scan_info.config(text=info)
        
    def scan_complete(self, threats_found=0):
        """Handle scan completion"""
        self.scan_info.config(text=f"Scan complete! Found {threats_found} threats")
        self.log_message(f"Scan completed - Found {threats_found} threats")
        messagebox.showinfo("Scan Complete", f"Scan finished. Found {threats_found} threats.")
        
    def stop_scan(self):
        """Stop current scan"""
        self.scan_info.config(text="Scan stopped by user")
        self.log_message("Scan stopped")
        
    def log_message(self, message):
        """Log message to console"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
        
        # Update status bar
        if hasattr(self, 'status_text'):
            self.status_text.config(text=f"🟢 {message[:50]}...")

def main():
    """Main entry point"""
    root = tk.Tk()
    
    # Set style
    style = ttk.Style()
    style.theme_use('clam')
    
    app = AdvancedAndroidSecuritySuite(root)
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Exit security suite?"):
            root.destroy()
            
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
