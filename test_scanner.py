import os
import pytest
from scanner import scan_file, RULES, IGNORED_DIRS

def test_slack_webhook_detection(tmp_path):
    """Test that Slack Webhook patterns are detected correctly."""
    test_file = tmp_path / "test_slack.py"
    test_file.write_text('SLACK_URL = "https://hooks.slack.com/services/T00/B00/X00"')
    
    findings = scan_file(str(test_file))
    assert len(findings) == 1
    assert findings[0]["rule_id"] == "RULE-001"
    assert findings[0]["severity"] == "HIGH"

def test_aws_key_detection(tmp_path):
    """Test that AWS Access Key IDs are detected correctly."""
    test_file = tmp_path / "test_aws.py"
    test_file.write_text('AWS_KEY = "AKIAIOSFODNN7EXAMPLE"')
    
    findings = scan_file(str(test_file))
    assert len(findings) == 1
    assert findings[0]["rule_id"] == "RULE-002"
    assert findings[0]["severity"] == "CRITICAL"

def test_clean_file_has_no_findings(tmp_path):
    """Test that safe code produces zero findings."""
    test_file = tmp_path / "clean_code.py"
    test_file.write_text('print("Hello, Mentor Me Collective!")')
    
    findings = scan_file(str(test_file))
    assert len(findings) == 0

def test_ignored_directories_configuration():
    """Test that crucial system/environment folders are in the ignore set."""
    assert "venv" in IGNORED_DIRS
    assert ".git" in IGNORED_DIRS