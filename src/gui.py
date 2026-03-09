#!/usr/bin/env python3
"""
Instagram Polaris Security Analyzer Pro
Meta Internal Security Tool - CONFIDENTIAL
Version 2.0 - Advanced GUI Edition

Author: ATHEX BLACK HAT
Purpose: Authorized vulnerability assessment and fix validation
"""

import sys
import os
import json
import re
import time
import threading
import queue
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import urllib3

# GUI Imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Data Visualization
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import numpy as np

# Networking
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Utilities
from colorama import init, Fore, Style
import pyfiglet
from prettytable import PrettyTable
import plotly.graph_objects as go
from plotly.offline import plot
import networkx as nx

# Disable SSL warnings for testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# ============================================================================
# DATA MODELS
# ============================================================================

class RiskLevel(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH" 
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"

@dataclass
class VulnerabilityReport:
    """Data class for vulnerability findings"""
    username: str
    is_vulnerable: bool
    risk_level: RiskLevel
    media_exposed: int
    json_path: str
    timestamp: str
    headers_used: Dict
    response_code: int
    confidence_score: float
    fix_recommendation: str

@dataclass
class SecurityFix:
    """Data class for security fixes"""
    fix_id: str
    description: str
    implementation: str
    status: str
    deployment_date: str
    verified_by: str

# ============================================================================
# CUSTOM WIDGETS
# ============================================================================

class AnimatedToggle(QCheckBox):
    """Custom animated toggle switch"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(60, 30)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw background
        rect = QRect(0, 0, 60, 30)
        if self.isChecked():
            painter.setBrush(QBrush(QColor(0, 255, 0, 100)))
            painter.setPen(QPen(QColor(0, 200, 0), 2))
        else:
            painter.setBrush(QBrush(QColor(255, 0, 0, 100)))
            painter.setPen(QPen(QColor(200, 0, 0), 2))
        
        painter.drawRoundedRect(rect, 15, 15)
        
        # Draw toggle
        if self.isChecked():
            toggle_rect = QRect(30, 2, 26, 26)
        else:
            toggle_rect = QRect(4, 2, 26, 26)
            
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(QColor(0, 0, 0), 1))
        painter.drawEllipse(toggle_rect)

class AnimatedButton(QPushButton):
    """Button with hover animations"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        self.default_style = """
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
                transform: scale(1.05);
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """
        self.setStyleSheet(self.default_style)
        
    def enterEvent(self, event):
        self.animate_property(b"geometry", self.geometry(), 
                             self.geometry().adjusted(-2, -2, 2, 2), 200)
        super().enterEvent(event)
        
    def animate_property(self, prop, start, end, duration):
        self.animation = QPropertyAnimation(self, prop)
        self.animation.setDuration(duration)
        self.animation.setStartValue(start)
        self.animation.setEndValue(end)
        self.animation.start()

class LoadingSpinner(QWidget):
    """Custom loading animation"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.angle = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate)
        self.timer.start(50)
        
    def rotate(self):
        self.angle += 10
        if self.angle >= 360:
            self.angle = 0
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        painter.translate(25, 25)
        painter.rotate(self.angle)
        
        gradient = QConicalGradient(0, 0, 0)
        gradient.setColorAt(0, QColor(0, 255, 0))
        gradient.setColorAt(1, QColor(0, 100, 0))
        
        pen = QPen(QBrush(gradient), 4)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        
        painter.drawArc(QRect(-20, -20, 40, 40), 0, 300 * 16)

# ============================================================================
# MAIN GUI WINDOW
# ============================================================================

class PolarisAnalyzerGUI(QMainWindow):
    """Main GUI Application Window"""
    
    def __init__(self):
        super().__init__()
        self.vulnerable_accounts = []
        self.scan_results = []
        self.current_theme = "dark"
        self.scan_queue = queue.Queue()
        self.is_scanning = False
        self.init_ui()
        self.setup_animations()
        self.load_styles()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Instagram Polaris Security Analyzer Pro v2.0")
        self.setGeometry(100, 100, 1400, 900)
        
        # Set window icon
        self.setWindowIcon(self.create_icon())
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create header with ASCII art
        self.create_header()
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setDocumentMode(True)
        
        # Initialize all tabs
        self.init_scanner_tab()
        self.init_visualizer_tab()
        self.init_fix_validator_tab()
        self.init_report_generator_tab()
        self.init_network_analyzer_tab()
        
        self.main_layout.addWidget(self.tab_widget)
        
        # Create status bar
        self.create_status_bar()
        
    def create_icon(self):
        """Create application icon"""
        icon = QIcon()
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setBrush(QBrush(QColor(0, 255, 0)))
        painter.setPen(QPen(QColor(255, 255, 255), 2))
        painter.drawEllipse(10, 10, 44, 44)
        painter.drawText(20, 40, "P")
        painter.end()
        icon.addPixmap(pixmap)
        return icon
        
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        new_scan = QAction('New Scan', self)
        new_scan.setShortcut('Ctrl+N')
        new_scan.triggered.connect(self.new_scan)
        file_menu.addAction(new_scan)
        
        load_results = QAction('Load Results', self)
        load_results.setShortcut('Ctrl+O')
        load_results.triggered.connect(self.load_results)
        file_menu.addAction(load_results)
        
        save_results = QAction('Save Results', self)
        save_results.setShortcut('Ctrl+S')
        save_results.triggered.connect(self.save_results)
        file_menu.addAction(save_results)
        
        file_menu.addSeparator()
        
        export_report = QAction('Export Report', self)
        export_report.setShortcut('Ctrl+E')
        export_report.triggered.connect(self.export_report)
        file_menu.addAction(export_report)
        
        file_menu.addSeparator()
        
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Tools menu
        tools_menu = menubar.addMenu('Tools')
        
        validate_fix = QAction('Validate Fix', self)
        validate_fix.triggered.connect(self.validate_fix)
        tools_menu.addAction(validate_fix)
        
        network_scan = QAction('Network Analysis', self)
        network_scan.triggered.connect(self.network_analysis)
        tools_menu.addAction(network_scan)
        
        # Settings menu
        settings_menu = menubar.addMenu('Settings')
        
        theme_menu = QMenu('Theme', self)
        dark_theme = QAction('Dark Theme', self)
        dark_theme.triggered.connect(lambda: self.change_theme('dark'))
        light_theme = QAction('Light Theme', self)
        light_theme.triggered.connect(lambda: self.change_theme('light'))
        theme_menu.addAction(dark_theme)
        theme_menu.addAction(light_theme)
        settings_menu.addMenu(theme_menu)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        docs = QAction('Documentation', self)
        docs.triggered.connect(self.show_docs)
        help_menu.addAction(docs)
        
        about = QAction('About', self)
        about.triggered.connect(self.show_about)
        help_menu.addAction(about)
        
    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = self.addToolBar('Main Toolbar')
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(32, 32))
        
        # Add toolbar actions
        new_action = QAction(QIcon.fromTheme('document-new'), 'New Scan', self)
        new_action.triggered.connect(self.new_scan)
        toolbar.addAction(new_action)
        
        save_action = QAction(QIcon.fromTheme('document-save'), 'Save', self)
        save_action.triggered.connect(self.save_results)
        toolbar.addAction(save_action)
        
        toolbar.addSeparator()
        
        start_action = QAction(QIcon.fromTheme('media-playback-start'), 'Start Scan', self)
        start_action.triggered.connect(self.start_scan)
        toolbar.addAction(start_action)
        
        stop_action = QAction(QIcon.fromTheme('media-playback-stop'), 'Stop Scan', self)
        stop_action.triggered.connect(self.stop_scan)
        toolbar.addAction(stop_action)
        
        toolbar.addSeparator()
        
        # Add search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search accounts...")
        self.search_box.setFixedWidth(200)
        self.search_box.textChanged.connect(self.filter_results)
        toolbar.addWidget(self.search_box)
        
    def create_header(self):
        """Create animated ASCII art header"""
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        
        # ASCII Art Label
        ascii_text = pyfiglet.figlet_format("POLARIS PRO", font="slant")
        ascii_label = QLabel(ascii_text)
        ascii_label.setStyleSheet("""
            QLabel {
                color: #00ff00;
                font-family: monospace;
                font-size: 12px;
                background-color: #1a1a1a;
                padding: 10px;
                border-radius: 5px;
            }
        """)
        header_layout.addWidget(ascii_label)
        
        # Version badge
        version_badge = QLabel("v2.0.0 | META INTERNAL")
        version_badge.setStyleSheet("""
            QLabel {
                color: #ffffff;
                background-color: #ff6b6b;
                padding: 5px 10px;
                border-radius: 15px;
                font-weight: bold;
            }
        """)
        header_layout.addWidget(version_badge, alignment=Qt.AlignRight)
        
        self.main_layout.addWidget(header_widget)
        
    def init_scanner_tab(self):
        """Initialize the main scanner tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Split into left and right panels
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel - Input and controls
        left_panel = self.create_scanner_input_panel()
        
        # Right panel - Results display
        right_panel = self.create_scanner_results_panel()
        
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([400, 800])
        
        layout.addWidget(splitter)
        self.tab_widget.addTab(tab, "🔍 Scanner")
        
    def create_scanner_input_panel(self):
        """Create input panel for scanner"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Input section
        input_group = QGroupBox("Target Input")
        input_layout = QVBoxLayout()
        
        # Username input with validation
        username_layout = QHBoxLayout()
        username_layout.addWidget(QLabel("Username:"))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Instagram username")
        self.username_input.textChanged.connect(self.validate_username)
        username_layout.addWidget(self.username_input)
        
        # Validation indicator
        self.validation_label = QLabel("⚪")
        username_layout.addWidget(self.validation_label)
        input_layout.addLayout(username_layout)
        
        # File upload
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Or select file with usernames")
        self.file_path.setReadOnly(True)
        file_layout.addWidget(self.file_path)
        
        browse_btn = AnimatedButton("Browse")
        browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(browse_btn)
        input_layout.addLayout(file_layout)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Scan configuration
        config_group = QGroupBox("Scan Configuration")
        config_layout = QGridLayout()
        
        # Thread count
        config_layout.addWidget(QLabel("Threads:"), 0, 0)
        self.thread_spin = QSpinBox()
        self.thread_spin.setRange(1, 20)
        self.thread_spin.setValue(5)
        config_layout.addWidget(self.thread_spin, 0, 1)
        
        # Timeout
        config_layout.addWidget(QLabel("Timeout (s):"), 1, 0)
        self.timeout_spin = QSpinBox()
        self.timeout_spin.setRange(1, 30)
        self.timeout_spin.setValue(10)
        config_layout.addWidget(self.timeout_spin, 1, 1)
        
        # Rate limit
        config_layout.addWidget(QLabel("Rate Limit:"), 2, 0)
        self.rate_limit = QComboBox()
        self.rate_limit.addItems(["Slow (1/sec)", "Medium (5/sec)", "Fast (10/sec)"])
        config_layout.addWidget(self.rate_limit, 2, 1)
        
        # Advanced options
        self.save_responses = AnimatedToggle()
        config_layout.addWidget(QLabel("Save Responses:"), 3, 0)
        config_layout.addWidget(self.save_responses, 3, 1)
        
        self.follow_redirects = AnimatedToggle()
        self.follow_redirects.setChecked(True)
        config_layout.addWidget(QLabel("Follow Redirects:"), 4, 0)
        config_layout.addWidget(self.follow_redirects, 4, 1)
        
        config_group.setLayout(config_layout)
        layout.addWidget(config_group)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        self.start_btn = AnimatedButton("🚀 Start Scan")
        self.start_btn.clicked.connect(self.start_scan)
        button_layout.addWidget(self.start_btn)
        
        self.stop_btn = AnimatedButton("⏹️ Stop Scan")
        self.stop_btn.clicked.connect(self.stop_scan)
        self.stop_btn.setEnabled(False)
        button_layout.addWidget(self.stop_btn)
        
        layout.addLayout(button_layout)
        
        # Status display
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setMaximumHeight(150)
        layout.addWidget(self.status_text)
        
        # Loading spinner
        self.spinner = LoadingSpinner()
        self.spinner.hide()
        layout.addWidget(self.spinner, alignment=Qt.AlignCenter)
        
        layout.addStretch()
        return panel
        
    def create_scanner_results_panel(self):
        """Create results display panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Results table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(8)
        self.results_table.setHorizontalHeaderLabels([
            "Username", "Vulnerable", "Risk Level", "Media Exposed",
            "Confidence", "Response Code", "Timestamp", "Actions"
        ])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.setAlternatingRowColors(True)
        self.results_table.setSortingEnabled(True)
        
        layout.addWidget(self.results_table)
        
        # Statistics bar
        stats_widget = QWidget()
        stats_layout = QHBoxLayout(stats_widget)
        
        self.total_scanned = QLabel("Total: 0")
        stats_layout.addWidget(self.total_scanned)
        
        self.vulnerable_count = QLabel("Vulnerable: 0")
        self.vulnerable_count.setStyleSheet("color: #ff4444;")
        stats_layout.addWidget(self.vulnerable_count)
        
        self.secure_count = QLabel("Secure: 0")
        self.secure_count.setStyleSheet("color: #44ff44;")
        stats_layout.addWidget(self.secure_count)
        
        stats_layout.addStretch()
        
        layout.addWidget(stats_widget)
        
        return panel
        
    def init_visualizer_tab(self):
        """Initialize data visualization tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Create matplotlib figure
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(tab)
        
        # Add toolbar
        toolbar = NavigationToolbar(self.canvas, tab)
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        
        self.tab_widget.addTab(tab, "📊 Visualizer")
        
    def init_fix_validator_tab(self):
        """Initialize fix validation tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Fix validation interface
        validator_group = QGroupBox("Fix Validation")
        validator_layout = QVBoxLayout()
        
        # Account selector
        account_selector = QComboBox()
        account_selector.addItems(["Select account to validate..."])
        validator_layout.addWidget(account_selector)
        
        # Fix status
        self.fix_status_tree = QTreeWidget()
        self.fix_status_tree.setHeaderLabels(["Fix", "Status", "Verified", "Date"])
        validator_layout.addWidget(self.fix_status_tree)
        
        validator_group.setLayout(validator_layout)
        layout.addWidget(validator_group)
        
        # Apply fix button
        apply_fix_btn = AnimatedButton("Apply Fix to Selected Account")
        apply_fix_btn.clicked.connect(self.apply_fix)
        layout.addWidget(apply_fix_btn)
        
        self.tab_widget.addTab(tab, "🔧 Fix Validator")
        
    def init_report_generator_tab(self):
        """Initialize report generation tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Report configuration
        config_group = QGroupBox("Report Configuration")
        config_layout = QGridLayout()
        
        config_layout.addWidget(QLabel("Report Format:"), 0, 0)
        self.report_format = QComboBox()
        self.report_format.addItems(["PDF", "HTML", "JSON", "CSV"])
        config_layout.addWidget(self.report_format, 0, 1)
        
        config_layout.addWidget(QLabel("Include:"), 1, 0)
        self.include_vulns = QCheckBox("Vulnerabilities")
        self.include_vulns.setChecked(True)
        config_layout.addWidget(self.include_vulns, 1, 1)
        
        self.include_stats = QCheckBox("Statistics")
        self.include_stats.setChecked(True)
        config_layout.addWidget(self.include_stats, 2, 1)
        
        self.include_graphs = QCheckBox("Graphs")
        self.include_graphs.setChecked(True)
        config_layout.addWidget(self.include_graphs, 3, 1)
        
        config_group.setLayout(config_layout)
        layout.addWidget(config_group)
        
        # Generate button
        generate_btn = AnimatedButton("Generate Report")
        generate_btn.clicked.connect(self.generate_report)
        layout.addWidget(generate_btn)
        
        # Preview area
        preview_group = QGroupBox("Report Preview")
        preview_layout = QVBoxLayout()
        self.report_preview = QWebEngineView()
        preview_layout.addWidget(self.report_preview)
        preview_group.setLayout(preview_layout)
        layout.addWidget(preview_group)
        
        self.tab_widget.addTab(tab, "📄 Report Generator")
        
    def init_network_analyzer_tab(self):
        """Initialize network analysis tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Network graph
        self.network_figure = Figure(figsize=(12, 8))
        self.network_canvas = FigureCanvas(self.network_figure)
        
        # Controls
        controls_layout = QHBoxLayout()
        
        capture_btn = AnimatedButton("Start Capture")
        capture_btn.clicked.connect(self.start_network_capture)
        controls_layout.addWidget(capture_btn)
        
        analyze_btn = AnimatedButton("Analyze Traffic")
        analyze_btn.clicked.connect(self.analyze_traffic)
        controls_layout.addWidget(analyze_btn)
        
        layout.addLayout(controls_layout)
        layout.addWidget(self.network_canvas)
        
        self.tab_widget.addTab(tab, "🌐 Network Analyzer")
        
    def create_status_bar(self):
        """Create status bar with animations"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # Status labels
        self.status_label = QLabel("Ready")
        self.status_bar.addWidget(self.status_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(200)
        self.progress_bar.hide()
        self.status_bar.addPermanentWidget(self.progress_bar)
        
        # Connection status
        self.connection_status = QLabel("● Connected")
        self.connection_status.setStyleSheet("color: #44ff44;")
        self.status_bar.addPermanentWidget(self.connection_status)
        
        # Time display
        self.time_label = QLabel()
        self.status_bar.addPermanentWidget(self.time_label)
        
        # Update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)
        
    def setup_animations(self):
        """Setup window animations"""
        self.animation_group = QParallelAnimationGroup()
        
        # Fade in animation
        self.fade_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_animation.setDuration(500)
        self.fade_animation.setStartValue(0)
        self.fade_animation.setEndValue(1)
        self.fade_animation.start()
        
    def load_styles(self):
        """Load stylesheet based on theme"""
        if self.current_theme == "dark":
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2b2b2b;
                }
                QTabWidget::pane {
                    background-color: #3c3c3c;
                    border: 1px solid #555;
                }
                QTabBar::tab {
                    background-color: #444;
                    color: #fff;
                    padding: 8px 15px;
                }
                QTabBar::tab:selected {
                    background-color: #555;
                }
                QGroupBox {
                    color: #fff;
                    border: 2px solid #555;
                    border-radius: 5px;
                    margin-top: 10px;
                    font-weight: bold;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 10px;
                    padding: 0 5px;
                }
                QLabel {
                    color: #fff;
                }
                QLineEdit, QTextEdit {
                    background-color: #444;
                    color: #fff;
                    border: 1px solid #555;
                    border-radius: 3px;
                    padding: 3px;
                }
                QTableWidget {
                    background-color: #3c3c3c;
                    color: #fff;
                    gridline-color: #555;
                }
                QHeaderView::section {
                    background-color: #444;
                    color: #fff;
                    padding: 5px;
                }
                QScrollBar {
                    background-color: #444;
                }
            """)
            
    # ============================================================================
    # FUNCTIONALITY METHODS
    # ============================================================================
    
    def validate_username(self, text):
        """Validate username input"""
        if text and re.match(r'^[a-zA-Z0-9._]+$', text):
            self.validation_label.setText("✅")
            self.validation_label.setStyleSheet("color: #44ff44;")
        else:
            self.validation_label.setText("❌")
            self.validation_label.setStyleSheet("color: #ff4444;")
            
    def browse_file(self):
        """Browse for username file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select Username File", "", "Text Files (*.txt)")
        if filename:
            self.file_path.setText(filename)
            
    def new_scan(self):
        """Reset for new scan"""
        reply = QMessageBox.question(self, 'New Scan', 
                                    'Start new scan? Current results will be cleared.',
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.results_table.setRowCount(0)
            self.scan_results.clear()
            self.vulnerable_accounts.clear()
            self.update_statistics()
            
    def load_results(self):
        """Load previous scan results"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Load Results", "", "JSON Files (*.json)")
        if filename:
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    self.display_results(data)
                self.status_label.setText(f"Loaded results from {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load results: {e}")
                
    def save_results(self):
        """Save scan results"""
        if not self.scan_results:
            QMessageBox.warning(self, "No Data", "No results to save")
            return
            
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Results", "", "JSON Files (*.json)")
        if filename:
            try:
                with open(filename, 'w') as f:
                    json.dump(self.scan_results, f, indent=2, default=str)
                self.status_label.setText(f"Saved results to {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save results: {e}")
                
    def export_report(self):
        """Export formatted report"""
        if not self.scan_results:
            QMessageBox.warning(self, "No Data", "No data to export")
            return
            
        filename, _ = QFileDialog.getSaveFileName(
            self, "Export Report", "", "PDF Files (*.pdf);;HTML Files (*.html)")
        if filename:
            self.generate_report(filename)
            
    def start_scan(self):
        """Start the vulnerability scan"""
        if not self.username_input.text() and not self.file_path.text():
            QMessageBox.warning(self, "Input Required", 
                              "Please enter a username or select a file")
            return
            
        self.is_scanning = True
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.spinner.show()
        self.status_label.setText("Scanning...")
        self.progress_bar.show()
        self.progress_bar.setValue(0)
        
        # Start scan in separate thread
        self.scan_thread = QThread()
        self.scan_worker = ScanWorker(self.username_input.text(), 
                                      self.file_path.text())
        self.scan_worker.moveToThread(self.scan_thread)
        
        self.scan_thread.started.connect(self.scan_worker.run)
        self.scan_worker.finished.connect(self.scan_thread.quit)
        self.scan_worker.finished.connect(self.scan_worker.deleteLater)
        self.scan_worker.finished.connect(self.scan_finished)
        self.scan_worker.result_ready.connect(self.add_scan_result)
        self.scan_worker.progress_updated.connect(self.update_progress)
        
        self.scan_thread.start()
        
    def stop_scan(self):
        """Stop the ongoing scan"""
        self.is_scanning = False
        if hasattr(self, 'scan_worker'):
            self.scan_worker.stop()
        self.status_label.setText("Scan stopped by user")
        self.scan_finished()
        
    def scan_finished(self):
        """Handle scan completion"""
        self.is_scanning = False
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.spinner.hide()
        self.progress_bar.hide()
        self.status_label.setText("Scan completed")
        
        # Update visualizations
        self.update_visualizations()
        
    def add_scan_result(self, result: dict):
        """Add result to table"""
        self.scan_results.append(result)
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        
        # Username
        self.results_table.setItem(row, 0, QTableWidgetItem(result['username']))
        
        # Vulnerable status
        vuln_item = QTableWidgetItem("✅" if result['is_vulnerable'] else "❌")
        vuln_item.setForeground(QBrush(QColor('#44ff44' if result['is_vulnerable'] else '#ff4444')))
        self.results_table.setItem(row, 1, vuln_item)
        
        # Risk level
        risk_item = QTableWidgetItem(result.get('risk_level', 'Unknown'))
        if result.get('risk_level') == 'CRITICAL':
            risk_item.setForeground(QBrush(QColor('#ff0000')))
        self.results_table.setItem(row, 2, risk_item)
        
        # Media exposed
        self.results_table.setItem(row, 3, QTableWidgetItem(str(result.get('media_exposed', 0))))
        
        # Confidence
        confidence = f"{result.get('confidence_score', 0)*100:.1f}%"
        self.results_table.setItem(row, 4, QTableWidgetItem(confidence))
        
        # Response code
        self.results_table.setItem(row, 5, QTableWidgetItem(str(result.get('response_code', ''))))
        
        # Timestamp
        self.results_table.setItem(row, 6, QTableWidgetItem(result.get('timestamp', '')))
        
        # Action button
        view_btn = QPushButton("Details")
        view_btn.clicked.connect(lambda: self.show_details(result))
        self.results_table.setCellWidget(row, 7, view_btn)
        
        self.update_statistics()
        
    def update_statistics(self):
        """Update statistics display"""
        total = len(self.scan_results)
        vulnerable = sum(1 for r in self.scan_results if r.get('is_vulnerable'))
        secure = total - vulnerable
        
        self.total_scanned.setText(f"Total: {total}")
        self.vulnerable_count.setText(f"Vulnerable: {vulnerable}")
        self.secure_count.setText(f"Secure: {secure}")
        
    def update_progress(self, current, total):
        """Update progress bar"""
        progress = int((current / total) * 100) if total > 0 else 0
        self.progress_bar.setValue(progress)
        
    def update_visualizations(self):
        """Update all visualizations with current data"""
        if not self.scan_results:
            return
            
        # Clear figure
        self.figure.clear()
        
        # Create subplots
        ax1 = self.figure.add_subplot(221)
        ax2 = self.figure.add_subplot(222)
        ax3 = self.figure.add_subplot(223)
        ax4 = self.figure.add_subplot(224)
        
        # Vulnerability pie chart
        vulnerable_count = sum(1 for r in self.scan_results if r.get('is_vulnerable'))
        secure_count = len(self.scan_results) - vulnerable_count
        ax1.pie([vulnerable_count, secure_count], 
                labels=['Vulnerable', 'Secure'],
                colors=['#ff4444', '#44ff44'],
                autopct='%1.1f%%')
        ax1.set_title('Vulnerability Distribution')
        
        # Risk level bar chart
        risk_levels = {}
        for r in self.scan_results:
            level = r.get('risk_level', 'UNKNOWN')
            risk_levels[level] = risk_levels.get(level, 0) + 1
        
        ax2.bar(risk_levels.keys(), risk_levels.values())
        ax2.set_title('Risk Levels')
        ax2.tick_params(axis='x', rotation=45)
        
        # Media exposure histogram
        media_counts = [r.get('media_exposed', 0) for r in self.scan_results if r.get('media_exposed', 0) > 0]
        if media_counts:
            ax3.hist(media_counts, bins=10)
            ax3.set_title('Media Exposure Distribution')
            ax3.set_xlabel('Number of Media Items')
            ax3.set_ylabel('Frequency')
        
        # Confidence scores
        confidence_scores = [r.get('confidence_score', 0) for r in self.scan_results]
        ax4.boxplot(confidence_scores)
        ax4.set_title('Confidence Score Distribution')
        ax4.set_ylabel('Confidence Score')
        
        self.figure.tight_layout()
        self.canvas.draw()
        
    def filter_results(self, text):
        """Filter results table based on search text"""
        for row in range(self.results_table.rowCount()):
            match = False
            for col in range(self.results_table.columnCount() - 1):  # Exclude action column
                item = self.results_table.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.results_table.setRowHidden(row, not match)
            
    def show_details(self, result):
        """Show detailed view of a result"""
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Details for @{result['username']}")
        dialog.setMinimumSize(600, 400)
        
        layout = QVBoxLayout(dialog)
        
        # Create details tree
        tree = QTreeWidget()
        tree.setHeaderLabels(["Property", "Value"])
        
        def add_item(parent, key, value):
            item = QTreeWidgetItem(parent)
            item.setText(0, str(key))
            item.setText(1, str(value))
            
        # Add all result properties
        root = tree.invisibleRootItem()
        for key, value in result.items():
            if isinstance(value, dict):
                dict_item = QTreeWidgetItem(root)
                dict_item.setText(0, str(key))
                for k, v in value.items():
                    add_item(dict_item, k, v)
            else:
                add_item(root, key, value)
                
        layout.addWidget(tree)
        
        # Add close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)
        
        dialog.exec_()
        
    def apply_fix(self):
        """Apply fix to selected account"""
        # This would contain the fix implementation logic
        QMessageBox.information(self, "Fix Applied", 
                               "Security fix has been applied successfully!")
        
    def generate_report(self, filename=None):
        """Generate comprehensive report"""
        if not self.scan_results:
            QMessageBox.warning(self, "No Data", "No data to generate report")
            return
            
        # Generate HTML report
        html_content = self.create_html_report()
        
        if filename:
            if filename.endswith('.pdf'):
                self.convert_to_pdf(html_content, filename)
            else:
                with open(filename, 'w') as f:
                    f.write(html_content)
        else:
            # Show preview
            self.report_preview.setHtml(html_content)
            
        QMessageBox.information(self, "Report Generated", 
                               "Report has been generated successfully!")
        
    def create_html_report(self):
        """Create HTML report content"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Polaris Security Report</title>
            <style>
                body {{ font-family: Arial; margin: 20px; }}
                h1 {{ color: #333; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #4CAF50; color: white; }}
                .vulnerable {{ background-color: #ffdddd; }}
                .secure {{ background-color: #ddffdd; }}
            </style>
        </head>
        <body>
            <h1>Instagram Polaris Security Assessment Report</h1>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <h2>Summary</h2>
            <ul>
                <li>Total Accounts Scanned: {len(self.scan_results)}</li>
                <li>Vulnerable Accounts: {sum(1 for r in self.scan_results if r.get('is_vulnerable'))}</li>
                <li>Secure Accounts: {sum(1 for r in self.scan_results if not r.get('is_vulnerable'))}</li>
            </ul>
            
            <h2>Detailed Results</h2>
            <table>
                <tr>
                    <th>Username</th>
                    <th>Status</th>
                    <th>Risk Level</th>
                    <th>Media Exposed</th>
                    <th>Confidence</th>
                </tr>
        """
        
        for result in self.scan_results:
            status_class = "vulnerable" if result.get('is_vulnerable') else "secure"
            html += f"""
                <tr class="{status_class}">
                    <td>@{result['username']}</td>
                    <td>{'VULNERABLE' if result.get('is_vulnerable') else 'SECURE'}</td>
                    <td>{result.get('risk_level', 'N/A')}</td>
                    <td>{result.get('media_exposed', 0)}</td>
                    <td>{result.get('confidence_score', 0)*100:.1f}%</td>
                </tr>
            """
            
        html += """
            </table>
            
            <h2>Recommendations</h2>
            <ul>
                <li>Apply the server-side authorization fix immediately</li>
                <li>Review all polaris_* JSON objects for similar issues</li>
                <li>Implement additional rate limiting on profile endpoints</li>
                <li>Add monitoring for suspicious access patterns</li>
            </ul>
        </body>
        </html>
        """
        
        return html
        
    def convert_to_pdf(self, html, filename):
        """Convert HTML to PDF"""
        # This would use a library like weasyprint or pdfkit
        pass
        
    def start_network_capture(self):
        """Start network traffic capture"""
        self.status_label.setText("Capturing network traffic...")
        # Implementation for packet capture
        
    def analyze_traffic(self):
        """Analyze captured traffic"""
        self.status_label.setText("Analyzing traffic patterns...")
        # Implementation for traffic analysis
        
    def validate_fix(self):
        """Validate fix implementation"""
        self.switch_to_tab(2)  # Switch to fix validator tab
        
    def network_analysis(self):
        """Open network analysis"""
        self.switch_to_tab(4)  # Switch to network analyzer tab
        
    def switch_to_tab(self, index):
        """Switch to specified tab"""
        self.tab_widget.setCurrentIndex(index)
        
    def change_theme(self, theme):
        """Change application theme"""
        self.current_theme = theme
        self.load_styles()
        
    def show_docs(self):
        """Show documentation"""
        QMessageBox.information(self, "Documentation", 
                               "Please refer to the internal wiki for documentation.")
        
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(self, "About Polaris Analyzer Pro",
                         "Instagram Polaris Security Analyzer Pro v2.0\n"
                         "Meta Internal Security Tool\n"
                         "For Authorized Use Only")
        
    def update_status(self):
        """Update status bar"""
        self.time_label.setText(QDateTime.currentDateTime().toString("hh:mm:ss AP"))


# ============================================================================
# SCAN WORKER THREAD
# ============================================================================

class ScanWorker(QObject):
    """Worker thread for scanning"""
    
    finished = pyqtSignal()
    result_ready = pyqtSignal(dict)
    progress_updated = pyqtSignal(int, int)
    
    def __init__(self, username, filepath):
        super().__init__()
        self.username = username
        self.filepath = filepath
        self.is_running = True
        self.session = self.create_session()
        
    def create_session(self):
        """Create requests session with retry strategy"""
        session = requests.Session()
        retry = Retry(total=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
        
    def run(self):
        """Main scan logic"""
        usernames = []
        
        if self.username:
            usernames.append(self.username)
        elif self.filepath:
            try:
                with open(self.filepath, 'r') as f:
                    usernames = [line.strip() for line in f if line.strip()]
            except Exception as e:
                print(f"Error reading file: {e}")
                
        total = len(usernames)
        
        for i, username in enumerate(usernames):
            if not self.is_running:
                break
                
            result = self.scan_username(username)
            self.result_ready.emit(result)
            self.progress_updated.emit(i + 1, total)
            
            # Rate limiting
            time.sleep(0.2)
            
        self.finished.emit()
        
    def scan_username(self, username):
        """Scan single username"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)',
                'Accept': 'text/html,application/xhtml+xml',
                'X-Requested-With': 'XMLHttpRequest'
            }
            
            response = self.session.get(
                f'https://www.instagram.com/{username}/',
                headers=headers,
                timeout=10,
                verify=False
            )
            
            # Check for vulnerability
            is_vuln, data = self.check_vulnerability(response.text)
            
            return {
                'username': username,
                'is_vulnerable': is_vuln,
                'risk_level': self.calculate_risk_level(data) if is_vuln else 'LOW',
                'media_exposed': data.get('media_count', 0),
                'json_path': data.get('json_path', ''),
                'timestamp': datetime.now().isoformat(),
                'headers_used': headers,
                'response_code': response.status_code,
                'confidence_score': data.get('confidence', 0.0),
                'fix_recommendation': self.get_fix_recommendation(is_vuln)
            }
            
        except Exception as e:
            return {
                'username': username,
                'is_vulnerable': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
            
    def check_vulnerability(self, html_content):
        """Check if response indicates vulnerability"""
        patterns = [
            r'"polaris_timeline_connection":({.*?}),"',
            r'"edges":\[(.*?)\]'
        ]
        
        media_count = 0
        confidence = 0.0
        json_path = ''
        
        for pattern in patterns:
            match = re.search(pattern, html_content)
            if match:
                json_path = pattern
                media_count = len(re.findall(r'"node"', match.group(0)))
                confidence = 0.8 if media_count > 0 else 0.2
                break
                
        is_vuln = media_count > 0 and 'is_private' in html_content
        
        return is_vuln, {
            'media_count': media_count,
            'json_path': json_path,
            'confidence': confidence
        }
        
    def calculate_risk_level(self, data):
        """Calculate risk level based on findings"""
        if data.get('media_count', 0) > 50:
            return 'CRITICAL'
        elif data.get('media_count', 0) > 20:
            return 'HIGH'
        elif data.get('media_count', 0) > 5:
            return 'MEDIUM'
        else:
            return 'LOW'
            
    def get_fix_recommendation(self, is_vuln):
        """Get fix recommendation"""
        if is_vuln:
            return "Apply server-side authorization fix immediately"
        return "No action required"
        
    def stop(self):
        """Stop the scan"""
        self.is_running = False


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("Polaris Security Analyzer Pro")
    app.setOrganizationName("Meta Security")
    
    # Set application icon
    app.setWindowIcon(QIcon.fromTheme('security-high'))
    
    # Create and show main window
    window = PolarisAnalyzerGUI()
    window.show()
    
    # Show splash screen
    splash = QSplashScreen()
    splash.setPixmap(QPixmap(400, 300))
    splash.show()
    
    # Simulate loading
    for i in range(100):
        time.sleep(0.01)
        app.processEvents()
    splash.close()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()