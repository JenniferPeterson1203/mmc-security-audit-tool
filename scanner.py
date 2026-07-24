import re

# Define our search pattern for Slack Webhooks
# Looks for URLs starting with https://hooks.slack.com/services/ followed by non-space characters
SLACK_PATTERN = r"https://hooks\.slack\.com/services/\S+"

def scan_file(file_path):
    print(f"Scanning {file_path} for exposed secrets...\n")
    
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            match = re.search(SLACK_PATTERN, line)
            if match:
                print(f"🚨 SECRET DETECTED on line {line_number}!")
                print(f"   Matched Pattern: {match.group()}\n")

if __name__ == "__main__":
    scan_file("sample_code.py")