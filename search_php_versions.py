import re
import os
import subprocess
import platform

def search_wamp64():
    php_versions = []
    php_base_path = 'C:\\wamp64\\bin\\php'

    if os.path.exists(php_base_path):
        for version_dir in os.listdir(php_base_path):
            php_exe = os.path.join(php_base_path, version_dir, 'php.exe')
            if os.path.exists(php_exe):
                try:
                    if version_dir.lower().startswith('php') and re.match(r"^\d{1,2}\.\d{1,2}\.\d{1,2}$", version_dir.replace('php', '')):
                        php_versions.append([version_dir.replace('php', ''), php_exe])
                    else:
                        version_info = subprocess.check_output([php_exe, '--version'], universal_newlines=True).split("\n")[0]
                        regex = re.search(r"\d{1,2}\.\d{1,2}\.\d{1,2}", version_info)
                        if regex:
                            php_versions.append([regex.group(), php_exe])
                except (subprocess.CalledProcessError, FileNotFoundError) as e:
                    pass

    return sorted(php_versions, key=lambda x: x[0], reverse=True)

def find_php_versions():
    php_versions = search_wamp64()

    common_paths = [
        '/usr/bin/php', '/usr/local/bin/php',
        'C:\\xampp\\php\\php.exe', 'C:\\Program Files\\PHP\\php.exe'
    ]

    # Include Linux paths dynamically if running on Linux
    if platform.system().lower() == "linux":
        common_paths.append('/opt/lampp/php/bin/php')

    for php_path in common_paths:
        if os.path.exists(php_path):
            try:
                version_info = subprocess.check_output([php_path, '-v'], universal_newlines=True).split("\n")[0]
                regex = re.search(r"\d{1,2}\.\d{1,2}\.\d{1,2}", version_info)
                if regex:
                    php_versions.append([regex.group(), php_path])
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                pass

    return sorted(php_versions, key=lambda x: x[0], reverse=True)


def build_php_menu():
    menu = {
        "caption": "PHP",
        "children": [
            {
                "caption": "Run File",
                "children": []
            },
            {
                "caption": "Serve File",
                "children": []
            },
            {
                "caption": "Serve Directory",
                "children": []
            }
        ],
        "context": [
            { "key": "selector", "operator": "equal", "operand": "source.php" }
        ]
    }

    php_versions = find_php_versions()

    if len(php_versions) > 0:
        for version, path in php_versions:
            menu['children'][0]['children'].append({"command": "run_file_with_php", "args": {"path": path}, "caption": version})
            menu['children'][1]['children'].append({"command": "serve_file_with_php", "args": {"path": path}, "caption": version})
            menu['children'][2]['children'].append({"command": "serve_dir_with_php", "args": {"path": path}, "caption": version})
        return menu
    return None
