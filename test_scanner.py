import json
import os
import pytest
from scanner import scan_file, scan_directory, RULES, IGNORED_DIRS
from remediation import generate_env_template

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

def test_custom_output_json_generation(tmp_path):
    """Test that scanning exports results to a custom JSON file path."""
    test_file = tmp_path / "leaky_code.py"
    test_file.write_text('SLACK_URL = "https://hooks.slack.com/services/T00/B00/X00"')
    
    custom_json = str(tmp_path / "custom_test_report.json")
    scan_directory(target_dir=str(tmp_path), output_json=custom_json)
    
    assert os.path.exists(custom_json)
    with open(custom_json, "r") as f:
        data = json.load(f)
        assert data["total_findings"] == 1

def test_env_template_remediation_generation(tmp_path):
    """Test that generate_env_template converts scan findings into a valid .env.template."""
    # Create mock scan results
    mock_scan = tmp_path / "mock_results.json"
    mock_scan.write_text(json.dumps({
        "findings": [
            {"rule_id": "RULE-001"},
            {"rule_id": "RULE-002"}
        ]
    }))
    
    template_out = str(tmp_path / ".env.template.test")
    generate_env_template(scan_results_file=str(mock_scan), output_template=template_out)
    
    assert os.path.exists(template_out)
    with open(template_out, "r") as f:
        content = f.read()
        assert "SLACK_WEBHOOK_URL=" in content
        assert "AWS_ACCESS_KEY_ID=" in content