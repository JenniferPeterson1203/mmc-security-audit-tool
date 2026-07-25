# 🚨 BEFORE MIGRATION: Vulnerable Code (Hardcoded Secrets)

# The secret is directly in the source code. If committed, it leaks!
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/DUMMY/TEST/TOKEN123"

def send_alert(message):
    print(f"Sending '{message}' to {SLACK_WEBHOOK_URL}")

if __name__ == "__main__":
    send_alert("System offline!")