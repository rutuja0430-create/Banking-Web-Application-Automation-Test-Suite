# 🏦 Banking Web Application Automation Test Suite

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Chrome](https://img.shields.io/badge/Chrome-Driver-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Supported-0078D6?style=for-the-badge&logo=windows&logoColor=white)

> **End-to-end automated test suite for the Guru99 Demo Banking Application — covering login, customer management, account operations, fund transfers, and balance enquiry.**

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Test Cases](#-test-cases)
- [Getting Started](#-getting-started)
- [Configuration](#️-configuration)
- [Running Tests](#-running-tests)
- [Test Reports](#-test-reports)
- [Important Notes](#-important-notes)
- [Author](#-author)

---

## 📖 About the Project

This project is a **Selenium + Python automation test suite** built for the [Guru99 Demo Banking Application](https://demo.guru99.com/V4) — a widely used practice site that simulates a real-world banking system.

### 🎯 What This Project Demonstrates

| Skill | Description |
|---|---|
| 🔐 Authentication Testing | Valid/invalid login scenarios |
| 📋 Form Automation | Multi-field form filling and submission |
| 🔔 Alert Handling | Accepting and reading browser alert popups |
| 📊 Table Data Reading | Extracting generated IDs from result tables |
| 🧩 Page Object Model | Clean, reusable, maintainable code structure |
| 📈 HTML Test Reports | Auto-generated visual test reports |
| 🔁 Data-Driven Testing | External JSON test data for flexible inputs |

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **Selenium WebDriver** | Browser automation engine |
| **Pytest** | Test framework and test runner |
| **WebDriver Manager** | Auto-installs and manages ChromeDriver |
| **pytest-html** | Generates beautiful HTML test reports |
| **Chrome Browser** | Browser under test |

---

## 📁 Project Structure

```
banking_automation/
│
├── 📂 pages/                        # Page Object Model classes
│     ├── __init__.py
│     ├── login_page.py              # Login page interactions
│     ├── new_customer_page.py       # Add new customer
│     ├── new_account_page.py        # Create bank account
│     ├── fund_transfer_page.py      # Transfer funds
│     └── balance_enquiry_page.py    # Check account balance
│
├── 📂 tests/                        # Test files
│     ├── __init__.py
│     ├── test_login.py              # TC01 – TC03
│     ├── test_new_customer.py       # TC04 – TC06
│     ├── test_new_account.py        # TC07 – TC08
│     ├── test_fund_transfer.py      # TC09 – TC10
│     └── test_balance_enquiry.py    # TC11 – TC12
│
├── 📂 test_data/
│     └── customer_data.json         # External test data (data-driven)
│
├── 📂 reports/                      # Auto-generated HTML reports
│
├── conftest.py                      # Browser setup & shared fixtures
├── config.py                        # URL, credentials configuration
├── pytest.ini                       # Pytest settings
└── requirements.txt                 # Python dependencies
```

---

## ✅ Test Cases

| TC # | Module | Scenario | Expected Result |
|------|--------|----------|-----------------|
| TC01 | 🔐 Login | Valid Manager ID and password | Redirect to Manager Home Page |
| TC02 | 🔐 Login | Invalid User ID | Error alert displayed |
| TC03 | 🔐 Login | Empty password field | Password required error |
| TC04 | 👤 New Customer | Fill all fields and submit | Customer ID generated |
| TC05 | 👤 New Customer | Submit with empty name field | Name must not be blank error |
| TC06 | 👤 New Customer | Enter letters in PIN field | Characters not allowed error |
| TC07 | 🏦 New Account | Create savings account for customer | Account number generated |
| TC08 | 🏦 New Account | Create current account for customer | Account number generated |
| TC09 | 💸 Fund Transfer | Transfer valid amount between accounts | Transaction successful message |
| TC10 | 💸 Fund Transfer | Transfer with invalid account number | Account does not exist error |
| TC11 | 💰 Balance Enquiry | Check balance with valid account | Balance amount displayed |
| TC12 | 💰 Balance Enquiry | Check balance with invalid account | Account does not exist error |

---

## 🚀 Getting Started

### Prerequisites

- ✅ Python 3.x installed
- ✅ Google Chrome browser installed
- ✅ VS Code or any code editor

### Step 1 — Clone or Download the Project

```bash
cd "your-project-location"
```

### Step 2 — Create and Activate Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 4 — Get Your Guru99 Credentials

1. Go to 👉 **https://demo.guru99.com**
2. Enter your email address
3. Check your inbox for **Manager User ID** and **Password**

> ⚠️ Credentials **reset daily** — always get fresh ones if login fails.

---

## ⚙️ Configuration

Open `config.py` and fill in your credentials:

```python
# config.py
BASE_URL   = 'https://demo.guru99.com/V4'
MANAGER_ID = 'mngr??????'   # ← Your Manager ID from email
PASSWORD   = '????????'      # ← Your Password from email
```

Update `test_data/customer_data.json` with a **unique email** before each run:

```json
{
  "valid_customer": {
    "name": "Rutuja Test",
    "dob": "1995-01-01",
    "address": "Pune Maharashtra",
    "city": "Pune",
    "state": "Maharashtra",
    "pin": "411001",
    "mobile": "9373424819",
    "email": "rutujatest01@mailinator.com",
    "password": "Test@1234"
  }
}
```

---

## ▶️ Running Tests

| Command | What it does |
|---|---|
| `pytest` | Run all tests |
| `pytest -v` | Run with detailed output |
| `pytest -v -s` | Run with detailed output + print statements |
| `pytest tests/test_login.py` | Run only login tests |
| `pytest tests/test_new_customer.py -v` | Run customer tests verbosely |

### Recommended Run Order

```
Step 1 → Run test_login.py          (verify login works)
Step 2 → Run test_new_customer.py   (copy Customer ID from output)
Step 3 → Paste Customer ID into test_new_account.py
Step 4 → Run test_new_account.py    (copy Account IDs from output)
Step 5 → Paste Account IDs into test_fund_transfer.py and test_balance_enquiry.py
Step 6 → Run pytest (all tests)
```

---

## 📊 Test Reports

After every run, an HTML report is auto-generated at:

```
reports/report.html
```

Open it in your browser to see:
- ✅ Passed tests (green)
- ❌ Failed tests (red) with error details
- ⏱️ Execution time per test
- 📋 Full test log

---

## ⚠️ Important Notes

```
🔁  Credentials reset daily     → Always get fresh ones from demo.guru99.com
📧  Use a unique email per run  → Guru99 rejects duplicate email IDs
🔗  Test order matters          → Customer ID must exist before creating account
💻  Keep venv activated         → Always run: venv\Scripts\activate before pytest
🌐  Stable internet needed      → Tests run against a live demo website
```

---

## 👩‍💻 Author

**Rutuja** — QA Automation Engineer in Training

> Built as a hands-on project to demonstrate Selenium WebDriver skills, Page Object Model design pattern, and real-world test automation practices using Python and Pytest.

---

<div align="center">

⭐ **If this project helped you, consider giving it a star!** ⭐

Made with 💙 using Python + Selenium

</div>
