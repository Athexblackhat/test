<a href="https://github.com/Athexhacker/UNIFIED"><img src="/src/logo.png" alt="0" border="0" /></a> 

<div align="center">

```
   
             ██╗   ██╗███╗   ██╗██╗███████╗██╗███████╗██████╗   ╔══════╗  
             ██║   ██║████╗  ██║██║██╔════╝██║██╔════╝██╔══██╗  ║ CYBER║  
             ██║   ██║██╔██╗ ██║██║█████╗  ██║█████╗  ██║  ██║  ║ ═════╝  
             ██║   ██║██║╚██╗██║██║██╔══╝  ██║██╔══╝  ██║  ██║  ║ ELITE║
             ╚██████╔╝██║ ╚████║██║██║     ██║███████╗██████╔╝  ║ ═════╗  
              ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝╚═════╝   ║ TOOL ║  
                                                                ═══════╝
```

**Unified Security Analysis Tool — Professional Edition**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)]()
[![OWASP](https://img.shields.io/badge/OWASP-Top%2010-red?style=flat-square)](https://owasp.org/Top10/)

*Four powerful security tools. One unified interface. Live progress. Real results.*

[Features](#-features) · [Installation](#-installation) · [Usage](#-usage) · [Modules](#-modules) · [Legal](#️-legal-notice)

</div>

---

## ⚡ What Is This?

**UNIFIED** is an all-in-one desktop security analysis platform built in Python + Tkinter. It combines four distinct security disciplines into a single, dark-themed GUI with **real-time progress tracking**, making it suitable for professional security assessments and academic research.

```
┌─────────────────────────────────────────────────────┐
│  🌐 Web App Scanner    │  🧩 Extension Analyzer    │
│  ──────────────────    │  ────────────────────      │
│  OWASP Top 10 tests    │  Chrome CRX download       │
│  SQLi / XSS / CSRF     │  Manifest audit            │
│  Path traversal        │  JS vulnerability scan     │
│  Directory enumeration │  API key extraction        │
├─────────────────────────────────────────────────────┤
│  📡 Network Monitor    │  🔍 Deep Web Crawler      │
│  ──────────────────    │  ─────────────────         │
│  Passive packet sniff  │  Recursive site crawl      │
│  HTTP/HTTPS analysis   │  JS file analysis          │
│  API key detection     │  Secret key detection      │
│  Live traffic stats    │  Configurable depth/pages  │
└─────────────────────────────────────────────────────┘
```

---

## ✨ Features

### 🎯 Core Capabilities

| Feature | Description |
|---|---|
| **Live Progress Tracking** | Every scan shows real-time % completion with animated progress bars |
| **Unified Dashboard** | Central stats overview across all tools |
| **Severity Classification** | CRITICAL / HIGH / MEDIUM / LOW / INFO with color coding |
| **CWE & OWASP Mapping** | All findings mapped to industry standards |
| **Export & Reporting** | Copy-paste details from any vulnerability |
| **Graceful Degradation** | Works even with optional deps missing |

### 🔑 API Key Pattern Recognition

Detects **15+ secret types** out of the box:

```
☁️  Cloud        →  AWS Keys, Google API, Firebase
🤖  AI Services  →  OpenAI (sk-*), Anthropic (sk-ant-*)
💳  Payment      →  Stripe Live, PayPal Access Tokens
🔧  DevOps       →  GitHub PATs (ghp_/gho_/ghr_...)
💬  Comms        →  Discord Bot Tokens, Telegram Bots
🗄️  Database     →  MongoDB URIs, Firebase URLs
🔐  Auth         →  JWT Tokens, OAuth credentials
```

---

## 📦 Installation

### Prerequisites

```bash
python --version  
```

### Quick Start

```bash
git clone https://github.com/Athexhacker/UNIFIED.git
cd UNIFIED
bash run.sh
```

### Dependency Matrix

| Library | Purpose | Required? |
|---|---|---|
| `requests` | Web scanning & crawling | ✅ Core |
| `beautifulsoup4` | HTML parsing | ✅ Core |
| `scapy` | Network packet capture | ⚡ Network Monitor only |
| `cryptography` | Decryption analysis | 🔧 Optional |
| `dnspython` | DNS lookups | 🔧 Optional |

> The tool launches and functions even if optional packages are absent — it simply disables the relevant features and notifies you.

---

## 🚀 Usage

### Launching

```bash
bash run.sh
```

You'll be prompted with a legal notice. Accept to proceed.

### Module Walkthroughs

#### 🌐 Web Application Scanner

1. Navigate to **WEB SCANNER** tab
2. Enter target URL (e.g., `https://yourtestsite.com`)
3. Click **▶ START SCAN**
4. Watch the live progress bar — 8 sequential test phases run automatically:

```
Phase 1: Target Validation     → Connectivity & server info
Phase 2: Tech Fingerprinting   → Frameworks, analytics, CMS
Phase 3: Website Crawl         → Discover pages & forms
Phase 4: Path Discovery        → Hidden directories & sensitive files
Phase 5: Misconfiguration Check→ Debug mode, directory listing
Phase 6: SQL Injection Tests   → Error-based detection
Phase 7: XSS Tests             → Reflected XSS via forms
Phase 8: CSRF / Path Traversal → Token checks, file reads
```

#### 🧩 Chrome Extension Analyzer

1. Navigate to **EXTENSION ANALYZER** tab
2. Paste an Extension ID (32-char string) or full Chrome Web Store URL
3. Use quick-load buttons for popular extensions (uBlock, LastPass, Grammarly)
4. Click **🔍 ANALYZE**

The analyzer will:
- Fetch metadata from Chrome Web Store
- Download the `.crx` file
- Extract and inspect all JavaScript files
- Flag obfuscated code, dangerous APIs, hardcoded secrets

#### 📡 Network Monitor

> Requires `scapy` and typically elevated privileges (root/admin)

1. Navigate to **NETWORK MONITOR** tab
2. Set your network interface (`eth0`, `Wi-Fi`, etc.)
3. Click **▶ START MONITOR**
4. Live stats update in real time: Packets · HTTP requests · Keys found

#### 🔍 Deep Web Crawler

1. Navigate to **DEEP CRAWLER** tab
2. Set target URL, crawl depth (1–5), and max pages
3. Click **▶ START CRAWL**

Crawls the site recursively, then scans all discovered JavaScript files for exposed secrets.

## 📊 Output & Results

### Vulnerability Severity Schema

```
🔴 CRITICAL  →  Immediate remediation required (hardcoded secrets, SQLi, RCE vectors)
🟠 HIGH      →  Serious risk, fix within 24–48h (XSS, missing auth, insecure storage)
🟡 MEDIUM    →  Moderate risk, schedule fix (missing headers, CSRF, info disclosure)
🟢 LOW       →  Minor issues, fix in next sprint (email exposure, internal IPs)
🔵 INFO      →  Informational only
```

### Extension Risk Score

Risk scores are calculated from found vulnerabilities:

```
CRITICAL finding  →  +25 points
HIGH finding      →  +10 points
MEDIUM finding    →  + 5 points
LOW finding       →  + 1 point

Score 0–20   → Low Risk    ✅
Score 21–50  → Medium Risk ⚠️
Score 51–80  → High Risk   🔴
Score 81–100 → Critical    🚨
```

---

## 🛡️ Remediation Guides

The **🔧 REMEDIATION** tab contains built-in reference guides covering:

- **OWASP Top 10** — All 10 categories with actionable fixes
- **API Security** — Auth, rate limiting, input validation, monitoring
- **Extension Security** — Manifest V3, CSP, message passing, permissions
- **Network Security** — TLS hardening, DNS security, firewall config, incident response

---


---

## ⚙️ Configuration

Key constants you can modify at the top of the file:

| Constant | Default | Description |
|---|---|---|
| `SQL_PAYLOADS` | 13 payloads | SQLi test strings |
| `XSS_PAYLOADS` | 10 payloads | XSS test strings |
| `COMMON_PATHS` | 50+ paths | Directory enumeration list |
| `SENSITIVE_FILES` | 30+ files | Sensitive file checklist |
| `API_PATTERNS` | 15+ patterns | API key regex patterns |

---

## ⚖️ Legal Notice

> **This tool is for authorized security testing ONLY.**

- ✅ Test systems you **own**
- ✅ Test systems you have **written permission** to assess
- ✅ Use in isolated lab/CTF environments
- ❌ Do NOT scan systems without explicit authorization
- ❌ Network monitoring may be **illegal** in your jurisdiction without consent
- ❌ The authors assume **no liability** for misuse

Always act responsibly and in accordance with applicable laws. When in doubt, consult a legal professional before testing.

---

## 🤝 Contributing

Contributions are welcome! Areas of interest:

- Additional API key patterns
- New vulnerability detection modules
- Improved false-positive filtering
- Export formats (JSON, HTML report, PDF)
- Plugin architecture for custom scanners

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

*Built for security professionals. Use responsibly.*

⭐ **Star this repo if you find it useful** ⭐
***DEVELOPER***
 *MARKHOR ( TEAM ATHEX )*
</div>