import sublime
import sublime_plugin
import os
import subprocess
import platform
import shutil

class OpenTerminalCommand(sublime_plugin.WindowCommand):
    def run(self, terminal=None):
        file_path = self.window.active_view().file_name()
        if file_path:
            dir_path = os.path.dirname(file_path)
            terminals = self.get_available_terminals()

            if terminal in terminals:
                subprocess.Popen(terminals[terminal], cwd=dir_path)
            else:
                sublime.error_message("Invalid terminal selection.")

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

    def input(self, args):
        return TerminalInputHandler(self.get_available_terminals())

class TerminalInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, terminals):
        self.terminals = terminals

    def list_items(self):
        return list(self.terminals.keys())

class OpenWithAppCommand(sublime_plugin.WindowCommand):
    def run(self):
        file_path = self.window.active_view().file_name()
        if file_path:
            system = platform.system()
            if system == "Windows":
                subprocess.Popen(["rundll32.exe", "shell32.dll,OpenAs_RunDLL", file_path])
            elif system == "Darwin":
                subprocess.Popen(["open", file_path])
            else:
                subprocess.Popen(["xdg-open", file_path])

class RunFileWithPhpCommand(sublime_plugin.WindowCommand):
    def run(self, path=None):
        file_path = self.window.active_view().file_name()
        if file_path and file_path.endswith(".php"):
            dir_path = os.path.dirname(file_path)

            if os.path.exists(path):
                system = platform.system()

                terminal = None

                if system == "Windows":
                    terminal = ["powershell", "-NoExit", "-Command"]
                    # terminal = ["cmd", '/k']
                elif system == "Darwin":
                    terminal = ['open', '-a', 'Terminal']
                else:
                    terminal = ["gnome-terminal", "--"]

                if terminal:
                    terminal.append(path)
                    terminal.append(file_path)
                    subprocess.Popen(terminal, cwd=dir_path)
            else:
                sublime.error_message("Invalid php selection.")

class ServeFileWithPhpCommand(sublime_plugin.WindowCommand):
    def run(self, path=None):
        file_path = self.window.active_view().file_name()
        if file_path and file_path.endswith(".php"):
            dir_path = os.path.dirname(file_path)

            if os.path.exists(path):
                subprocess.Popen([path, '-S', '127.0.0.1:8080', file_path], cwd=dir_path)
            else:
                sublime.error_message("Invalid php selection.")

class ServeDirWithPhpCommand(sublime_plugin.WindowCommand):
    def run(self, path=None):
        file_path = self.window.active_view().file_name()
        if file_path:
            dir_path = os.path.dirname(file_path)

            if os.path.exists(path):
                subprocess.Popen([path, '-S', '127.0.0.1:8080'], cwd=dir_path)
            else:
                sublime.error_message("Invalid php selection.")



"""
Open console using
ctrl + `

to run class ExampleAppCommand
window.run_command('example_app')

passing arguments to command
window.run_command('example_app', { 'agr1': 'value', .... })
"""
