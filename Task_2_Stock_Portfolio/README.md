# Task 2: Stock Portfolio Tracker

A robust, menu-driven terminal application to track personal stock investments, calculate holdings, search positions, and persist portfolio data to CSV. Developed for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Description

The **Stock Portfolio Tracker** empowers users to manage their stock portfolio without reliance on paid or external stock APIs. Users can add positions (specifying stock symbol, quantity of shares, and purchase price), update existing positions, remove stocks, search holdings, and display a comprehensive tabular portfolio statement calculating individual and total portfolio value. All data is automatically loaded from and saved to a persistent CSV file.

---

## 🚀 Features

1. **Add Stock**:
   - Accepts stock ticker symbol (e.g., `AAPL`, `MSFT`, `GOOGL`).
   - Accepts number of shares and purchase price per share.
   - Intelligent conflict detection: If the stock already exists, offers weighted-average accumulation or position overwrite.
2. **Update Stock**:
   - Select an existing stock symbol to modify.
   - Choose to update quantity of shares, purchase price, or both.
3. **Remove Stock**:
   - Remove any stock from the portfolio with confirmation safety prompts.
4. **Display Portfolio**:
   - Formats holdings into a clean, aligned console table.
   - Computes individual position values: $\text{Total Value} = \text{Shares} \times \text{Purchase Price}$.
   - Computes cumulative total portfolio investment value.
   - Gracefully handles empty portfolios.
5. **Search Stock**:
   - Case-insensitive search by symbol or partial match.
   - Displays all matching records and their calculated totals.
6. **Data Persistence (CSV)**:
   - Stores all records in `portfolio.csv` using Python's standard `csv.DictWriter` and `csv.DictReader`.
   - Auto-loads existing portfolio data on program start.
   - Auto-saves changes upon addition, modification, removal, and exit.
7. **Input Validation & Exception Handling**:
   - Enforces positive numerical values ($> 0$) for shares and prices.
   - Handles non-numeric inputs using `try...except ValueError`.
   - Handles missing or corrupted CSV files gracefully.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3.10+
- **Standard Library Modules**: `csv`, `os`, `sys`
- **External Dependencies**: None (100% core Python standard library)

---

## 🧠 Python Concepts Demonstrated

1. **File I/O & CSV Module (`csv.DictReader`, `csv.DictWriter`)**: Reading and writing structured tabular data with headers.
2. **Data Structures**:
   - `dict`: Key-value storage indexed by stock symbol for fast $O(1)$ lookups and updates.
   - `list`: Filtering and sorting for table rendering and search results.
3. **Control Flow**:
   - `while` loops for interactive menu navigation and input validation retries.
   - `if-elif-else` branches for menu selection and update options.
4. **Exception Handling**:
   - `try-except ValueError` to intercept invalid numerical inputs.
   - `try-except FileNotFoundError / Exception` for file operations.
5. **String Formatting**:
   - Aligned f-strings with precision formatting (e.g., `{price:>14.2f}`, `{shares:>10.2f}`).

---

## 📂 Project Structure

```text
Task_2_Stock_Portfolio/
│
├── portfolio.py        # Main menu-driven portfolio script
├── portfolio.csv       # Persistent CSV storage file
└── README.md           # Project documentation and manual
```

---

## ⚙️ Installation & Prerequisites

1. Ensure **Python 3.10 or newer** is installed.
   Verify with:
   ```bash
   python --version
   ```
2. No third-party packages or API keys are required.

---

## 🎮 How to Run the Project

1. Open your terminal or VS Code terminal.
2. Navigate to the project directory:
   ```bash
   cd Task_2_Stock_Portfolio
   ```
3. Run the application:
   ```bash
   python portfolio.py
   ```

---

## 🖥️ Sample Output

### Main Menu
```text
Initializing Stock Portfolio Tracker...
>> Successfully loaded 5 stock(s) from 'portfolio.csv'.

=============================================
        STOCK PORTFOLIO TRACKER        
=============================================
1. Display Portfolio
2. Add Stock
3. Update Stock
4. Remove Stock
5. Search Stock
6. Save Portfolio to CSV
7. Exit
=============================================
Enter your choice (1-7): 1
```

### Portfolio Table View
```text
=================================================================
                    CURRENT STOCK PORTFOLIO                      
=================================================================
Symbol       |     Shares |  Purchase Price |     Total Value
-----------------------------------------------------------------
AAPL         |      15.00 |         $182.50 |       $2,737.50
GOOGL        |       8.00 |         $165.25 |       $1,322.00
MSFT         |      10.00 |         $415.00 |       $4,150.00
NVDA         |      25.00 |         $120.00 |       $3,000.00
TSLA         |      12.00 |         $245.80 |       $2,949.60
=================================================================
TOTAL PORTFOLIO VALUE:                      |      $14,159.10
=================================================================
```

### Adding a Stock
```text
--- Add Stock ---
Enter stock symbol (e.g., AAPL, TSLA): AMZN
Enter number of shares: 20
Enter purchase price per share: $185.50
>> Successfully added AMZN (20.00 shares @ $185.50) to portfolio.
>> Portfolio successfully saved to 'portfolio.csv'.
```

---

## 🏆 Internship Evaluation Checklist

- [x] Menu-driven interface with 7 options
- [x] Add stock with symbol, shares, and purchase price
- [x] Conflict resolution (weighted average or overwrite) for existing symbols
- [x] Update stock quantity and/or purchase price
- [x] Remove stock with user confirmation
- [x] Tabular display with individual and total portfolio value
- [x] Search stock by symbol with partial match support
- [x] CSV saving and loading using `csv` module
- [x] Handle missing CSV without crashes
- [x] Input validation for negative and non-numeric inputs
