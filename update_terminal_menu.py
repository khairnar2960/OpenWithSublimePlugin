import sublime
import sublime_plugin
import os
import subprocess
import platform
import json
import shutil
from .search_php_versions import build_php_menu

def plugin_loaded():
    # Load package settings
    settings = sublime.load_settings("OpenWith.sublime-settings")

    # Check if the command has already been executed
    if not settings.get("update_menu_executed", False):
        sublime.active_window().run_command("update_terminal_menu")

        # Set the flag so it doesn't run again on restart
        settings.set("update_menu_executed", True)
        sublime.save_settings("OpenWith.sublime-settings")

class UpdateTerminalMenuCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        if not os.path.exists('Context.sublime-menu'):
            terminals = self.get_available_terminals()

            menu_structure = [
                {
                    "caption": "Open With",
                    "children": [
                        {
                            "caption": "Terminal",
                            "children": [
                                {"command": "open_terminal", "args": {"terminal": term}, "caption": term}
                                for term in terminals.keys()
                            ]
                        },
                        {
                            "caption": "Choose",
                            "command": "open_with_app"
                        }
                    ]
                }
            ]

            php_menu = build_php_menu()

            if php_menu:
                menu_structure[0]['children'].append(php_menu)

            menu_structure[0]['children'].append({
                "caption": "Settings",
                "command": "open_file",
                "args": {
                    "file": "${packages}/User/OpenWith.sublime-settings"
                }
            })

            menu_structure[0]['children'].append({
                "caption": "Reload",
                "command": "update_terminal_menu"
            })
            menuOptions = ['Context', 'Tab Context']
            for menuOption in menuOptions:
                menu_path = os.path.join(sublime.packages_path(), "OpenWith", f"{menuOption}.sublime-menu")
                with open(menu_path, "w") as menu_file:
                    json.dump(menu_structure, menu_file, indent=4)

            sublime.message_dialog("OpenWith menu updated! Restart Sublime to apply changes.")

    def get_available_terminals(self):
        terminals = {}

        system = platform.system()
        if system == "Windows":
            possible_terminals = {
                "Command Prompt": "cmd.exe",
                "PowerShell": "powershell.exe",
                "Git Bash": "C:\\Program Files\\Git\\bin\\bash.exe",
                "Windows Terminal": "wt.exe"
            }
        elif system == "Darwin":  # macOS
            possible_terminals = {
                "Terminal": "open -a Terminal",
                "iTerm2": "open -a iTerm"
            }
        else:  # Linux
            try:
                terminal_list = subprocess.check_output("compgen -c | grep -E 'bash|zsh|konsole|gnome-terminal|xfce4-terminal'", shell=True).decode().split("\n")
                possible_terminals = {term: term for term in terminal_list if term}
            except Exception:
                possible_terminals = {}

        for name, command in possible_terminals.items():
            if self.is_executable(command):
                terminals[name] = command

        return terminals

    def is_executable(self, cmd):
        """Checks if a terminal executable exists without opening it."""
        if isinstance(cmd, list):
            cmd = cmd[0]  # Extract executable name from list
        return shutil.which(cmd) is not None
