# ✅ AFTER MIGRATION: Secure Code (Environment Variables)
import os
from dotenv import load_dotenv

# 1. Load variables from a local .env file into the system environment
load_dotenv()

# 2. Read the secret securely from the OS environment (no hardcoding!)
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_alert(message):
    if not SLACK_WEBHOOK_URL:
        print("❌ Error: SLACK_WEBHOOK_URL is missing from the environment!")
        return
        
    print(f"🔒 Securely sending '{message}' to {SLACK_WEBHOOK_URL}")

if __name__ == "__main__":
    send_alert("System offline!")