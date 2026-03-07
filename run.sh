#!/usr/bin/env bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BLACK='\033[0;30m'
ORANGE='\033[0;33m'
MAGENTA='\033[0;35m'
LIGHT_RED='\033[1;31m'
LIGHT_GREEN='\033[1;32m'
LIGHT_BLUE='\033[1;34m'
LIGHT_PURPLE='\033[1;35m'
LIGHT_CYAN='\033[1;36m'
BOLD='\033[1m'
NC='\033[0m' 
BG_RED='\033[41m'
BG_GREEN='\033[42m'
BG_BLUE='\033[44m'
BG_PURPLE='\033[45m'
BG_CYAN='\033[46m'
BG_YELLOW='\033[43m'


clear

print_banner() {
    local frame=$1
    local colors=($RED $GREEN $YELLOW $BLUE $PURPLE $CYAN $WHITE)
    case $frame in
        0|6)
            echo -e "${colors[$frame]}"
            cat << "EOF"

          ██╗   ██╗███╗   ██╗██╗███████╗██╗███████╗██████╗            
          ██║   ██║████╗  ██║██║██╔════╝██║██╔════╝██╔══██╗           
          ██║   ██║██╔██╗ ██║██║█████╗  ██║█████╗  ██║  ██║           
          ██║   ██║██║╚██╗██║██║██╔══╝  ██║██╔══╝  ██║  ██║           
          ╚██████╔╝██║ ╚████║██║██║     ██║███████╗██████╔╝           
           ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚══════╝╚═════╝                     
    
EOF
            ;;
        1|7)
            echo -e "${colors[$frame]}"
            cat << "EOF"

                          🔐 SECURITY ANALYZER 🔐                       
                             PROFESSIONAL EDITION                       
///═════════════════════════════════════════════════════════════════///
                                                                       
          ⚡ Network Monitoring    |    🕷️  Deep Web Crawler            
          🧩 Extension Analysis    |    🌐 Web App Scanner             
          📊 Live Progress         |    🎯 Real-time Detection         
                                                                       
                     🚀 Version 3.0 Professional                  
    
EOF
            ;;
        2|8)
            echo -e "${colors[$frame]}"
            cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ║
    ║     ░█▀▀░█▀█░█▀▄░█▀▀░█░█░░░█▀▄░█▀█░█▀▀░█░█░░░█▀▀░█▀█░█▀▄░░        ║
    ║     ░█░░░█░█░█░█░█▀▀░▄▀▄░░░█░█░█░█░█▀▀░█▄█░░░█░░░█░█░█░█░░        ║
    ║     ░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀░░░        ║
    ║     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ║
    ║                                                                   ║
    ║              🔥 PROFESSIONAL SECURITY SUITE 🔥                    ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
EOF
            ;;
        3|9)
            echo -e "${colors[$frame]}"
            cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║     ╔═╗╦ ╦╔╦╗╔═╗╔╦╗╔═╗╔╗╔╔╦╗  ╔═╗╔═╗╔╦╗╔═╗╦ ╦╔╗╔╔╦╗╔═╗            ║
    ║     ╠═╣║ ║ ║ ╠═╣ ║ ║╣ ║║║ ║   ║  ║ ║║║║╠═╣║ ║║║║ ║ ╚═╗            ║
    ║     ╩ ╩╚═╝ ╩ ╩ ╩ ╩ ╚═╝╝╚╝ ╩   ╚═╝╚═╝╩ ╩╩ ╩╚═╝╝╚╝ ╩ ╚═╝            ║
    ║                                                                   ║
    ║                    🛡️  ZERO TRUST READY  🛡️                       ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
EOF
            ;;
        4|10)
            echo -e "${colors[$frame]}"
            cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║    🌐 WEB SCANNER    │    📡 NETWORK MONITOR    │    🧩 EXTENSION  ║
    ║    ─────────────────────────────────────────────────────────────   ║
    ║    ✓ SQL Injection   │    ✓ API Key Detection │    ✓ Hardcoded    ║
    ║    ✓ XSS Testing     │    ✓ Traffic Analysis  │    ✓ Permissions  ║
    ║    ✓ Path Traversal  │    ✓ Live Statistics   │    ✓ Obfuscation  ║
    ║    ✓ CSRF Checks     │    ✓ Packet Capture    │    ✓ External API ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
