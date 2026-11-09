# CodeAlpha Python Programming Internship Projects

Welcome to the official repository for the **CodeAlpha Python Programming Internship**. This repository contains three independent, production-ready, beginner-friendly Python applications designed to showcase foundational and practical programming skills.

---

## 📌 Repository Overview

This repository is structured into three self-contained tasks:

| Task # | Project Name | Focus Areas | Key Modules / Tools |
| :---: | :--- | :--- | :--- |
| **01** | [**Hangman Game**](./Task_1_Hangman) | Interactive CLI Game, Logic & Flow Control | `random`, ASCII art, loops, sets |
| **02** | [**Stock Portfolio Tracker**](./Task_2_Stock_Portfolio) | Menu-driven CRUD App, Financial Calculations, CSV Persistence | `csv`, exception handling, dictionaries |
| **03** | [**Task Automation with Python Scripts**](./Task_3_Task_Automation) | Desktop & Web Automation, File Organization, Web Scraping | `pathlib`, `shutil`, `re`, `requests`, `bs4` |

---

## 📂 Project Directory Structure

```text
CodeAlpha_Python_Internship/
│
├── Task_1_Hangman/
│   ├── hangman.py              # Hangman game script
│   └── README.md               # Task 1 detailed documentation
│
├── Task_2_Stock_Portfolio/
│   ├── portfolio.py            # Menu-driven stock portfolio tracker
│   ├── portfolio.csv           # Persistent CSV storage file
│   └── README.md               # Task 2 detailed documentation
│
├── Task_3_Task_Automation/
│   ├── automation.py           # Multi-feature automation utility
│   ├── requirements.txt        # Third-party dependencies (requests, bs4)
│   ├── README.md               # Task 3 detailed documentation
│   └── output/                 # Destination folder for extracted & scraped data
│       └── .gitkeep
│
├── .gitignore                  # Git exclusion rules
└── README.md                   # Repository overview (this file)
```

---

## 📋 Task Summaries

### Task 1: Hangman Game
A terminal-based word-guessing game featuring:
- Random word selection from a curated word bank.
- 7-stage ASCII gallows visualizer.
- Strict 6-incorrect-guess limit.
- Duplicate guess detection without penalty.
- Clean win/loss messages with secret word disclosure.
- Seamless replay loop.

### Task 2: Stock Portfolio Tracker
A menu-driven financial portfolio manager featuring:
- Add new positions with symbol, shares, and purchase price.
- Conflict detection: calculates weighted-average prices or permits overwrite.
- Update share count, purchase price, or both.
- Remove positions with safety confirmation.
- Formatted tabular portfolio view with total investment calculations.
- Search holdings by symbol (supports partial matches).
- Data persistence via CSV (`csv.DictReader` and `csv.DictWriter`).
- Defensive input handling for non-numeric and negative values.

### Task 3: Task Automation with Python Scripts
A multi-purpose automation CLI featuring three workflows:
1. **Automatic File Organizer**: Categorizes unorganized files into `Images`, `Documents`, `Videos`, `Audio`, and `Other` folders, equipped with collision-prevention suffixes (`_1`, `_2`) so files are never overwritten.
2. **Email Extractor**: Scans `.txt` files, extracts email patterns with regex, removes duplicates, and saves clean results to disk.
3. **Webpage Title Scraper**: Fetches any URL via `requests`, extracts HTML `<title>` tags with `BeautifulSoup`, and logs them with timestamps to an output file, with fault-tolerant connection handling.

---

## ⚙️ Prerequisites & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/CodeAlpha_Python_Internship.git
cd CodeAlpha_Python_Internship
```

### 2. Verify Python Version
Make sure you have **Python 3.10+** installed:
```bash
python --version
```

### 3. Install Required Dependencies
Tasks 1 and 2 rely solely on Python's built-in standard library. Task 3 requires `requests` and `beautifulsoup4`:
```bash
pip install -r Task_3_Task_Automation/requirements.txt
```

---

## 🚀 How to Run Each Project

You can execute each task directly from your VS Code terminal or command line:

### Run Task 1: Hangman
```bash
cd Task_1_Hangman
python hangman.py
```

### Run Task 2: Stock Portfolio Tracker
```bash
cd Task_2_Stock_Portfolio
python portfolio.py
```

### Run Task 3: Task Automation
```bash
cd Task_3_Task_Automation
python automation.py
```

---

## 🧪 Testing and Verification

Each application has undergone testing across:
- **Valid input workflows**: Standard happy paths and successful completions.
- **Edge cases**: Empty inputs, whitespace strings, non-existent files, and duplicate entries.
- **Error handling**: Negative numeric inputs, letters where numbers are expected, and network connection drops.
- **Data integrity**: Non-destructive file moves and CSV serialization / deserialization.

For detailed test steps and output examples, consult the dedicated `README.md` inside each task folder.

---

## 📜 Internship Declaration

These projects were created as deliverables for the **CodeAlpha Python Programming Internship**, demonstrating clean code structure, adherence to Python best practices, and effective problem-solving using core Python capabilities.
