# 🛡️ MMC Secrets & Data-Handling Security Audit Tool

> **Automated SAST utility for credential leak detection, folder hygiene, and privacy-rule compliance.**

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Security Focus](https://img.shields.io/badge/DevSecOps-SAST%20Audit-red.svg)

---

## 📌 Executive Summary

The **MMC Secrets & Data-Handling Security Audit Tool** is a lightweight, high-performance Static Application Security Testing (SAST) utility built in Python. Designed to enforce **Mentor Me Collective’s Non-Negotiable Product Rules** and the **VOL-001 Security Standard**, this tool proactively scans codebases and configuration trees to catch hardcoded secrets, private API tokens, and webhook URLs before they reach source control.

### Key Engineering Highlights
* **Deterministic Detection Engine:** Uses optimized Regular Expressions (`re`) to identify pattern-based credential leaks (Slack Incoming Webhooks, AWS Access Keys, generic API tokens).
* **Recursive Directory Traversal:** Utilizes `os.walk()` with built-in exclusion filters to efficiently audit full project trees while bypassing bulky dependencies (`venv/`, `.git/`, `__pycache__/`).
* **Structured JSON Reporting:** Exports actionable audit logs complete with line numbers, file paths, rule IDs, and standardized severity levels (`CRITICAL`, `HIGH`, `MEDIUM`).
* **Automated Unit Test Suite:** Full test coverage powered by `pytest` to guarantee detection reliability and zero false negatives on clean codebases.

---

## 🏗️ System Architecture & Workflow

```text
       ┌────────────────────────────────────────────────────────┐
       │             Target Repository / Directory              │
       └───────────────────────────┬────────────────────────────┘
                                   │
                                   ▼
                   ┌────────────────────────────────┐
                   │    Directory Walker (os.walk)  │
                   │  - Skips venv/, .git/, .pyc    │
                   └───────────────┬────────────────┘
                                   │
                                   ▼
                   ┌────────────────────────────────┐
                   │   Regex Detection Engine (re)  │
                   │  - RULE-001: Slack Webhooks    │
                   │  - RULE-002: AWS Keys          │
                   │  - RULE-003: Generic API Keys │
                   └───────────────┬────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
       ┌────────────────────────┐    ┌────────────────────────┐
       │ Terminal Summary Alert │    │  scan_results.json     │
       └────────────────────────┘    └────────────────────────┘
```
## 🛠️ Installation & Setup

### Prerequisites
* **Python 3.11+** installed
* **Git** installed

### 1. Clone the Repository
```bash
git clone [https://github.com/JenniferPeterson1203/mmc-security-audit-tool.git](https://github.com/JenniferPeterson1203/mmc-security-audit-tool.git)
cd mmc-security-audit-tool
```
### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (Mac)
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install pytest
```
## 🚀 Usage Guide
Running the Scanner
```bash
To scan the current repository directory and generate a structured JSON audit report:
```
```bash
python3 scanner.py
```
### Running Automated Unit Tests
To verify all regex patterns, folder exclusion rules, and edge-case handlers:
```bash
pytest
```

## 📊 Sample Output & Audit Report
Terminal Output
🔍 Starting security audit in: /Users/username/mmc-security-audit-tool

```bash 🚨 Audit Complete! Found 4 potential secret leak(s).

  [HIGH] Slack Incoming Webhook (Rule: RULE-001)
  └─ File: ./sample_code.py | Line: 4

  [CRITICAL] AWS Access Key ID (Rule: RULE-002)
  └─ File: ./sample_code.py | Line: 10
```

### 📁 Structured report saved to: scan_results.json
Exported scan_results.json Format
```bash
JSON
{
    "scan_target": "/path/to/project",
    "total_findings": 4,
    "findings": [
        {
            "rule_id": "RULE-002",
            "rule_name": "AWS Access Key ID",
            "severity": "CRITICAL",
            "file_path": "./sample_code.py",
            "line_number": 10,
            "matched_text": "AKIAIOSFODNN7EXAMPLE"
        }
    ]
}
```
### 🛡️ Security & Compliance Alignment
MMC Product Rules: Guarantees zero hardcoded webhook URLs or credentials in source control.

DevSecOps Best Practices: Built to integrate cleanly into CI/CD pipelines (GitHub Actions) as a pre-commit or build-stage security check.

Environment Hygiene: Strictly isolates machine dependencies (venv/) and local environmental secrets (.env) via .gitignore.

### 🎓 Residency & Author Information
Author: Jennifer Peterson

Program: Mentor Me Collective (MMC) Platform Engineering Residency

Track: Secrets & Data-Handling Security Audit Tool

Majors & Specialization: Programming & Software Development | Cybersecurity