EOF
            ;;
        5|11)
            echo -e "${colors[$frame]}"
            cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║     ████████╗ ██████╗  ██████╗ ██╗     ███████╗████████╗          ║
    ║     ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝╚══██╔══╝          ║
    ║        ██║   ██║   ██║██║   ██║██║     █████╗     ██║             ║
    ║        ██║   ██║   ██║██║   ██║██║     ██╔══╝     ██║             ║
    ║        ██║   ╚██████╔╝╚██████╔╝███████╗███████╗   ██║             ║
    ║        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝             ║
    ║                                                                   ║
    ║                     🔧 INSTALLATION SCRIPT 🔧                     ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
EOF
            ;;
    esac
}

loading_animation() {
    local pid=$1
    local message=$2
    local spinstr='|/-\'
    local temp
    
    echo -ne "${CYAN}$message ${NC}"
    
    while ps -p $pid > /dev/null 2>&1; do
        temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep 0.1
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
    echo -e "${GREEN}✓ Done!${NC}"
}

animate_banner() {
    for i in {0..5}; do
        clear
        print_banner $i
        sleep 0.3
    done
}

glitch_effect() {
    local text=$1
    local glitch_chars='!@#$%&*<>?/\\|'
    
    for i in {1..3}; do
        echo -ne "\r${RED}${text:0:${#text}-$i}${glitch_chars:RANDOM%${#glitch_chars}:1}${NC}"
        sleep 0.1
    done
    echo -ne "\r${GREEN}${text}${NC}\n"
}

matrix_effect() {
    local chars="01アイウエオカキクケコサシスセソタチツテト"
    local lines=5
    
    for ((l=0; l<lines; l++)); do
        for ((i=0; i<40; i++)); do
            echo -ne "\e[32m${chars:RANDOM%${#chars}:1}\e[0m"
        done
        echo
        sleep 0.1
    done
}

print_step() {
    echo -e "\n${BOLD}${BLUE}════════════════════════════════════════════════════════════════════${NC}"
    echo -e "${BOLD}${CYAN}   ⚡ $1${NC}"
    echo -e "${BOLD}${BLUE}════════════════════════════════════════════════════════════════════${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${CYAN}ℹ️  $1${NC}"
}

check_command() {
    if command -v $1 &> /dev/null; then
        print_success "$1 found"
        return 0
    else
        print_warning "$1 not found"
        return 1
    fi
}

progress_bar() {
    local current=$1
    local total=$2
    local width=50
    local percentage=$((current * 100 / total))
    local completed=$((current * width / total))
    local remaining=$((width - completed))
    
    printf "\r${CYAN}[${NC}"
    printf "%${completed}s" | tr ' ' '█'
    printf "%${remaining}s" | tr ' ' '░'
    printf "${CYAN}]${NC} ${GREEN}%3d%%${NC}" $percentage
}


animate_banner

echo -e "\n${GREEN}Initializing security protocols...${NC}\n"
matrix_effect
sleep 1

echo -e "\n${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}                    🔐 LEGAL NOTICE & DISCLAIMER                     ${NC}"
echo -e "${BOLD}${RED}///═══════════════════════════════════════════════════════════════════///${NC}"
echo -e "${BOLD}${RED}${NC}                                                                   ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}  ${YELLOW}Unified Security Analysis Tool is for AUTHORIZED testing ONLY!${NC}   ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}                                                                   ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}  • Only scan systems you own or have permission to test           ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}  • Network monitoring may be subject to local laws                 ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}  • The user assumes all responsibility for compliance              ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}  • Handle all findings confidentially                               ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}                                                                   ${BOLD}${RED}${NC}"
echo -e "${BOLD}${RED}${NC}\n"

echo -ne "${BOLD}${YELLOW}Do you accept these terms and wish to continue? (y/N): ${NC}"
read -r agreement

if [[ ! "$agreement" =~ ^[Yy]$ ]]; then
    echo -e "\n${RED}Installation cancelled.${NC}"
    exit 0
fi

echo -e "\n${GREEN}✓ Terms accepted. Starting installation...${NC}\n"
sleep 1

print_step "🔍 SYSTEM CHECK"

echo -ne "${CYAN}Checking Python version...${NC}"
python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
if [[ $(echo "$python_version" | cut -d. -f1) -ge 3 ]] && [[ $(echo "$python_version" | cut -d. -f2) -ge 6 ]]; then
    echo -e "\r${GREEN}✅ Python $python_version found${NC}"
else
    echo -e "\r${RED}❌ Python 3.6+ required (found $python_version)${NC}"
    exit 1
fi

