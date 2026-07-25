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