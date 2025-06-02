# OpenWithSublimePlugin

## 🔥 Overview
**OpenWithSublimePlugin** is a Sublime Text 4 plugin that allows developers to **open terminals**, **execute PHP scripts**, and **serve directories** with different PHP versions, making development faster and more convenient.

## 🚀 Features
✅ **Open terminals** (Command Prompt, PowerShell, Git Bash) directly from Sublime
✅ **Run PHP files** with selected versions
✅ **Serve PHP files or directories** using different PHP versions
✅ **Quick access menu for choosing apps to open files**

## 🛠 Installation

### **Using Package Control**
Once listed on Package Control, install via:
1. Open **Command Palette** (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Search for `Package Control: Install Package`.
3. Find **OpenWithSublimePlugin** and install it.

### **Manual Installation**
If installing manually:
1. Download the package from [GitHub](https://github.com/khairnar2960/OpenWithSublimePlugin).
2. Move it to Sublime’s **Packages** directory:
   - **Windows:** `%APPDATA%\Sublime Text\Packages\OpenWithSublimePlugin`
   - **macOS:** `~/Library/Application Support/Sublime Text/Packages/OpenWithSublimePlugin`
   - **Linux:** `~/.config/sublime-text/Packages/OpenWithSublimePlugin`
3. Restart Sublime Text.

## 🎯 Usage

### **Open Terminal**
1. Right-click in Sublime Text.
2. Select **"Open With" > "Terminal"**.
3. Choose:
   - **Command Prompt**
   - **PowerShell**
   - **Git Bash**

### **Run PHP File**
1. Right-click a PHP file.
2. Navigate to **"Open With" > "PHP" > "Run File"**.
3. Select a PHP version (e.g., `8.4.0`, `8.3.14`, etc.).

### **Serve PHP File or Directory**
1. Right-click a PHP file or folder.
2. Go to **"Open With" > "PHP" > "Serve File/Directory"**.
3. Select your PHP version to launch the built-in PHP server.

### **Update Terminal Menu (After Installation)**
After installing the package, ensure menus are properly updated by running:

1. Open the **Sublime Console** using:
   - `Ctrl + \`` or go to **View > Show Console**

2. Enter the command:
   ```python

   window.run_command('update_terminal_menu')

   ```

This refreshes the terminal menu and ensures all features are available.

## 🤝 Contributing
Feel free to submit issues or pull requests to enhance the plugin!

## 📜 License
Released under the **MIT License**.

## 🌍 Links
🔗 **GitHub Repository:** [OpenWithSublimePlugin](https://github.com/khairnar2960/OpenWithSublimePlugin)
🔗 **Sublime Package Control:** *(Coming Soon)*

---
