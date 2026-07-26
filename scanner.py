import argparse
import json
import os
import re

# 1. Pattern Dictionary with Rule IDs and Severities
RULES = {
    "RULE-001": {
        "name": "Slack Incoming Webhook",
        "pattern": r"https://hooks\.slack\.com/services/\S+",
        "severity": "HIGH"
    },
    "RULE-002": {
        "name": "AWS Access Key ID",
        "pattern": r"AKIA[0-9A-Z]{16}",
        "severity": "CRITICAL"
    },
    "RULE-003": {
        "name": "Generic API Key",
        "pattern": r"(?i)(api[_-]?key|secret|token)\s*=\s*['\"][A-Za-z0-9_\-]{16,}['\"]",
        "severity": "HIGH"
    }
}

IGNORED_DIRS = {"venv", ".git", "__pycache__"}

def scan_file(file_path):
    """Scans an individual file line-by-line and returns structured finding objects."""
    findings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line_number, line in enumerate(file, start=1):
                for rule_id, rule_info in RULES.items():
                    match = re.search(rule_info["pattern"], line)
                    if match:
                        finding = {
                            "rule_id": rule_id,
                            "rule_name": rule_info["name"],
                            "severity": rule_info["severity"],
                            "file_path": file_path,
                            "line_number": line_number,
                            "matched_text": match.group()
                        }
                        findings.append(finding)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return findings

def scan_directory(target_dir=".", output_json="scan_results.json"):
    """Recursively walks directories, collects findings, and exports a JSON report."""
    print(f"🔍 Starting security audit in: {os.path.abspath(target_dir)}\n")
    all_findings = []
    
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
        for file in files:
            if not file.endswith(".pyc") and file != output_json:
                file_path = os.path.join(root, file)
                file_findings = scan_file(file_path)
                all_findings.extend(file_findings)

    # Print summary to terminal
    print(f"🚨 Audit Complete! Found {len(all_findings)} potential secret leak(s).\n")
    for item in all_findings:
        print(f"  [{item['severity']}] {item['rule_name']} (Rule: {item['rule_id']})")
        print(f"  └─ File: {item['file_path']} | Line: {item['line_number']}\n")

    # Export findings to JSON report
    report_data = {
        "scan_target": os.path.abspath(target_dir),
        "total_findings": len(all_findings),
        "findings": all_findings
    }
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)
        
    print(f"📁 Structured report saved to: {output_json}")
    return len(all_findings)

if __name__ == "__main__":
    # Configure Command Line Interface (CLI) arguments
    parser = argparse.ArgumentParser(
        description="🛡️ MMC Secrets & Data-Handling Security Audit Tool"
    )
    parser.add_argument(
        "--path", "-p",
        default=".",
        help="Target directory path to scan (default: current directory '.')"
    )
    parser.add_argument(
        "--output", "-o",
        default="scan_results.json",
        help="JSON report file output destination (default: 'scan_results.json')"
    )
    
    args = parser.parse_args()
    scan_directory(target_dir=args.path, output_json=args.output)