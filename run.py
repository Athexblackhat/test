#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════╗
║              POLARIS - Animated Launcher Script               ║
║         Cross-platform terminal launcher with effects         ║
╚═══════════════════════════════════════════════════════════════╝
"""

import sys
import os
import time
import random
import threading
import subprocess
import platform

# ─────────────────────────────────────────────
#  Platform detection & ANSI setup
# ─────────────────────────────────────────────

IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

# ─────────────────────────────────────────────
#  ANSI Color / Style Codes
# ─────────────────────────────────────────────

class C:
    RESET       = "\033[0m"
    BOLD        = "\033[1m"
    DIM         = "\033[2m"
    BLINK       = "\033[5m"
    REVERSE     = "\033[7m"

    BLACK       = "\033[30m"
    RED         = "\033[31m"
    GREEN       = "\033[32m"
    YELLOW      = "\033[33m"
    BLUE        = "\033[34m"
    MAGENTA     = "\033[35m"
    CYAN        = "\033[36m"
    WHITE       = "\033[37m"

    BRIGHT_RED     = "\033[91m"
    BRIGHT_GREEN   = "\033[92m"
    BRIGHT_YELLOW  = "\033[93m"
    BRIGHT_BLUE    = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN    = "\033[96m"
    BRIGHT_WHITE   = "\033[97m"

    BG_BLACK    = "\033[40m"
    BG_RED      = "\033[41m"
    BG_GREEN    = "\033[42m"
    BG_BLUE     = "\033[44m"
    BG_CYAN     = "\033[46m"

    # Cursor
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    CLEAR       = "\033[2J\033[H"
    CLEAR_LINE  = "\033[2K\r"

def move_up(n=1):    return f"\033[{n}A"
def move_down(n=1):  return f"\033[{n}B"
def move_right(n=1): return f"\033[{n}C"
def move_left(n=1):  return f"\033[{n}D"
def move_to(row, col): return f"\033[{row};{col}H"

def write(text, flush=True):
    sys.stdout.write(text)
    if flush:
        sys.stdout.flush()

# ─────────────────────────────────────────────
#  Terminal size helper
# ─────────────────────────────────────────────

def term_width():
    try:
        return os.get_terminal_size().columns
    except Exception:
        return 80

# ─────────────────────────────────────────────
#  ASCII Banner Lines
# ─────────────────────────────────────────────

BANNER = [
    r"  ██████╗  ██████╗ ██╗      █████╗ ██████╗ ██╗███████╗",
    r"  ██╔══██╗██╔═══██╗██║     ██╔══██╗██╔══██╗██║██╔════╝",
    r"  ██████╔╝██║   ██║██║     ███████║██████╔╝██║███████╗",
    r"  ██╔═══╝ ██║   ██║██║     ██╔══██║██╔══██╗██║╚════██║",
    r"  ██║     ╚██████╔╝███████╗██║  ██║██║  ██║██║███████║",
    r"  ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝",
]

TAGLINE = "✦  Navigation System — Advanced Launcher v1.0  ✦"

STARS_TOP = "  ★  ·  ✦  ·  ★  ·  ✦  ·  ★  ·  ✦  ·  ★  ·  ✦  ·  ★  ·  ✦  ·  ★"

# ─────────────────────────────────────────────
#  Animation Helpers
# ─────────────────────────────────────────────

def sleep(s):
    time.sleep(s)

def typing_text(text, color=C.BRIGHT_GREEN, delay=0.03, newline=True):
    """Print text with a typewriter effect."""
    write(color)
    for ch in text:
        write(ch)
        sleep(delay)
    write(C.RESET)
    if newline:
        write("\n")

def flash_text(text, color1=C.BRIGHT_CYAN, color2=C.CYAN, times=3, delay=0.12):
    """Flash text between two colors."""
    for _ in range(times):
        write(f"\r{color1}{text}{C.RESET}")
        sleep(delay)
        write(f"\r{color2}{text}{C.RESET}")
        sleep(delay)
    write(f"\r{color1}{text}{C.RESET}\n")

def spinner(message, duration=2.0, color=C.BRIGHT_CYAN):
    """Display a spinner for a given duration."""
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_time = time.time() + duration
    i = 0
    write(C.HIDE_CURSOR)
    try:
        while time.time() < end_time:
            frame = frames[i % len(frames)]
            write(f"\r  {color}{frame}{C.RESET}  {C.BRIGHT_WHITE}{message}{C.RESET}  ")
            sleep(0.08)
            i += 1
        write(f"\r  {C.BRIGHT_GREEN}✔{C.RESET}  {C.BRIGHT_WHITE}{message}{C.RESET}  \n")
    finally:
        write(C.SHOW_CURSOR)

def progress_bar(message, steps=30, delay=0.05, color=C.BRIGHT_GREEN, bar_color=C.CYAN):
    """Animated progress bar."""
    write(C.HIDE_CURSOR)
    try:
        write(f"\n  {C.BRIGHT_WHITE}{message}{C.RESET}\n\n")
        for i in range(steps + 1):
            pct = int(i / steps * 100)
            filled = i
            empty = steps - i
            bar = f"{bar_color}{'█' * filled}{C.DIM}{'░' * empty}{C.RESET}"
            spark = random.choice(["·", "✦", "★", "·"]) if i < steps else "✦"
            write(f"\r  [{bar}{color}] {pct:3d}%  {spark} ")
            sleep(delay)
        write(f"\n\n")
    finally:
        write(C.SHOW_CURSOR)

def slide_in_text(text, color=C.BRIGHT_WHITE, delay=0.018):
    """Print text as if sliding in from the left."""
    for i in range(1, len(text) + 1):
        write(f"\r  {color}{text[:i]}{C.RESET}")
        sleep(delay)
    write("\n")

def matrix_rain_line(width=60):
    """Print a single 'matrix rain' line of random characters."""
    chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ01"
    line = "".join(random.choice(chars) for _ in range(width))
    colors = [C.GREEN, C.BRIGHT_GREEN, C.CYAN, C.DIM + C.GREEN]
    colored = ""
    for ch in line:
        colored += random.choice(colors) + ch
    write(f"  {colored}{C.RESET}\n")

def animated_border(width=60, color=C.CYAN, delay=0.01):
    """Draw an animated top/bottom border."""
    chars = ["─", "═", "━"]
    border = ""
    for _ in range(width):
        border += random.choice(chars)
    write(color)
    for i in range(1, width + 1):
        write(f"\r  ╔{border[:i]}")
        sleep(delay)
    write(f"╗{C.RESET}\n")

def error_message(text):
    """Show a red blinking error message."""
    write(f"\n  {C.BLINK}{C.BRIGHT_RED}⚠  ERROR:{C.RESET}  {C.RED}{text}{C.RESET}\n\n")
    sleep(0.4)
    for _ in range(3):
        write(f"\r  {C.BG_RED}{C.WHITE}  ⚠  {text}  {C.RESET}")
        sleep(0.18)
        write(f"\r  {C.BRIGHT_RED}  ⚠  {text}  {C.RESET}")
        sleep(0.18)
    write(f"\r  {C.BRIGHT_RED}  ⚠  {text}  {C.RESET}\n\n")

def success_animation(message="Done!"):
    """Green success flash."""
    write(f"\n")
    for _ in range(2):
        write(f"\r  {C.BG_GREEN}{C.BLACK}  ✔  {message}  {C.RESET}")
        sleep(0.15)
        write(f"\r  {C.BRIGHT_GREEN}  ✔  {message}  {C.RESET}")
        sleep(0.15)
    write(f"\r  {C.BRIGHT_GREEN}  ✔  {message}  {C.RESET}\n\n")

# ─────────────────────────────────────────────
#  Banner Display
# ─────────────────────────────────────────────

BANNER_COLORS = [C.BRIGHT_CYAN, C.CYAN, C.BRIGHT_GREEN, C.BRIGHT_CYAN, C.CYAN, C.BRIGHT_GREEN]

def show_banner():
    """Display the full animated Polaris banner."""
    write(C.CLEAR)
    write(C.HIDE_CURSOR)

    # Matrix rain intro
    write(f"\n")
    for _ in range(4):
        matrix_rain_line(56)
        sleep(0.07)
    sleep(0.15)
    write(C.CLEAR)
    write(f"\n")

    # Stars top line - fade in
    write(f"  {C.DIM}{C.CYAN}")
    for ch in STARS_TOP:
        write(ch)
        sleep(0.012)
    write(f"{C.RESET}\n\n")

    # Banner lines - slide in with color
    for idx, line in enumerate(BANNER):
        color = BANNER_COLORS[idx % len(BANNER_COLORS)]
        for i in range(1, len(line) + 1):
            write(f"\r{color}{line[:i]}{C.RESET}")
            sleep(0.008)
        write("\n")
        sleep(0.04)

    write("\n")

    # Tagline typing
    padding = " " * max(0, (term_width() - len(TAGLINE)) // 2)
    typing_text(f"{padding}{TAGLINE}", color=C.BRIGHT_YELLOW, delay=0.025)

    # Stars bottom line
    write(f"\n  {C.DIM}{C.CYAN}")
    for ch in STARS_TOP:
        write(ch)
        sleep(0.012)
    write(f"{C.RESET}\n\n")

    # Glowing border flash
    border_str = "═" * 56
    for color in [C.DIM+C.CYAN, C.CYAN, C.BRIGHT_CYAN, C.CYAN, C.DIM+C.CYAN]:
        write(f"\r  {color}╔{border_str}╗{C.RESET}")
        sleep(0.09)
    write(f"\r  {C.BRIGHT_CYAN}╔{border_str}╗{C.RESET}\n\n")

    write(C.SHOW_CURSOR)

# ─────────────────────────────────────────────
#  Menu Display
# ─────────────────────────────────────────────

MENU_OPTIONS = [
    ("1", "→", "Run Script       ", "CLI VERSION",  C.BRIGHT_GREEN),
    ("2", "▶", "Run Script       ", "GUI VERSION",  C.BRIGHT_CYAN),
    ("3", "✗", "Exit Polaris     ", None,           C.BRIGHT_RED),
]

def show_menu():
    """Display the animated main menu."""
    write(C.HIDE_CURSOR)

    # Animated top border
    border_w = 50
    write(f"  {C.CYAN}")
    bar = ""
    for ch in "╔" + "═" * border_w + "╗":
        write(ch)
        bar += ch
        sleep(0.008)
    write(f"{C.RESET}\n")
    write(f"  {C.CYAN}║{C.RESET}")
    title = "  ✦  SELECT AN OPTION  ✦  "
    pad = " " * ((border_w - len(title)) // 2)
    typing_text(f"{pad}{title}{pad}", color=C.BRIGHT_WHITE, delay=0.018, newline=False)
    write(f"{C.CYAN}║{C.RESET}\n")
    write(f"  {C.CYAN}╠{'═' * border_w}╣{C.RESET}\n")

    # Menu options - slide in
    for key, sym, label, path, color in MENU_OPTIONS:
        path_str = f"  {C.DIM}{C.WHITE}({path}){C.RESET}" if path else ""
        line = f"  {C.CYAN}║{C.RESET}  [{color}{sym}{C.RESET}]  {color}{key}.{C.RESET}  {C.BRIGHT_WHITE}{label}{C.RESET}{path_str}"
        # Slide in effect
        raw = f"  ║  [{sym}]  {key}.  {label}" + (f"  ({path})" if path else "")
        for i in range(1, len(raw) + 1):
            write(f"\r{line[:i + 10]}")  # approximate slide
            sleep(0.006)
        write(f"\r{line}" + " " * 4 + f"  {C.CYAN}║{C.RESET}\n")
        sleep(0.04)

    write(f"  {C.CYAN}╚{'═' * border_w}╝{C.RESET}\n\n")
    write(C.SHOW_CURSOR)

# ─────────────────────────────────────────────
#  Input Prompt with spinner dots
# ─────────────────────────────────────────────

def prompt_choice():
    """Prompt user with an animated indicator."""
    write(f"  {C.BRIGHT_YELLOW}❯{C.RESET} {C.BRIGHT_WHITE}Enter choice {C.DIM}[1/2/3]{C.RESET}{C.BRIGHT_WHITE}:{C.RESET} ")
    sys.stdout.flush()
    try:
        choice = input().strip()
    except (EOFError, KeyboardInterrupt):
        choice = "3"
    return choice

# ─────────────────────────────────────────────
#  Script Execution
# ─────────────────────────────────────────────

def run_script(script_path, label):
    """Run a Python script with loading animations."""
    write(C.HIDE_CURSOR)
    write(f"\n  {C.BRIGHT_CYAN}╔{'═'*46}╗{C.RESET}\n")
    write(f"  {C.BRIGHT_CYAN}║{C.RESET}  {C.BRIGHT_WHITE}Launching:{C.RESET} {C.BRIGHT_GREEN}{label:<34}{C.RESET}  {C.BRIGHT_CYAN}║{C.RESET}\n")
    write(f"  {C.BRIGHT_CYAN}╚{'═'*46}╝{C.RESET}\n")

    spinner("Initializing Polaris...", duration=1.8)
    spinner("Loading modules...",      duration=1.0)
    progress_bar("Preparing environment", steps=28, delay=0.04)

    # Transition flash
    for _ in range(3):
        write(f"\r  {C.BG_CYAN}{C.BLACK}  ► LAUNCHING {label.strip().upper()}  {C.RESET}")
        sleep(0.13)
        write(f"\r  {C.BRIGHT_CYAN}  ► LAUNCHING {label.strip().upper()}  {C.RESET}")
        sleep(0.13)
    write(f"\n\n")
    write(C.SHOW_CURSOR)

    # Determine script path relative to this launcher
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, script_path)

    if not os.path.isfile(full_path):
        error_message(f"Script not found: {full_path}")
        write(f"  {C.DIM}Please ensure '{script_path}' exists.{C.RESET}\n\n")
        return False

    try:
        write(f"  {C.DIM}{C.CYAN}{'─'*52}{C.RESET}\n\n")
        result = subprocess.run([sys.executable, full_path], check=True)
        write(f"\n  {C.DIM}{C.CYAN}{'─'*52}{C.RESET}\n")
        success_animation(f"{label.strip()} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        error_message(f"Script exited with code {e.returncode}")
        return False
    except Exception as e:
        error_message(str(e))
        return False

# ─────────────────────────────────────────────
#  Return to Menu Pause
# ─────────────────────────────────────────────

def pause_return():
    """Wait for user to press Enter before returning to menu."""
    write(f"  {C.DIM}{C.WHITE}Press {C.RESET}{C.BRIGHT_WHITE}[ENTER]{C.RESET}{C.DIM} to return to menu...{C.RESET}  ")
    sys.stdout.flush()
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass

# ─────────────────────────────────────────────
#  Exit Animation
# ─────────────────────────────────────────────

def exit_animation():
    """Show farewell animation and exit."""
    write(C.HIDE_CURSOR)
    write(f"\n\n")

    farewell_lines = [
        "  ★  Polaris signing off...  ★",
        "  Fly safe, navigator.",
        "  Until next time — goodbye.",
    ]
    for line in farewell_lines:
        typing_text(line, color=C.BRIGHT_CYAN, delay=0.03)
        sleep(0.15)

    write(f"\n")

    # Matrix outro
    for i in range(5):
        matrix_rain_line(56)
        sleep(0.07)

    write(f"\n  {C.DIM}Session ended.{C.RESET}\n\n")
    write(C.SHOW_CURSOR)
    sys.exit(0)

# ─────────────────────────────────────────────
#  Main Loop
# ─────────────────────────────────────────────

def main():
    # Ensure ANSI works on Windows
    if IS_WINDOWS:
        os.system("color")

    show_banner()

    # Short initialisation spinner after banner
    spinner("Polaris ready", duration=1.2, color=C.BRIGHT_GREEN)
    write(f"\n")

    while True:
        show_menu()
        choice = prompt_choice()

        if choice == "1":
            write(f"\n")
            run_script("src/run.py", "run.py")
            pause_return()
            write(C.CLEAR)
            show_banner()

        elif choice == "2":
            write(f"\n")
            run_script("src/gui.py", "gui.py")
            pause_return()
            write(C.CLEAR)
            show_banner()

        elif choice == "3":
            exit_animation()

        else:
            error_message(f"'{choice}' is not a valid option — choose 1, 2, or 3.")
            sleep(0.8)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        write(f"\n{C.SHOW_CURSOR}")
        exit_animation()