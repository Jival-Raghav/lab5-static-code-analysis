Below is **your own rewritten `README.md`**, in the **same structure and tone** as the one you uploaded, but fully updated to match **your specific cleaned code** and the **issues listed in your PDF** (the issues table you generated) and **your reflections**.

I used only the issues shown in your PDF and the fixes present in your cleaned code.

---

# 🐍 Python Static Analysis – Inventory Management System

This repository contains the work completed to clean, debug, and secure a Python-based Inventory Management System using multiple static analysis tools.
The goal was to identify coding errors, security flaws, style violations, and logical bugs—and fix them in a maintainable, standards-compliant way.

---

## 📂 Repository Structure

This repository includes both the original problematic script and the improved version:

* **`inventory_system.py`** – Original code containing multiple security, logic, and style issues.
* **`inventory_system_cleaned.py`** – Fully corrected version after applying fixes from static analysis.
* **`errors_static code.pdf`** – The table documenting all issues found (from Pylint, Bandit, and Flake8) with severity and line numbers.
* **`README.md`** – This document summarizing changes, issues, and reflections.

---

## 🛠️ Tools Used

Static analysis was performed using the following tools:

* **Pylint** – Found security issues, bad coding practices, unused imports, and naming problems.
* **Bandit** – Reported security vulnerabilities such as `eval`.
* **Flake8** – Reported PEP8 style issues, spacing, unused imports, and bare `except` blocks.

---

## 📊 Issue Documentation Summary

The following summarizes the issues found in the **original static code** (as shown in the PDF) and how they were fixed in the cleaned version.

| Issue                                            | Tool            | Line(s)  | Description                                                                   | Fix                                                                    |
| ------------------------------------------------ | --------------- | -------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **W0102 — Mutable default argument (`logs=[]`)** | Pylint          | 8        | Using a list as a default argument causes shared state across function calls. | Changed to `logs=None` and initialized inside function.                |
| **W0702 / E722 — Bare `except:`**                | Pylint / Flake8 | 19       | Catches all exceptions silently, hides errors.                                | Replaced with specific `KeyError` and `TypeError`, and added messages. |
| **W0123 / B307 — Use of `eval()`**               | Pylint / Bandit | 59       | Major security risk; can run arbitrary code.                                  | Removed the `eval()` call entirely.                                    |
| **Resource Leak — File not opened using `with`** | Pylint          | 26, 32   | Files opened without context manager could leak.                              | Converted all file operations to `with open(...)`.                     |
| **W0611 — Unused import (`logging`)**            | Pylint / Flake8 | 2        | `logging` imported but never used.                                            | Removed unused import.                                                 |
| **Encoding not specified**                       | Pylint          | 26, 32   | Missing UTF-8 encoding for file operations.                                   | Added `encoding="utf-8"`.                                              |
| **Global variable usage (`global stock_data`)**  | Pylint          | 27       | Considered poor practice.                                                     | Cleaned by removing global usage in cleaned code.                      |
| **Naming Convention Violations**                 | Pylint          | Many     | Functions used CamelCase (e.g., `addItem`).                                   | Renamed to snake_case (`add_item`, `remove_item`, etc.).               |
| **Missing Docstrings**                           | Pylint          | Multiple | No documentation for functions.                                               | Added docstrings to all functions.                                     |
| **String Formatting**                            | Pylint          | Multiple | Old `%` formatting used.                                                      | Converted to f-strings.                                                |
| **PEP8 Spacing Issues (E302, E305)**             | Flake8          | Multiple | Missing required blank lines.                                                 | Fixed spacing around functions and before main.                        |
| **Logic Bug — getQty() KeyError**                | Manual          | 24       | Would crash when item missing.                                                | Replaced with `.get(item, 0)`.                                         |
| **Logic Bug — Incorrect quantity validation**    | Manual          | 51–52    | Could add invalid types or negative qty.                                      | Added full validation in `add_item` and `remove_item`.                 |

All issues listed in the PDF have been addressed in the cleaned code.

---

## 🔬 Reflections

### **1. Which issues were the easiest to fix, and which were the hardest? Why?**

**Easiest fixes:**

* Removing `eval()` — a single-line, high-risk issue that required deletion.
* Removing unused imports and fixing spacing — straightforward and suggested directly by the tools.

**Hardest fixes:**

* Replacing the **bare `except:`** block.
  It required reading the logic, identifying the *specific* exceptions (`KeyError`, `TypeError`), and ensuring the behavior remained correct.
  This required code understanding, not just following a warning.

* Fixing the **mutable default argument** (`logs=[]`).
  Understanding why it's dangerous and how Python handles default arguments is essential.

### **2. Did the static analysis tools report any false positives? Describe one.**

Yes.
Pylint flagged several *naming convention* warnings (e.g., `addItem` not in snake_case).
While it is helpful, this can be considered a false positive if a project intentionally uses CamelCase or a non-PEP8 naming style.
The warning does not indicate a functional issue.

### **3. How would you integrate static analysis tools into your software development workflow?**

* **Local Pre-Commit Hooks**
  Use tools like Flake8 and Pylint to check code before committing. This prevents style and simple logic issues from entering the repository.

* **CI Pipeline (GitHub Actions, GitLab CI, Jenkins)**
  Automatically run Pylint, Bandit, and Flake8 on every push or pull request.
  High-severity issues (security or logic bugs) should block merges.

This ensures secure, reliable, and readable code across the entire team.

### **4. What improvements did you observe after applying the fixes?**

* **Security:**
  Removing `eval` and replacing the bare `except` significantly improved safety.

* **Reliability:**
  Using `.get()` instead of direct indexing prevents KeyErrors.
  Proper validation prevents invalid types and negative quantities.

* **Maintainability:**
  Code is cleaner, readable, spaced correctly, documented, and follows PEP8.

* **Robustness:**
  Removing globals, validating inputs, and using context managers reduced crash risks and improved correctness.

Overall, the cleaned script is safer, easier to understand, and more maintainable.

---

If you want, I can also **rewrite the cleaned code file header**, generate a **diagram**, or restructure your repo for submission.
