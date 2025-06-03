import zipfile
import os

package_name = "OpenWith.sublime-package"
files = ["Main.sublime-menu", "open_terminal.py", "packages.json", "README.md", "search_php_versions.py", "update_terminal_menu.py"]

with zipfile.ZipFile(package_name, "w") as package:
    for file in files:
        package.write(file)

print(f"Created {package_name}")
