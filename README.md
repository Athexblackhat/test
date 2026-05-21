# 💰 Cash Cam Pro v2.0

> **Payment Gateway Phishing + Camera Capture Tool**
> 
> Created by: **ATHEX BLACK HAT**
> 
> ⚠️ **For Educational Purposes Only!**

---

## 📋 Description

Cash Cam Pro is an advanced security testing tool that simulates a payment gateway phishing scenario with integrated camera capture capabilities. It creates a realistic **Cash Easy Way** (EasyPaisa/JazzCash style) payment interface and monitors victim interactions in real-time through a professional admin panel.

### ✨ Features

| Feature | Description |
|---------|-------------|
| 🎣 **Payment Phishing** | Realistic EasyPaisa/JazzCash/Cash Easy Way payment form |
| 📸 **Camera Capture** | Auto camera snap every 200ms with permission retry logic |
| 🌐 **Cloudflare Tunnel** | Instant public URL via Cloudflared |
|   **Live Admin Panel** | Real-time monitoring dashboard with stats |
| 💰 **Payment Data Log** | Captures name, account number, service, amount |
| 🎯 **IP Tracking** | Logs visitor IP + User-Agent |
| 🎨 **Animated UI** | Professional green theme with wave animations |
| 📱 **Mobile Responsive** | Works on all devices |

---

---


---

## 🚀 Installation

### Prerequisites
- **Termux** (Android) or any Linux terminal
- Internet connection

### One-Click Setup
```
git clone https://github.com/Athexblackhat/CASH-CAM-PRO.git
cd CASH-CAM-PRO
chmod +x *
./cash.sh
```

## 🎯 Victim Flow

```
Victim opens phishing link

Sees Cash Easy Way payment page

Clicks "Send Payment" or "Receive Payment"

Camera permission requested (3 retries if denied)

After allowing camera → snaps captured silently

Victim fills payment form (Name, Account, Amount, etc.)

Form submitted → Data sent to post.php

Success animation shown to victim
```

##   Admin Panel Features
```
Panel Section	Data Shown
Stats Cards	    Total Events, IP Captures, Payments, Camera Snaps
Live Feed	    Real-time event log with color-coded icons
Payment         Details	Service, Name, Account, Amount, Description
Camera          Gallery	Thumbnail grid with click-to-enlarge modal
Live Ticker	Scrolling recent events
```

## Panel Filters
```
🔵 ALL - Show all events

🟡 IP - Only IP captures

🟢 PAYMENT - Only payment data

🔴 CAMERA - Only camera snaps
```


### 🔄 All data stored locally on your device

### 🌐 Cloudflared provides HTTPS encryption


## 👤 Credits
***Developer: ATHEX H4CK3R***

***Contact: WhatsApp: +92 3490916663***

***Tool Name: Cash Cam Pro v2.0***


## ⚠️ Disclaimer

This tool is created for EDUCATIONAL PURPOSES ONLY.
The developer is not responsible for any misuse or damage.
Always obtain proper authorization before testing.
Using this tool for illegal activities is strictly prohibited.
Users are responsible for complying with all applicable laws.

<p align="center"> <b>💰 Cash Cam Pro v2.0 💰</b><br> <i>Payment Phishing + Camera Capture Suite</i><br> <sub>© 2026 ATHEX H4CK3R | Educational Use Only</sub> </p> ```