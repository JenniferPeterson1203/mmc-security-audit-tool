import json
import os

# Map scanner Rule IDs to clean Environment Variable Key names
RULE_TO_ENV_VAR = {
    "RULE-001": "SLACK_WEBHOOK_URL",
    "RULE-002": "AWS_ACCESS_KEY_ID",
    "RULE-003": "GENERIC_API_KEY"
}

def generate_env_template(scan_results_file="scan_results.json", output_template=".env.template"):
    """Reads scan_results.json and creates a blank .env.template file with placeholder values."""
    if not os.path.exists(scan_results_file):
        print(f"❌ Error: {scan_results_file} not found. Run scanner.py first!")
        return

    try:
        with open(scan_results_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        findings = data.get("findings", [])
        if not findings:
            print("✨ No secrets detected! No .env.template needed.")
            return

        # Collect unique environment variable keys needed based on detected rules
        required_env_vars = set()
        for item in findings:
            rule_id = item.get("rule_id")
            if rule_id in RULE_TO_ENV_VAR:
                required_env_vars.add(RULE_TO_ENV_VAR[rule_id])
            else:
                # Default fallback key name
                required_env_vars.add(f"MISSING_SECRET_{rule_id}")

        # Write .env.template with clean placeholders
        with open(output_template, "w", encoding="utf-8") as f:
            f.write("# .env.template - Environment Variable Template\n")
            f.write("# DO NOT store actual secret values in this file.\n")
            f.write("# Copy this file to .env and fill in your private local keys.\n\n")
            
            for env_var in sorted(required_env_vars):
                f.write(f"{env_var}=your_{env_var.lower()}_here\n")

        print(f"✅ Success! Auto-generated template with {len(required_env_vars)} required key(s) at: {output_template}")

    except Exception as e:
        print(f"Error generating template: {e}")

if __name__ == "__main__":
    generate_env_template()