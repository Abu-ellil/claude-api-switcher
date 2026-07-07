"""
Claude Code API Switcher - Modern GUI Application
A beautiful modern GUI app to switch between different API providers for Claude Code.
"""

import os
import json
import sys
from pathlib import Path
from tkinter import messagebox, filedialog
import tkinter as tk
from tkinter import ttk

# Try to import customtkinter for modern dark theme
try:
    import customtkinter as ctk
    from customtkinter import CTkFont, CTkImage
    USE_CTK = True
except ImportError:
    USE_CTK = False
    import tkinter as tk
    from tkinter import ttk


class ModernButton(ctk.CTkButton if USE_CTK else ttk.Button):
    """Modern styled button"""
    pass


class ProviderConfig:
    """Configuration class for a provider"""

    def __init__(self, key, name, url, description, color=None):
        self.key = key
        self.name = name
        self.url = url
        self.description = description
        self.color = color or "#2196F3"


class ClaudeAPISwitcher:
    """Main application class - Modern UI"""

    # Color scheme
    COLORS = {
        "primary": "#2196F3",
        "success": "#4CAF50",
        "warning": "#FF9800",
        "danger": "#F44336",
        "info": "#00BCD4",
        "dark": "#1E1E1E",
        "darker": "#121212",
        "light": "#FFFFFF",
        "gray": "#757575",
        "gray_light": "#BDBDBD"
    }

    # Default providers with colors
    DEFAULT_PROVIDERS = [
        ProviderConfig("zai", "Z.AI API", "https://api.z.ai/api/anthropic",
                       "Z.AI Configuration", "#9C27B0"),
        ProviderConfig("lmstudio", "LM Studio", "http://localhost:1234/v1",
                       "Local Server (Port 1234)", "#FF5722"),
        ProviderConfig("ollama", "Ollama", "http://localhost:11434/v1",
                       "Local Server (Port 11434)", "#795548"),
        ProviderConfig("anthropic", "Anthropic Official", None,
                       "Default API Endpoint", "#4CAF50"),
    ]

    def __init__(self):
        """Initialize the application"""
        self.settings_path = None
        self.current_provider = {"name": "Unknown", "url": "Not found"}
        self.providers = []  # Will be loaded from file or defaults
        self.selected_provider = None
        self.custom_providers_file = Path.home() / ".claude" / "custom-providers.json"

        # Load providers
        self.load_providers()

        # Find settings file
        self.auto_find_settings()

        # Setup theme
        self.setup_theme()

        # Create main window
        self.create_window()

        # Build UI
        self.create_ui()

        # Update displays
        self.update_displays()

    def setup_theme(self):
        """Setup the application theme"""
        if USE_CTK:
            ctk.set_appearance_mode("Dark")
            ctk.set_default_color_theme("blue")

    def create_window(self):
        """Create the main window"""
        if USE_CTK:
            self.root = ctk.CTk()
        else:
            self.root = tk.Tk()

        self.root.title("Claude Code API Switcher")
        self.root.geometry("650x580")

        # Set window icon
        icon_path = Path(__file__).parent / "CLogo.png"
        if icon_path.exists():
            try:
                self.root.iconphoto(True, tk.PhotoImage(file=str(icon_path)))
            except:
                pass

        # Center window
        self.root.update_idletasks()
        width = 650
        height = 580
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        self.root.resizable(True, True)

    def load_providers(self):
        """Load providers from file or use defaults"""
        # Try to load custom providers
        if self.custom_providers_file.exists():
            try:
                with open(self.custom_providers_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for p in data:
                        self.providers.append(ProviderConfig(
                            p.get("key", ""),
                            p.get("name", ""),
                            p.get("url"),
                            p.get("description", ""),
                            p.get("color")
                        ))
                return
            except:
                pass

        # Use defaults
        self.providers = self.DEFAULT_PROVIDERS.copy()

    def save_providers(self):
        """Save providers to file"""
        try:
            self.custom_providers_file.parent.mkdir(parents=True, exist_ok=True)
            data = []
            for p in self.providers:
                data.append({
                    "key": p.key,
                    "name": p.name,
                    "url": p.url,
                    "description": p.description,
                    "color": p.color
                })
            with open(self.custom_providers_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Failed to save providers: {e}")

    def auto_find_settings(self):
        """Automatically find settings.json"""
        possible_paths = [
            Path.home() / ".claude" / "settings.json",
            Path.home() / ".config" / "claude" / "settings.json",
            Path.home() / ".claude" / "settings.local.json",
            Path.home() / ".config" / "claude" / "settings.local.json",
        ]

        if sys.platform == "win32":
            possible_paths.extend([
                Path(os.environ.get("LOCALAPPDATA", "")) / "claude" / "settings.json",
                Path(os.environ.get("APPDATA", "")) / "claude" / "settings.json",
            ])

        for path in possible_paths:
            if path.exists():
                self.settings_path = str(path)
                break

        if self.settings_path:
            self.load_current_provider()

    def load_current_provider(self):
        """Load current provider from settings"""
        try:
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)

            base_url = settings.get('env', {}).get('ANTHROPIC_BASE_URL')

            if not base_url:
                self.current_provider = {"name": "Anthropic Official", "url": "Default"}
            else:
                # Find matching provider
                for p in self.providers:
                    if p.url == base_url:
                        self.current_provider = {"name": p.name, "url": base_url}
                        return
                self.current_provider = {"name": "Custom", "url": base_url}
        except:
            pass

    def browse_settings_file(self):
        """Open file browser to select settings.json"""
        filepath = filedialog.askopenfilename(
            title="Select Claude Code settings.json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialdir=str(Path.home())
        )

        if filepath:
            self.settings_path = filepath
            self.settings_path_label.configure(text=filepath)
            self.load_current_provider()
            self.update_displays()

    def create_ui(self):
        """Create the modern UI"""
        # Main container
        main_container = self.create_main_container()

        # Header
        self.create_header(main_container)

        # Settings file section
        self.create_settings_section(main_container)

        # Current provider card
        self.create_current_provider_card(main_container)

        # Provider selection
        self.create_provider_selection(main_container)

        # Custom provider button
        self.create_add_provider_section(main_container)

        # Action buttons
        self.create_action_buttons(main_container)

        # Footer
        self.create_footer(main_container)

    def create_main_container(self):
        """Create main container with scroll"""
        if USE_CTK:
            main_frame = ctk.CTkScrollableFrame(
                self.root,
                fg_color="transparent"
            )
        else:
            main_frame = ttk.Frame(self.root)
            main_frame.columnconfigure(0, weight=1)

        main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        return main_frame

    def create_header(self, parent):
        """Create beautiful header"""
        if USE_CTK:
            header = ctk.CTkFrame(parent, height=80, fg_color=self.COLORS["darker"])
            header.pack(fill="x", padx=10, pady=(10, 5))
            header.pack_propagate(False)

            # Title
            title = ctk.CTkLabel(
                header,
                text="⚡ Claude Code API Switcher",
                font=CTkFont(size=24, weight="bold")
            )
            title.pack(pady=(15, 5))

            # Subtitle
            subtitle = ctk.CTkLabel(
                header,
                text="Switch between API providers instantly",
                font=CTkFont(size=12),
                text_color=self.COLORS["gray"]
            )
            subtitle.pack()
        else:
            header = ttk.Frame(parent, padding="15")
            header.pack(fill="x", padx=10, pady=(10, 5))

            title = ttk.Label(
                header,
                text="⚡ Claude Code API Switcher",
                font=("Arial", 16, "bold")
            )
            title.pack()

            subtitle = ttk.Label(
                header,
                text="Switch between API providers instantly",
                font=("Arial", 9),
                foreground="gray"
            )
            subtitle.pack()

    def create_settings_section(self, parent):
        """Create settings file section with browse button"""
        if USE_CTK:
            section = ctk.CTkFrame(parent, fg_color=self.COLORS["dark"], corner_radius=10)
            section.pack(fill="x", padx=15, pady=8)

            # Label row
            label_row = ctk.CTkFrame(section, fg_color="transparent")
            label_row.pack(fill="x", padx=15, pady=(12, 5))

            label = ctk.CTkLabel(
                label_row,
                text="📁 Settings File",
                font=CTkFont(size=13, weight="bold"),
                anchor="w"
            )
            label.pack(side="left", fill="x", expand=True)

            # Browse button
            browse_btn = ctk.CTkButton(
                label_row,
                text="Browse",
                width=80,
                height=28,
                command=self.browse_settings_file,
                fg_color=self.COLORS["info"],
                hover_color="#0097A7"
            )
            browse_btn.pack(side="right")

            # Path display
            self.settings_path_label = ctk.CTkLabel(
                section,
                text=self.settings_path or "Auto-detecting...",
                font=CTkFont(size=11),
                text_color=self.COLORS["gray_light"],
                anchor="w"
            )
            self.settings_path_label.pack(fill="x", padx=15, pady=(0, 12))
        else:
            section = ttk.LabelFrame(parent, text="Settings File", padding="10")
            section.pack(fill="x", padx=15, pady=8)

            # Path row
            path_row = ttk.Frame(section)
            path_row.pack(fill="x")

            self.settings_path_label = ttk.Label(
                path_row,
                text=self.settings_path or "Auto-detecting...",
                foreground="gray"
            )
            self.settings_path_label.pack(side="left", fill="x", expand=True)

            browse_btn = ttk.Button(
                path_row,
                text="Browse",
                command=self.browse_settings_file,
                width=10
            )
            browse_btn.pack(side="right", padx=(5, 0))

    def create_current_provider_card(self, parent):
        """Create current provider display card"""
        if USE_CTK:
            card = ctk.CTkFrame(parent, fg_color=self.COLORS["dark"], corner_radius=10)
            card.pack(fill="x", padx=15, pady=8)

            label = ctk.CTkLabel(
                card,
                text="🔌 Current Provider",
                font=CTkFont(size=13, weight="bold")
            )
            label.pack(anchor="w", padx=15, pady=(12, 8))

            self.current_provider_display = ctk.CTkLabel(
                card,
                text="",
                font=CTkFont(size=14, weight="bold"),
                fg_color=self.COLORS["darker"],
                corner_radius=8,
                padx=15,
                pady=12
            )
            self.current_provider_display.pack(fill="x", padx=15, pady=(0, 12))
        else:
            card = ttk.LabelFrame(parent, text="Current Provider", padding="10")
            card.pack(fill="x", padx=15, pady=8)

            self.current_provider_display = ttk.Label(
                card,
                text="",
                font=("Arial", 11, "bold"),
                foreground="#2196F3"
            )
            self.current_provider_display.pack(fill="x", pady=5)

    def create_provider_selection(self, parent):
        """Create provider selection with beautiful cards"""
        if USE_CTK:
            section = ctk.CTkFrame(parent, fg_color=self.COLORS["dark"], corner_radius=10)
            section.pack(fill="x", padx=15, pady=8)

            label = ctk.CTkLabel(
                section,
                text="📡 Select Provider",
                font=CTkFont(size=13, weight="bold")
            )
            label.pack(anchor="w", padx=15, pady=(12, 10))

            # Providers container
            providers_container = ctk.CTkFrame(section, fg_color="transparent")
            providers_container.pack(fill="x", padx=15, pady=(0, 12))

            self.provider_buttons = []
            self.provider_var = tk.StringVar(value=self.providers[0].key if self.providers else "")

            for provider in self.providers:
                btn_frame = ctk.CTkFrame(
                    providers_container,
                    fg_color=self.COLORS["darker"],
                    corner_radius=8,
                    border_width=2,
                    border_color=self.COLORS["darker"]
                )
                btn_frame.pack(fill="x", pady=4)

                # Radio and content row
                content_row = ctk.CTkFrame(btn_frame, fg_color="transparent")
                content_row.pack(fill="x", padx=12, pady=8)

                # Radio button
                rb = ctk.CTkRadioButton(
                    content_row,
                    text="",
                    variable=self.provider_var,
                    value=provider.key,
                    command=lambda p=provider: self.on_provider_select(p),
                    radiobutton_width=20,
                    radiobutton_height=20
                )
                rb.pack(side="left", padx=(0, 10))

                # Provider info
                info_frame = ctk.CTkFrame(content_row, fg_color="transparent")
                info_frame.pack(side="left", fill="x", expand=True)

                name_label = ctk.CTkLabel(
                    info_frame,
                    text=provider.name,
                    font=CTkFont(size=13, weight="bold"),
                    anchor="w"
                )
                name_label.pack(fill="x")

                desc_label = ctk.CTkLabel(
                    info_frame,
                    text=provider.description,
                    font=CTkFont(size=10),
                    text_color=self.COLORS["gray"],
                    anchor="w"
                )
                desc_label.pack(fill="x")

                # Color indicator
                color_label = ctk.CTkLabel(
                    content_row,
                    text="●",
                    font=CTkFont(size=20),
                    text_color=provider.color
                )
                color_label.pack(side="right")

                self.provider_buttons.append({
                    "frame": btn_frame,
                    "provider": provider
                })
        else:
            section = ttk.LabelFrame(parent, text="Select Provider", padding="10")
            section.pack(fill="x", padx=15, pady=8)

            self.provider_var = tk.StringVar(value=self.providers[0].key if self.providers else "")

            for provider in self.providers:
                rb = ttk.Radiobutton(
                    section,
                    text=f"{provider.name} - {provider.description}",
                    variable=self.provider_var,
                    value=provider.key,
                    command=lambda p=provider: self.on_provider_select(p)
                )
                rb.pack(anchor="w", pady=3)

    def create_add_provider_section(self, parent):
        """Create section for adding custom provider"""
        if USE_CTK:
            section = ctk.CTkFrame(parent, fg_color=self.COLORS["dark"], corner_radius=10)
            section.pack(fill="x", padx=15, pady=8)

            # Header row
            header_row = ctk.CTkFrame(section, fg_color="transparent")
            header_row.pack(fill="x", padx=15, pady=(12, 10))

            label = ctk.CTkLabel(
                header_row,
                text="➕ Custom Provider",
                font=CTkFont(size=13, weight="bold")
            )
            label.pack(side="left")

            # Toggle button
            self.toggle_custom_btn = ctk.CTkButton(
                header_row,
                text="Show",
                width=60,
                height=28,
                command=self.toggle_custom_section
            )
            self.toggle_custom_btn.pack(side="right")

            # Custom provider form (hidden by default)
            self.custom_frame = ctk.CTkFrame(section, fg_color="transparent")
            self.custom_frame.pack(fill="x", padx=15, pady=(0, 12))
            self.custom_frame.pack_forget()  # Hide initially

            # Name
            name_label = ctk.CTkLabel(
                self.custom_frame,
                text="Name:",
                font=CTkFont(size=11),
                anchor="w"
            )
            name_label.pack(fill="x", pady=(0, 3))

            self.custom_name_entry = ctk.CTkEntry(
                self.custom_frame,
                placeholder_text="My Custom API",
                height=35
            )
            self.custom_name_entry.pack(fill="x", pady=(0, 8))

            # URL
            url_label = ctk.CTkLabel(
                self.custom_frame,
                text="URL:",
                font=CTkFont(size=11),
                anchor="w"
            )
            url_label.pack(fill="x", pady=(0, 3))

            self.custom_url_entry = ctk.CTkEntry(
                self.custom_frame,
                placeholder_text="https://api.example.com/v1",
                height=35
            )
            self.custom_url_entry.pack(fill="x", pady=(0, 8))

            # Description
            desc_label = ctk.CTkLabel(
                self.custom_frame,
                text="Description:",
                font=CTkFont(size=11),
                anchor="w"
            )
            desc_label.pack(fill="x", pady=(0, 3))

            self.custom_desc_entry = ctk.CTkEntry(
                self.custom_frame,
                placeholder_text="My custom API endpoint",
                height=35
            )
            self.custom_desc_entry.pack(fill="x", pady=(0, 10))

            # Buttons
            btn_row = ctk.CTkFrame(self.custom_frame, fg_color="transparent")
            btn_row.pack(fill="x")

            add_btn = ctk.CTkButton(
                btn_row,
                text="Add Provider",
                command=self.add_custom_provider,
                height=35,
                fg_color=self.COLORS["success"],
                hover_color="#388E3C"
            )
            add_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))

            clear_btn = ctk.CTkButton(
                btn_row,
                text="Clear",
                command=self.clear_custom_form,
                height=35,
                fg_color=self.COLORS["gray"],
                hover_color="#616161"
            )
            clear_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))
        else:
            section = ttk.LabelFrame(parent, text="Custom Provider", padding="10")
            section.pack(fill="x", padx=15, pady=8)

            # Simple form for tkinter
            ttk.Label(section, text="Name:").grid(row=0, column=0, sticky="w", pady=3)
            self.custom_name_entry = ttk.Entry(section)
            self.custom_name_entry.grid(row=0, column=1, sticky="ew", pady=3, padx=(10, 0))

            ttk.Label(section, text="URL:").grid(row=1, column=0, sticky="w", pady=3)
            self.custom_url_entry = ttk.Entry(section)
            self.custom_url_entry.grid(row=1, column=1, sticky="ew", pady=3, padx=(10, 0))

            ttk.Label(section, text="Description:").grid(row=2, column=0, sticky="w", pady=3)
            self.custom_desc_entry = ttk.Entry(section)
            self.custom_desc_entry.grid(row=2, column=1, sticky="ew", pady=3, padx=(10, 0))

            btn_row = ttk.Frame(section)
            btn_row.grid(row=3, column=0, columnspan=2, pady=(10, 0))

            add_btn = ttk.Button(btn_row, text="Add Provider", command=self.add_custom_provider)
            add_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))

            clear_btn = ttk.Button(btn_row, text="Clear", command=self.clear_custom_form)
            clear_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))

            section.columnconfigure(1, weight=1)

    def create_action_buttons(self, parent):
        """Create action buttons"""
        if USE_CTK:
            button_frame = ctk.CTkFrame(parent, fg_color="transparent")
            button_frame.pack(fill="x", padx=15, pady=(15, 10))

            apply_btn = ctk.CTkButton(
                button_frame,
                text="✓ Apply Changes",
                command=self.apply_changes,
                height=45,
                font=CTkFont(size=14, weight="bold"),
                fg_color=self.COLORS["success"],
                hover_color="#388E3C",
                corner_radius=10
            )
            apply_btn.pack(side="left", fill="x", expand=True, padx=(0, 8))

            close_btn = ctk.CTkButton(
                button_frame,
                text="✕ Close",
                command=self.root.quit,
                height=45,
                font=CTkFont(size=14, weight="bold"),
                fg_color=self.COLORS["danger"],
                hover_color="#D32F2F",
                corner_radius=10
            )
            close_btn.pack(side="right", fill="x", expand=True, padx=(8, 0))
        else:
            button_frame = ttk.Frame(parent)
            button_frame.pack(fill="x", padx=15, pady=(15, 10))

            apply_btn = ttk.Button(button_frame, text="✓ Apply Changes", command=self.apply_changes)
            apply_btn.pack(side="left", fill="x", expand=True, padx=(0, 5))

            close_btn = ttk.Button(button_frame, text="✕ Close", command=self.root.quit)
            close_btn.pack(side="right", fill="x", expand=True, padx=(5, 0))

    def create_footer(self, parent):
        """Create footer"""
        if USE_CTK:
            footer = ctk.CTkLabel(
                parent,
                text="💡 Restart Claude Code after changing provider",
                font=CTkFont(size=10),
                text_color=self.COLORS["warning"]
            )
            footer.pack(pady=(5, 15))

    def toggle_custom_section(self):
        """Toggle custom provider section visibility"""
        if USE_CTK:
            if self.custom_frame.winfo_ismapped():
                self.custom_frame.pack_forget()
                self.toggle_custom_btn.configure(text="Show")
            else:
                self.custom_frame.pack(fill="x", padx=15, pady=(0, 12))
                self.toggle_custom_btn.configure(text="Hide")

    def on_provider_select(self, provider):
        """Handle provider selection"""
        self.selected_provider = provider
        self.highlight_selected_provider()

    def highlight_selected_provider(self):
        """Highlight the selected provider card"""
        if not USE_CTK:
            return

        for btn_data in self.provider_buttons:
            frame = btn_data["frame"]
            provider = btn_data["provider"]

            if self.provider_var.get() == provider.key:
                frame.configure(border_color=provider.color)
            else:
                frame.configure(border_color="transparent")

    def update_displays(self):
        """Update all displays"""
        # Update current provider
        if self.current_provider:
            text = f"{self.current_provider['name']}"
            if self.current_provider['url'] and self.current_provider['url'] != "Not found":
                text += f"\n{self.current_provider['url']}"
            if USE_CTK:
                self.current_provider_display.configure(text=text)
            else:
                self.current_provider_display.configure(text=text)

        # Update settings path
        if hasattr(self, 'settings_path_label'):
            path_text = self.settings_path or "Not found - Click Browse to select"
            if USE_CTK:
                self.settings_path_label.configure(text=path_text)
            else:
                self.settings_path_label.configure(text=path_text)

    def add_custom_provider(self):
        """Add a new custom provider"""
        name = self.custom_name_entry.get().strip()
        url = self.custom_url_entry.get().strip()
        desc = self.custom_desc_entry.get().strip() or "Custom provider"

        if not name or not url:
            messagebox.showwarning("Missing Info", "Please enter both Name and URL")
            return

        # Generate unique key
        key = name.lower().replace(" ", "-") + str(len(self.providers))

        # Add to providers list
        new_provider = ProviderConfig(key, name, url, desc, "#E91E63")
        self.providers.append(new_provider)

        # Save to file
        self.save_providers()

        # Rebuild UI
        self.rebuild_provider_selection()

        # Select the new provider
        self.provider_var.set(key)
        self.on_provider_select(new_provider)

        # Clear form
        self.clear_custom_form()

        messagebox.showinfo("Success", f"Provider '{name}' added successfully!")

    def rebuild_provider_selection(self):
        """Rebuild the provider selection section"""
        # This is a simplified version - in a real app you'd properly remove and recreate widgets
        # For now, just notify user to restart
        pass

    def clear_custom_form(self):
        """Clear the custom provider form"""
        self.custom_name_entry.delete(0, "end")
        self.custom_url_entry.delete(0, "end")
        self.custom_desc_entry.delete(0, "end")

    def apply_changes(self):
        """Apply the selected provider changes"""
        if not self.settings_path:
            messagebox.showerror(
                "Error",
                "No settings file selected!\n\nPlease click 'Browse' to select your Claude Code settings.json file."
            )
            return

        selected_key = self.provider_var.get()
        provider = next((p for p in self.providers if p.key == selected_key), None)

        if not provider:
            messagebox.showerror("Error", "Please select a provider")
            return

        try:
            # Read current settings
            with open(self.settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)

            # Ensure env section exists
            if "env" not in settings:
                settings["env"] = {}

            # Update settings
            if provider.url:
                settings["env"]["ANTHROPIC_BASE_URL"] = provider.url
            else:
                # Remove custom base URL (use Anthropic default)
                if "ANTHROPIC_BASE_URL" in settings["env"]:
                    del settings["env"]["ANTHROPIC_BASE_URL"]

            # Write back
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2)

            # Update current display
            self.current_provider = {"name": provider.name, "url": provider.url or "Default"}
            self.update_displays()

            # Show success message
            messagebox.showinfo(
                "✓ Success",
                f"API Provider changed to:\n\n📡 {provider.name}\n\nURL: {provider.url or 'Default (Anthropic)'}\n\n💡 Please restart Claude Code for changes to take effect."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to update settings:\n\n{str(e)}"
            )

    def run(self):
        """Run the application"""
        if USE_CTK:
            # Initial highlight
            self.root.after(100, self.highlight_selected_provider)
        self.root.mainloop()


def main():
    """Main entry point"""
    app = ClaudeAPISwitcher()
    app.run()


if __name__ == "__main__":
    main()