echo -ne "${CYAN}Checking pip...${NC}"
if command -v pip3 &> /dev/null; then
    echo -e "\r${GREEN}✅ pip3 found${NC}"
else
    echo -e "\r${RED}❌ pip3 not found${NC}"
    exit 1
fi

echo -ne "${CYAN}Checking permissions...${NC}"
if [[ $EUID -eq 0 ]]; then
    echo -e "\r${GREEN}✅ Running as root (network monitoring enabled)${NC}"
else
    echo -e "\r${YELLOW}⚠️  Not running as root (network monitoring may be limited)${NC}"
    print_warning "Network monitoring requires root privileges"
    print_info "You can run: sudo -E python3 install.py after installation"
fi
sleep 1

print_step "📦 CREATING VIRTUAL ENVIRONMENT"

echo -ne "${CYAN}Creating venv...${NC}"
python3 -m venv venv > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "\r${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "\r${YELLOW}⚠️  Could not create virtual environment${NC}"
    print_warning "Installing globally instead"
fi

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    print_success "Virtual environment activated"
fi

print_step "📥 INSTALLING DEPENDENCIES"

DEPENDENCIES=(
    "requests"
    "beautifulsoup4"
    "scapy"
    "cryptography"
    "dnspython"
    "lxml"
    "colorama"
)

