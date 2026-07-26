# 🧠 Project Knowledge Checks & Key Concepts

This document tracks technical concepts, questions, and answers learned throughout the development of the Secrets & Data-Handling Security Audit Tool.

---

### 1. Version Control & Environment Hygiene
* **Question:** Why do we put `venv/` and `.env` inside our `.gitignore` file instead of committing them to GitHub?
* **Answer:** `.env` contains sensitive credentials like private keys and API tokens that must never be exposed publicly. `venv/` contains bulky local environment dependencies that belong on the local machine rather than in source control.

---

### 2. Conventional Commit Standards
* **Question:** If we add a new regex rule to `scanner.py` to detect Slack tokens, which conventional commit prefix should we use?
* **Answer:** `feat:` because adding a new regex detection rule introduces a new feature/capability to the auditing tool.

---

### 3. File Iteration & Line Tracking in Python
* **Question:** In `scanner.py`, what does `enumerate(file, start=1)` do when looping through a file?
* **Answer:** It tracks human-readable line numbers (starting at 1) alongside the text of each line, allowing the scanner to report the exact line number where a secret is detected.

---

### 4. Branching Strategy & Push Protection
* **Question:** Why do we build new code on a branch like `feature/regex-scanner` and test it first before merging it into `main`?
* **Answer:** Branching isolates new features and bug fixes from stable production code. It allows developers to test, fix issues (like secret detection/push protection blocks), and review code safely before combining it with the main codebase.

---

### 5. Recursive Directory Walking & Performance Hygiene
* **Question:** In Python's `os.walk()`, why do we filter out directories like `venv` and `.git` using `IGNORED_DIRS`?
* **Answer:** Filtering out `venv/` and `.git/` prevents the scanner from wasting execution time and memory scanning thousands of internal binary, dependency, or version history files. It ensures the tool focuses only on project source code and runs efficiently.

---

### 6. Structured Reporting & Data Export (JSON)
* **Question:** Why do security tools export scan results to a structured format like JSON instead of just printing plain text strings to the terminal screen?
* **Answer:** Structured JSON formats allow security audit findings to be permanently logged, easily shared, and automatically parsed by other automated systems, security dashboards, or CI/CD pipelines without relying on manual terminal inspection.

---

### 7. Automated Unit Testing (`pytest`)
* **Question:** What is the purpose of writing unit tests for a security scanning tool, and how does `pytest` help developers build reliable code?
* **Answer:** Unit tests verify that detection rules, file handling, and exclusion logic work as expected in isolation. They prevent regressions, minimize false alarms, and ensure new code changes do not break existing security controls.

---

### 8. Environment Variable Hygiene
* **Question:** Why do development teams commit a `.env.template` file to GitHub source control, but NEVER commit a `.env` file?
* **Answer:** The `.env` file holds real, active configuration values and secrets for a specific environment; committing it introduces severe security risks. A `.env.template` file contains the exact same keys but leaves the sensitive values empty or uses safe placeholders, allowing developers to see required configurations without exposing real credentials.

---

### 9. Secure Secret Migration & Runtime Resolution (`os.getenv`)
* **Question:** In secure application design, why is reading secrets at runtime via `os.getenv()` or `python-dotenv` considered vastly superior to declaring credential strings directly in Python source code?
* **Answer:** Decoupling secrets from source code prevents credentials from ever being tracked in Git history or exposed in public repositories. It enables identical code to run across different environments (development, staging, production) simply by swapping environment configurations without modifying code files.

---

### 10. Command-Line Interface (CLI) Customization (`argparse`)
* **Question:** Why is `argparse` built into developer tools, and what benefit does providing command-line options (like `--path` or `--output`) give to security teams operating in automated CI/CD pipelines?
* **Answer:** `argparse` allows a script to accept dynamic inputs directly from the terminal without modifying source code. In automated CI/CD pipelines, this enables security teams to dynamically pass arguments (e.g., directing `--path` to specific subfolders or storing `--output` in build artifacts) for scalable, automated security checks.