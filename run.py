import tkinter as tk
from tkinter import ttk, messagebox, font
import requests
import json
from datetime import datetime
import threading
import webbrowser
from PIL import Image, ImageTk
import io
import re

class AnimatedSIMDatabaseTool:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🇵🇰 PAK SIM DATABASE TOOL v2.0")
        self.window.geometry("1200x700")
        
        # Set window icon and background
        self.window.configure(bg='#0a0f1e')
        
        # Center window on screen
        self.center_window()
        
        # Remove default title bar for custom look
        self.window.overrideredirect(True)
        
        # Variables
        self.current_frame = None
        self.colors = {
            'bg_dark': '#0a0f1e',
            'bg_medium': '#151f30',
            'bg_light': '#1e2a3a',
            'accent': '#00d4ff',
            'accent_secondary': '#7b2eda',
            'text': '#ffffff',
            'text_secondary': '#a0b3d9',
            'success': '#00d25b',
            'error': '#fc5a5a'
        }
        
        # API Base URL
        self.api_base = "https://howler-database-api.vercel.app/api/lookup?phone="
        
        # Load fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.heading_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=11)
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Custom title bar
        self.create_title_bar()
        
        # Show login screen first
        self.show_login_screen()
        
    def center_window(self):
        """Center the window on screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_title_bar(self):
        """Create custom animated title bar"""
        title_bar = tk.Frame(self.window, bg='#1a2538', height=40)
        title_bar.pack(fill='x', side='top')
        title_bar.pack_propagate(False)
        
        # App icon and title
        title_label = tk.Label(title_bar, text="⚡ SIM DATABASE PRO", 
                               fg='#00d4ff', bg='#1a2538',
                               font=("Helvetica", 12, "bold"))
        title_label.pack(side='left', padx=15, pady=8)
        
        # Window controls
        close_btn = tk.Button(title_bar, text='✕', bg='#1a2538', fg='#a0b3d9',
                              bd=0, font=("Helvetica", 14), activebackground='#fc5a5a',
                              activeforeground='white', command=self.close_app)
        close_btn.pack(side='right', padx=10, pady=5)
        
        minimize_btn = tk.Button(title_bar, text='─', bg='#1a2538', fg='#a0b3d9',
                                 bd=0, font=("Helvetica", 14), activebackground='#2a3a5a',
                                 activeforeground='white', command=self.minimize_window)
        minimize_btn.pack(side='right', padx=5, pady=5)
        
        # Make window draggable
        title_bar.bind('<Button-1>', self.start_move)
        title_bar.bind('<B1-Motion>', self.on_move)
        title_label.bind('<Button-1>', self.start_move)
        title_label.bind('<B1-Motion>', self.on_move)
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")
    
    def minimize_window(self):
        self.window.iconify()
    
    def close_app(self):
        self.window.destroy()
    
    def create_gradient(self, canvas, width, height, color1, color2):
        """Create gradient background"""
        limit = width
        for i in range(limit):
            ratio = i/limit
            r = int(int(color1[1:3], 16) * (1 - ratio) + int(color2[1:3], 16) * ratio)
            g = int(int(color1[3:5], 16) * (1 - ratio) + int(color2[3:5], 16) * ratio)
            b = int(int(color1[5:7], 16) * (1 - ratio) + int(color2[5:7], 16) * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(i, 0, i, height, fill=color, width=1)
    
    def clear_frame(self):
        """Clear current frame with fade animation"""
        if self.current_frame:
            def fade():
                alpha = 1.0
                while alpha > 0:
                    self.current_frame.attributes('-alpha', alpha)
                    alpha -= 0.1
                    self.window.update()
                    self.window.after(50)
                self.current_frame.destroy()
            
            threading.Thread(target=fade).start()
    
    def show_login_screen(self):
        """Show animated login screen"""
        # Clear existing content
        for widget in self.window.winfo_children():
            if widget.winfo_class() != 'Frame' or widget != self.window.winfo_children()[0]:
                widget.destroy()
        
        # Main login frame
        login_frame = tk.Frame(self.window, bg=self.colors['bg_dark'])
        login_frame.pack(fill='both', expand=True)
        self.current_frame = login_frame
        
        # Center container
        container = tk.Frame(login_frame, bg=self.colors['bg_medium'], 
                            highlightbackground=self.colors['accent'],
                            highlightthickness=2)
        container.place(relx=0.5, rely=0.5, anchor='center', width=400, height=500)
        
        # Animated title
        title_label = tk.Label(container, text="🔐 SECURE ACCESS", 
                              font=self.title_font,
                              fg=self.colors['accent'], bg=self.colors['bg_medium'])
        title_label.pack(pady=(40, 10))
        
        # Subtitle
        subtitle = tk.Label(container, text="PAKISTAN SIM DATABASE", 
                           font=self.heading_font,
                           fg=self.colors['text_secondary'], bg=self.colors['bg_medium'])
        subtitle.pack(pady=(0, 30))
        
        # Username
        username_frame = tk.Frame(container, bg=self.colors['bg_medium'])
        username_frame.pack(pady=10)
        
        tk.Label(username_frame, text="👤 USERNAME", font=self.normal_font,
                fg=self.colors['text_secondary'], bg=self.colors['bg_medium']).pack(anchor='w')
        
        self.username_entry = tk.Entry(username_frame, font=self.normal_font,
                                      bg=self.colors['bg_light'], fg=self.colors['text'],
                                      insertbackground=self.colors['accent'],
                                      relief='flat', width=30)
        self.username_entry.pack(pady=5, ipady=8)
        
        # Password
        password_frame = tk.Frame(container, bg=self.colors['bg_medium'])
        password_frame.pack(pady=10)
        
        tk.Label(password_frame, text="🔑 PASSWORD", font=self.normal_font,
                fg=self.colors['text_secondary'], bg=self.colors['bg_medium']).pack(anchor='w')
        
        self.password_entry = tk.Entry(password_frame, font=self.normal_font,
                                      bg=self.colors['bg_light'], fg=self.colors['text'],
                                      insertbackground=self.colors['accent'],
                                      show='•', relief='flat', width=30)
        self.password_entry.pack(pady=5, ipady=8)
        
        # Login button with hover effect
        self.login_btn = tk.Button(container, text="🔓 UNLOCK DATABASE", 
                                  font=self.heading_font,
                                  bg=self.colors['accent'], fg=self.colors['bg_dark'],
                                  relief='flat', cursor='hand2',
                                  activebackground=self.colors['accent_secondary'],
                                  activeforeground='white', width=25, height=2,
                                  command=self.authenticate)
        self.login_btn.pack(pady=30)
        
        # Add hover effect
        self.login_btn.bind('<Enter>', lambda e: self.login_btn.config(bg=self.colors['accent_secondary']))
        self.login_btn.bind('<Leave>', lambda e: self.login_btn.config(bg=self.colors['accent']))
        
        # Status label for animations
        self.login_status = tk.Label(container, text="", font=self.small_font,
                                    fg=self.colors['text_secondary'], bg=self.colors['bg_medium'])
        self.login_status.pack()
        
        # Bind Enter key
        self.username_entry.bind('<Return>', lambda e: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda e: self.authenticate())
        
        # Animate entry focus
        self.username_entry.bind('<FocusIn>', lambda e: self.animate_entry(self.username_entry, True))
        self.username_entry.bind('<FocusOut>', lambda e: self.animate_entry(self.username_entry, False))
        self.password_entry.bind('<FocusIn>', lambda e: self.animate_entry(self.password_entry, True))
        self.password_entry.bind('<FocusOut>', lambda e: self.animate_entry(self.password_entry, False))
    
    def animate_entry(self, entry, focus_in):
        """Animate entry field on focus"""
        if focus_in:
            entry.config(highlightbackground=self.colors['accent'], highlightthickness=2)
        else:
            entry.config(highlightbackground=self.colors['bg_light'], highlightthickness=1)
    
    def authenticate(self):
        """Authenticate user with animation"""
        # Special credentials for demo
        if self.username_entry.get() == "HOWLER" and self.password_entry.get() == "PAK@2024":
            self.login_status.config(text="✓ ACCESS GRANTED", fg=self.colors['success'])
            self.window.after(1000, self.show_main_menu)
        else:
            self.login_status.config(text="✗ ACCESS DENIED", fg=self.colors['error'])
            self.shake_window()
    
    def shake_window(self):
        """Shake window animation for wrong password"""
        original_x = self.window.winfo_x()
        for i in range(3):
            self.window.geometry(f"+{original_x + 10}+{self.window.winfo_y()}")
            self.window.update()
            self.window.after(50)
            self.window.geometry(f"+{original_x - 10}+{self.window.winfo_y()}")
            self.window.update()
            self.window.after(50)
        self.window.geometry(f"+{original_x}+{self.window.winfo_y()}")
    
    def show_main_menu(self):
        """Show main menu with animations"""
        # Clear login screen
        for widget in self.window.winfo_children():
            if widget != self.window.winfo_children()[0]:
                widget.destroy()
        
        # Main container
        main_frame = tk.Frame(self.window, bg=self.colors['bg_dark'])
        main_frame.pack(fill='both', expand=True)
        self.current_frame = main_frame
        
        # Header with animated gradient
        header = tk.Frame(main_frame, bg='#1a2538', height=80)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Title with animation
        title_label = tk.Label(header, text="🇵🇰 PAKISTAN SIM DATABASE", 
                              font=self.title_font,
                              fg=self.colors['accent'], bg='#1a2538')
        title_label.pack(side='left', padx=30, pady=20)
        
        # Time display
        self.time_label = tk.Label(header, text="", font=self.normal_font,
                                  fg=self.colors['text_secondary'], bg='#1a2538')
        self.time_label.pack(side='right', padx=30, pady=20)
        self.update_time()
        
        # Menu buttons container
        menu_container = tk.Frame(main_frame, bg=self.colors['bg_dark'])
        menu_container.pack(pady=30)
        
        # Menu buttons with icons and hover effects
        buttons = [
            ("🔍 LOOKUP SIM", self.show_lookup_screen),
            ("📖 USAGE GUIDE", self.show_usage),
            ("👨‍💻 DEVELOPER", self.show_developer),
            ("🚪 EXIT", self.close_app)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(menu_container, text=text, font=self.heading_font,
                          bg=self.colors['bg_medium'], fg=self.colors['text'],
                          relief='flat', cursor='hand2', width=20, height=2,
                          activebackground=self.colors['accent'],
                          activeforeground=self.colors['bg_dark'],
                          command=command)
            btn.grid(row=i, column=0, pady=10, padx=50)
            
            # Animated hover effect
            btn.bind('<Enter>', lambda e, b=btn: self.animate_button(b, True))
            btn.bind('<Leave>', lambda e, b=btn: self.animate_button(b, False))
    
    def animate_button(self, button, hover):
        """Animate button on hover"""
        if hover:
            button.config(bg=self.colors['accent'], fg=self.colors['bg_dark'])
        else:
            button.config(bg=self.colors['bg_medium'], fg=self.colors['text'])
    
    def update_time(self):
        """Update time display"""
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.time_label.config(text=f"{current_date} | {current_time}")
        self.window.after(1000, self.update_time)
    
    def show_lookup_screen(self):
        """Show SIM lookup screen with animations"""
        # Clear main frame
        for widget in self.current_frame.winfo_children():
            if widget != self.current_frame.winfo_children()[0]:
                widget.destroy()
        
        main_frame = self.current_frame
        
        # Back button
        back_btn = tk.Button(main_frame, text="← BACK", font=self.normal_font,
                           bg=self.colors['bg_medium'], fg=self.colors['text'],
                           relief='flat', cursor='hand2', command=self.show_main_menu)
        back_btn.place(x=20, y=100)
        
        # Search container
        search_frame = tk.Frame(main_frame, bg=self.colors['bg_medium'],
                               highlightbackground=self.colors['accent'],
                               highlightthickness=2)
        search_frame.pack(pady=50, padx=50, fill='x')
        
        # Title
        tk.Label(search_frame, text="📱 SIM NUMBER LOOKUP", 
                font=self.heading_font,
                fg=self.colors['accent'], bg=self.colors['bg_medium']).pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(search_frame, bg=self.colors['bg_medium'])
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="ENTER PHONE NUMBER:", font=self.normal_font,
                fg=self.colors['text_secondary'], bg=self.colors['bg_medium']).pack(anchor='w')
        
        # Phone entry with auto-format
        self.phone_entry = tk.Entry(input_frame, font=('Helvetica', 14),
                                   bg=self.colors['bg_light'], fg=self.colors['text'],
                                   insertbackground=self.colors['accent'],
                                   relief='flat', width=30)
        self.phone_entry.pack(pady=10, ipady=10)
        self.phone_entry.bind('<KeyRelease>', self.auto_format_number)
        
        # Search button
        search_btn = tk.Button(input_frame, text="🔍 SEARCH DATABASE", 
                             font=self.heading_font,
                             bg=self.colors['accent'], fg=self.colors['bg_dark'],
                             relief='flat', cursor='hand2', width=20, height=2,
                             command=self.search_sim)
        search_btn.pack(pady=20)
        
        # Results frame (initially hidden)
        self.results_frame = tk.Frame(main_frame, bg=self.colors['bg_dark'])
        self.results_frame.pack(fill='both', expand=True, padx=50, pady=20)
    
    def auto_format_number(self, event=None):
        """Auto-format phone number as user types"""
        number = self.phone_entry.get()
        # Remove non-digits
        number = re.sub(r'\D', '', number)
        
        # Format based on length
        if len(number) > 0:
            if len(number) <= 4:
                formatted = number
            elif len(number) <= 7:
                formatted = f"{number[:4]} {number[4:]}"
            elif len(number) <= 10:
                formatted = f"{number[:4]} {number[4:7]} {number[7:]}"
            else:
                formatted = f"{number[:4]} {number[4:7]} {number[7:11]}"
            
            # Update entry without triggering event
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, formatted)
    
    def search_sim(self):
        """Search SIM database with animation"""
        # Get phone number and clean it
        phone = self.phone_entry.get()
        phone = re.sub(r'\D', '', phone)
        
        if not phone:
            messagebox.showwarning("Warning", "Please enter a phone number")
            return
        
        # Show loading animation
        loading_label = tk.Label(self.results_frame, text="🔍 SEARCHING DATABASE...", 
                                font=self.heading_font,
                                fg=self.colors['accent'], bg=self.colors['bg_dark'])
        loading_label.pack(pady=20)
        self.window.update()
        
        # Search in thread
        threading.Thread(target=self.perform_search, args=(phone, loading_label)).start()
    
    def perform_search(self, phone, loading_label):
        """Perform actual API search"""
        try:
            # Call API
            response = requests.get(f"{self.api_base}{phone}", timeout=10)
            data = response.json()
            
            # Remove loading label
            self.window.after(0, loading_label.destroy)
            
            if data.get('success'):
                self.window.after(0, self.display_results, data)
            else:
                self.window.after(0, lambda: messagebox.showerror("Error", "No data found for this number"))
        except Exception as e:
            self.window.after(0, loading_label.destroy)
            self.window.after(0, lambda: messagebox.showerror("Error", f"API Error: {str(e)}"))
    
    def display_results(self, data):
        """Display search results with animations"""
        # Clear results frame
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Results count
        count = data.get('count', 0)
        count_label = tk.Label(self.results_frame, 
                              text=f"📊 FOUND {count} RECORD(S)", 
                              font=self.heading_font,
                              fg=self.colors['success'], bg=self.colors['bg_dark'])
        count_label.pack(pady=10)
        
        # Create scrollable frame for results
        canvas = tk.Canvas(self.results_frame, bg=self.colors['bg_dark'], 
                          highlightbackground=self.colors['bg_medium'])
        scrollbar = tk.Scrollbar(self.results_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_dark'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display each result with animations
        for i, result in enumerate(data.get('result', [])):
            self.create_result_card(scrollable_frame, result, i)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Developer credit
        dev_label = tk.Label(self.results_frame, 
                            text=f"Developer: {data.get('Developer', 'NIGHT-HOWLER')}",
                            font=self.small_font,
                            fg=self.colors['text_secondary'], bg=self.colors['bg_dark'])
        dev_label.pack(pady=5)
    
    def create_result_card(self, parent, result, index):
        """Create animated result card"""
        # Card frame
        card = tk.Frame(parent, bg=self.colors['bg_medium'],
                       highlightbackground=self.colors['accent'],
                       highlightthickness=1)
        card.pack(fill='x', pady=10, padx=20)
        
        # Add hover effect
        def on_enter(e):
            card.config(highlightbackground=self.colors['accent'], highlightthickness=2)
            e.widget.config(bg=self.colors['bg_light'])
        
        def on_leave(e):
            card.config(highlightbackground=self.colors['bg_medium'], highlightthickness=1)
            e.widget.config(bg=self.colors['bg_medium'])
        
        card.bind('<Enter>', on_enter)
        card.bind('<Leave>', on_leave)
        
        # Fields with icons
        fields = [
            ("📱 Mobile", result.get('mobile', 'N/A')),
            ("👤 Name", result.get('name', 'N/A')),
            ("🆔 CNIC", result.get('cnic', 'N/A')),
            ("📍 Address", result.get('address', 'N/A')),
            ("🌍 Country", result.get('country', 'N/A'))
        ]
        
        for label, value in fields:
            field_frame = tk.Frame(card, bg=self.colors['bg_medium'])
            field_frame.pack(fill='x', pady=5, padx=15)
            
            tk.Label(field_frame, text=label, font=self.normal_font,
                    fg=self.colors['accent'], bg=self.colors['bg_medium'],
                    width=10, anchor='w').pack(side='left')
            
            tk.Label(field_frame, text=value, font=self.normal_font,
                    fg=self.colors['text'], bg=self.colors['bg_medium'],
                    wraplength=400, justify='left').pack(side='left', padx=(10, 0))
    
    def show_usage(self):
        """Show usage guide"""
        # Clear main frame
        for widget in self.current_frame.winfo_children():
            if widget != self.current_frame.winfo_children()[0]:
                widget.destroy()
        
        main_frame = self.current_frame
        
        # Back button
        back_btn = tk.Button(main_frame, text="← BACK", font=self.normal_font,
                           bg=self.colors['bg_medium'], fg=self.colors['text'],
                           relief='flat', cursor='hand2', command=self.show_main_menu)
        back_btn.place(x=20, y=100)
        
        # Usage container
        usage_frame = tk.Frame(main_frame, bg=self.colors['bg_medium'],
                              highlightbackground=self.colors['accent'],
                              highlightthickness=2)
        usage_frame.pack(pady=50, padx=100, fill='both', expand=True)
        
        # Title
        tk.Label(usage_frame, text="📖 USAGE GUIDE", 
                font=self.heading_font,
                fg=self.colors['accent'], bg=self.colors['bg_medium']).pack(pady=20)
        
        # Usage text
        usage_text = """
        🔍 SIM DATABASE LOOKUP TOOL
        
        1️⃣ Enter a Pakistani phone number in the search field
        2️⃣ The tool will automatically format the number
        3️⃣ Click 'SEARCH DATABASE' to query the API
        4️⃣ Results will display all associated SIM records
        
        📋 FEATURES:
        • Real-time number formatting
        • Animated search results
        • Scrollable result cards
        • Hover effects on all elements
        
        ⚠️ NOTE:
        • Use for educational purposes only
        • Respect privacy and data protection laws
        • Data provided by NIGHT-HOWLER API
        """
        
        text_widget = tk.Text(usage_frame, font=self.normal_font,
                            bg=self.colors['bg_light'], fg=self.colors['text'],
                            wrap='word', height=15, width=50,
                            relief='flat', padx=20, pady=20)
        text_widget.pack(pady=20, padx=20)
        text_widget.insert('1.0', usage_text)
        text_widget.config(state='disabled')
    
    def show_developer(self):
        """Show developer information"""
        # Clear main frame
        for widget in self.current_frame.winfo_children():
            if widget != self.current_frame.winfo_children()[0]:
                widget.destroy()
        
        main_frame = self.current_frame
        
        # Back button
        back_btn = tk.Button(main_frame, text="← BACK", font=self.normal_font,
                           bg=self.colors['bg_medium'], fg=self.colors['text'],
                           relief='flat', cursor='hand2', command=self.show_main_menu)
        back_btn.place(x=20, y=100)
        
        # Developer container
        dev_frame = tk.Frame(main_frame, bg=self.colors['bg_medium'],
                            highlightbackground=self.colors['accent'],
                            highlightthickness=2)
        dev_frame.pack(pady=50, padx=100, fill='both', expand=True)
        
        # Title
        tk.Label(dev_frame, text="👨‍💻 DEVELOPER INFO", 
                font=self.heading_font,
                fg=self.colors['accent'], bg=self.colors['bg_medium']).pack(pady=20)
        
        # Developer info
        info_frame = tk.Frame(dev_frame, bg=self.colors['bg_light'])
        info_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        info_text = """
        ╔══════════════════════════════╗
        ║     NIGHT-HOWLER DATABASE    ║
        ╠══════════════════════════════╣
        ║  Lead Developer: NIGHT-HOWLER ║
        ║  Version: 2.0.0              ║
        ║  Release Date: 2024          ║
        ║  Framework: Python Tkinter   ║
        ║  API: Custom Database API     ║
        ╚══════════════════════════════╝
        
        ✨ SPECIAL THANKS
        • All users of this tool
        • Open source community
        • Pakistani developers
        
        📧 Contact: howler@database.pk
        🌐 Web: www.howler-database.pk
        
        ⚡ "Empowering Pakistani Digital Identity"
        """
        
        text_widget = tk.Text(info_frame, font=('Courier', 11),
                            bg=self.colors['bg_light'], fg=self.colors['accent'],
                            wrap='word', height=15, width=50,
                            relief='flat', padx=20, pady=20)
        text_widget.pack(pady=20, padx=20)
        text_widget.insert('1.0', info_text)
        text_widget.config(state='disabled')
    
    def run(self):
        """Run the application"""
        self.window.mainloop()

if __name__ == "__main__":
    app = AnimatedSIMDatabaseTool()
    app.run()