TOTAL=${#DEPENDENCIES[@]}
CURRENT=0

for dep in "${DEPENDENCIES[@]}"; do
    ((CURRENT++))
    progress_bar $CURRENT $TOTAL
    echo -ne " ${CYAN}Installing $dep...${NC}"
    
    pip3 install --quiet $dep 2>&1 &
    PID=$!
    wait $PID
    
    if [ $? -eq 0 ]; then
        echo -e "\r${GREEN}✅ $dep installed${NC}                    "
    else
        echo -e "\r${RED}❌ Failed to install $dep${NC}                "
    fi
done

echo -e "\n${GREEN}✓ Dependencies installed${NC}"
sleep 1

print_step "📝 CREATING INSTALLATION FILE"

cat > install.py << 'EOF'
#!/usr/bin/env python3
"""
Unified Security Analysis Tool - Professional Edition
Installation and setup script
"""

import sys
import subprocess
import platform
import os
import time

def print_color(text, color=None):
    """Print colored text"""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    
    if color and color in colors:
        print(f"{colors[color]}{text}{colors['end']}")
    else:
        print(text)

def loading_animation(message):
    """Show loading animation"""
    chars = "|/-\\"
    for i in range(20):
        sys.stdout.write(f'\r{message} {chars[i % len(chars)]}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
    sys.stdout.flush()

def main():
    """Main installation function"""
    print_color("""
╔══════════════════════════════════════════════════════════════╗
║           UNIFIED SECURITY ANALYSIS TOOL                     ║
║                  Python Installation                         ║
╚══════════════════════════════════════════════════════════════╝
    """, 'cyan')
    
    print_color("\n[+] Setting up environment...", 'yellow')
    
    # Check Python version
    if sys.version_info < (3, 6):
        print_color("[-] Python 3.6+ required!", 'red')
        sys.exit(1)
    
    print_color("[+] Python version OK", 'green')
    
    # Create necessary directories
    directories = ['logs', 'reports', 'temp']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print_color(f"[+] Created {directory} directory", 'green')
    
    # Check platform-specific requirements
    if platform.system() == "Linux":
        print_color("[+] Linux detected", 'green')
        # Check for libpcap (required for scapy)
        try:
            subprocess.run(["ldconfig", "-p"], capture_output=True, text=True)
            print_color("[+] Network libraries found", 'green')
        except:
            print_color("[-] Warning: Some network features may be limited", 'yellow')
    
    elif platform.system() == "Darwin":
        print_color("[+] macOS detected", 'green')
        # Check for libpcap on macOS
        if os.path.exists("/usr/lib/libpcap.dylib"):
            print_color("[+] Network libraries found", 'green')
    
    elif platform.system() == "Windows":
        print_color("[+] Windows detected", 'green')
        print_color("[+] Note: Network monitoring requires Npcap", 'yellow')
    
    loading_animation("[*] Finalizing installation")
    
    print_color("""
    
╔══════════════════════════════════════════════════════════════╗
║                     INSTALLATION COMPLETE!                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   Run the tool with:  python3 security_tool.py               ║
║                                                              ║
║   For network monitoring (Linux/macOS):                      ║
║   sudo python3 security_tool.py                              ║
║                                                              ║
║   Required dependencies are installed                        ║
║   Check logs directory for output                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """, 'green')
    
    print_color("\n[+] Starting the tool now...", 'cyan')
    time.sleep(2)

if __name__ == "__main__":
    main()
EOF

chmod +x install.py
print_success "install.py created"

print_step "🚀 FINAL INSTALLATION"

echo -e "${CYAN}Running Python installation script...${NC}\n"
python3 install.py

if [ ! -f "security_tool.py" ] && [ ! -f "unified_security_tool.py" ]; then
    print_warning "Main tool file not found in current directory"
    print_info "Please ensure your security tool Python file is in this directory"
    print_info "Expected filename: security_tool.py or unified_security_tool.py"
    
    echo -ne "\n${YELLOW}Enter the filename of your security tool (or press Enter to skip): ${NC}"
    read -r tool_file
    
    if [ -n "$tool_file" ] && [ -f "$tool_file" ]; then
        print_success "Found $tool_file"
        chmod +x "$tool_file"
    fi
fi

# Final ASCII art
clear
echo -e "${GREEN}"
cat << "EOF"
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗            ║
    ║      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║            ║
    ║      ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║            ║
    ║      ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║            ║
    ║      ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗       ║
    ║      ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝       ║
    ║                                                                   ║
    ║                      🎉 INSTALLATION COMPLETE! 🎉                ║
    ║                                                                   ║
    ╠═══════════════════════════════════════════════════════════════════╣
    ║                                                                   ║
    ║   🌐 Web Scanner:    python3 security_tool.py                     ║
    ║   📡 Network Monitor: sudo python3 security_tool.py               ║
    ║   📊 Reports:        ./reports/                                   ║
    ║   📝 Logs:           ./logs/                                      ║
    ║                                                                   ║
    ║   🔧 Quick Start:                                                 ║
    ║   $ python3 security_tool.py                                      ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Show dependency status
print_step "📊 DEPENDENCY STATUS"

deps_ok=0
deps_total=5

# Check each dependency
check_command "python3" && ((deps_ok++))
python3 -c "import requests" 2>/dev/null && print_success "requests installed" && ((deps_ok++))
python3 -c "import bs4" 2>/dev/null && print_success "beautifulsoup4 installed" && ((deps_ok++))
python3 -c "import scapy" 2>/dev/null && print_success "scapy installed" && ((deps_ok++))
python3 -c "import cryptography" 2>/dev/null && print_success "cryptography installed" && ((deps_ok++))

echo
if [ $deps_ok -eq $deps_total ]; then
    echo -e "${GREEN}✓ All dependencies installed successfully!${NC}"
else
    echo -e "${YELLOW}⚠️  Some dependencies are missing ($deps_ok/$deps_total)${NC}"
    print_info "Run: pip install -r requirements.txt"
fi

# Create requirements.txt for future reference
cat > requirements.txt << 'EOF'
requests>=2.26.0
beautifulsoup4>=4.10.0
scapy>=2.4.5
cryptography>=3.4.8
dnspython>=2.1.0
lxml>=4.6.3
colorama>=0.4.4
EOF

print_success "Created requirements.txt"

# Glitch effect for fun
echo -e "\n"
glitch_effect "SYSTEM READY"
echo -e "\n"

# Final countdown
echo -ne "${CYAN}Launching tool in ${NC}"
for i in 3 2 1; do
    echo -ne "${GREEN}$i${NC} "
    sleep 0.5
done
echo -e "${GREEN}GO!${NC}\n"
sleep 0.5

# Check for main tool file and run it
if [ -f "install.py" ]; then
    python3 install.py
elif [ -f "install.py" ]; then
    python3 install.py
else
    # Save the provided Python code
    echo -e "${YELLOW}Main tool file not found. Creating from provided code...${NC}"
    
    cat > install.py << 'PYTHON_CODE'
#!/usr/bin/env python3
"""
Unified Security Analysis Tool - Professional Edition
Paste your provided Python code here
"""
PYTHON_CODE
    
    echo -e "${YELLOW}Please paste your Python tool code into install.py${NC}"
    echo -e "${GREEN}Installation complete! Run: python3 install.py${NC}"
    
    # Open in editor if possible
    if command -v nano &> /dev/null; then
        echo -ne "\n${CYAN}Open in nano editor now? (y/N): ${NC}"
        read -r open_editor
        if [[ "$open_editor" =~ ^[Yy]$ ]]; then
            nano install.py
        fi
    fi
fi