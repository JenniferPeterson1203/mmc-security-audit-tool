import os
import re

# 1. Dictionary of Secret Detection Patterns
RULES = {
    "Slack Incoming Webhook": r"https://hooks\.slack\.com/services/\S+",
    "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "Generic API Key": r"(?i)(api[_-]?key|secret|token)\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]"
}

# Folders we want to ignore so we don't scan internal binaries or git files
IGNORED_DIRS = {"venv", ".git", "__pycache__"}

def scan_file(file_path):
    """Scans an individual file line-by-line against all rules."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line_number, line in enumerate(file, start=1):
                for rule_name, pattern in RULES.items():
                    match = re.search(pattern, line)
                    if match:
                        print(f"🚨 [{rule_name}] DETECTED in {file_path} on line {line_number}!")
                        print(f"   Matched Text: {match.group()}\n")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def scan_directory(target_dir="."):
    """Recursively walks through a folder and scans all files."""
    print(f"🔍 Starting security audit in directory: {os.path.abspath(target_dir)}\n")
    
    for root, dirs, files in os.walk(target_dir):
        # Skip ignored directories in-place
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
        for file in files:
            # Only scan code/text files, skip python cached files
            if not file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                scan_file(file_path)

if __name__ == "__main__":
    scan_directory(".")