# 🤖 AQA Python Project

Automation QA project covering UI and API testing with Python.
Built as a portfolio project using industry-standard tools and patterns.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-UI%20Tests-green.svg)
![Requests](https://img.shields.io/badge/Requests-API%20Tests-orange.svg)
![Allure](https://img.shields.io/badge/Allure-Reports-yellow.svg)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red.svg)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Playwright** | UI test automation |
| **Requests** | API test automation |
| **Pytest** | Test framework |
| **Allure** | Test reports |
| **Jenkins** | CI/CD pipeline |

---

## 📁 Project Structure

```
aqa_project/
├── pages/                  # Page Object classes
│   ├── base_page.py        # Base class for all pages
│   ├── text_box_page.py    # demoqa.com/text-box
│   ├── buttons_page.py     # demoqa.com/buttons
│   └── checkbox_page.py    # demoqa.com/checkbox
├── tests/
│   ├── ui/                 # UI tests (Playwright)
│   │   ├── test_text_box.py
    │   ├── test_buttons.py
│   │   └── test_checkbox.py
│   └── api/                # API tests (Requests)
│       ├── test_users.py
│       └── test_auth.py
├── utils/
│   └── api_client.py       # Requests wrapper
├── conftest.py             # Pytest fixtures
├── pytest.ini              # Pytest configuration
├── Jenkinsfile             # Jenkins CI/CD pipeline
└── requirements.txt
```

---

## 🧪 Test Coverage

### API Tests — [reqres.in](https://reqres.in)
| Test | Type | Marker |
|------|------|--------|
| Get users list | GET /api/users | smoke |
| Get single user | GET /api/users/2 | regress |
| Create user | POST /api/users | smoke |
| Delete user | DELETE /api/users/2 | regress |
| Login success | POST /api/login | smoke |
| Login missing email | POST /api/login | smoke |

### UI Tests — [demoqa.com](https://demoqa.com)
| Test | Page | Marker |
|------|------|--------|
| Fill text box form | /text-box | smoke |
| Select home checkbox | /checkbox | smoke |
| Double click | /buttons | smoke |
| Right click | /buttons | smoke |
| Click | /buttons | smoke |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Allure CLI (`brew install allure` on macOS)

### Installation

```bash
# Clone the repository
git clone https://github.com/egorpusto/aqa-python-project.git
cd aqa-python-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Running Tests

```bash
# Run all tests
pytest

# Run only smoke tests
pytest -m smoke

# Run only regress tests
pytest -m regress

# Run only API tests
pytest tests/api/

# Run only UI tests
pytest tests/ui/
```

### Allure Reports

```bash
# Generate and open report
allure serve reports
```

---

## 🏗️ Design Patterns

- **Page Object** — each page is a separate class with locators and methods
- **Fixtures** — shared setup via pytest fixtures in `conftest.py`
- **ApiClient** — wrapper over Requests with base URL and API key
- **Arrange-Act-Assert** — clear test structure

---

## ⚙️ CI/CD

Jenkins pipeline runs automatically on every push:

```
Install dependencies → Smoke tests → Regress tests → Allure report
```

---

## 👤 Author

**Egor Pusto**
- GitHub: [@egorpusto](https://github.com/egorpusto)