"""
=============================================================================
Project 2: Stock Portfolio Tracker
Author: CodeAlpha Python Internship
Description: A menu-driven terminal application to track stock holdings,
             calculate investments, search, update, remove positions,
             and persist data to a CSV file.
=============================================================================
"""

import csv
import os

# Default CSV file path located in the same directory as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CSV_FILE = os.path.join(SCRIPT_DIR, "portfolio.csv")


def load_portfolio_from_csv(filepath: str = DEFAULT_CSV_FILE) -> dict:
    """
    Load stock portfolio data from a CSV file.
    If the file does not exist, an empty portfolio is returned.
    Handles corrupted rows gracefully with exception handling.
    """
    portfolio = {}

    if not os.path.exists(filepath):
        print(f">> Notice: Data file '{os.path.basename(filepath)}' not found. Starting with an empty portfolio.")
        return portfolio

    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row_num, row in enumerate(reader, start=2):
                try:
                    symbol = row["Symbol"].strip().upper()
                    shares = float(row["Shares"])
                    price = float(row["PurchasePrice"])

                    if not symbol or shares <= 0 or price <= 0:
                        print(f">> Warning: Skipping invalid row #{row_num} in CSV.")
                        continue

                    portfolio[symbol] = {
                        "symbol": symbol,
                        "shares": shares,
                        "price": price
                    }
                except (KeyError, ValueError) as err:
                    print(f">> Warning: Skipping corrupted data on row #{row_num}: {err}")
                    continue

        print(f">> Successfully loaded {len(portfolio)} stock(s) from '{os.path.basename(filepath)}'.")
    except Exception as exc:
        print(f">> Error reading CSV file: {exc}. Initializing with empty portfolio.")

    return portfolio


def save_portfolio_to_csv(portfolio: dict, filepath: str = DEFAULT_CSV_FILE) -> bool:
    """
    Save the current portfolio to the CSV file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Symbol", "Shares", "PurchasePrice"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for stock in portfolio.values():
                writer.writerow({
                    "Symbol": stock["symbol"],
                    "Shares": f"{stock['shares']:.2f}",
                    "PurchasePrice": f"{stock['price']:.2f}"
                })

        print(f">> Portfolio successfully saved to '{os.path.basename(filepath)}'.")
        return True
    except Exception as exc:
        print(f">> Error saving portfolio to CSV: {exc}")
        return False


def get_positive_float(prompt: str) -> float:
    """
    Prompt the user for a numeric value and enforce that it is greater than zero.
    Handles non-numeric input exceptions gracefully.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            val = float(user_input)
            if val <= 0:
                print(">> Value must be strictly greater than 0. Please try again.")
                continue
            return val
        except ValueError:
            print(">> Invalid input! Please enter a valid positive number.")


def display_portfolio(portfolio: dict) -> None:
    """
    Display all stocks in the portfolio formatted as a table,
    showing symbol, shares, purchase price, total value per stock,
    and overall portfolio total value.
    """
    if not portfolio:
        print("\n" + "-" * 55)
        print(">> Your portfolio is currently empty.")
        print("-" * 55)
        return

    print("\n" + "=" * 65)
    print("                    CURRENT STOCK PORTFOLIO                      ")
    print("=" * 65)
    # Header format
    header = f"{'Symbol':<12} | {'Shares':>10} | {'Purchase Price':>15} | {'Total Value':>15}"
    print(header)
    print("-" * 65)

    total_portfolio_value = 0.0

    # Display each stock row
    for symbol in sorted(portfolio.keys()):
        stock = portfolio[symbol]
        shares = stock["shares"]
        price = stock["price"]
        stock_total = shares * price
        total_portfolio_value += stock_total

        row = (
            f"{stock['symbol']:<12} | "
            f"{shares:>10.2f} | "
            f"${price:>14.2f} | "
            f"${stock_total:>14.2f}"
        )
        print(row)

    print("=" * 65)
    summary = f"{'TOTAL PORTFOLIO VALUE:':<43} | ${total_portfolio_value:>14.2f}"
    print(summary)
    print("=" * 65 + "\n")


def add_stock(portfolio: dict) -> None:
    """
    Add a new stock or update shares of an existing stock.
    Prompts for symbol, shares, and purchase price.
    """
    print("\n--- Add Stock ---")
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").strip().upper()

    if not symbol:
        print(">> Error: Stock symbol cannot be empty.")
        return

    if symbol in portfolio:
        print(f">> '{symbol}' already exists in your portfolio:")
        print(f"   Current Shares: {portfolio[symbol]['shares']:.2f}, Price: ${portfolio[symbol]['price']:.2f}")
        print("   Options:")
        print("   1. Add more shares to existing holding (calculates weighted average price)")
        print("   2. Overwrite completely with new position")
        print("   3. Cancel")
        choice = input("Select an option (1/2/3): ").strip()

        if choice == "1":
            new_shares = get_positive_float("Enter additional shares to add: ")
            new_price = get_positive_float("Enter purchase price for these additional shares: $")

            curr_shares = portfolio[symbol]["shares"]
            curr_price = portfolio[symbol]["price"]

            # Weighted average price calculation
            total_shares = curr_shares + new_shares
            weighted_price = ((curr_shares * curr_price) + (new_shares * new_price)) / total_shares

            portfolio[symbol]["shares"] = total_shares
            portfolio[symbol]["price"] = weighted_price
            print(f">> Updated position for {symbol}! Total Shares: {total_shares:.2f}, Weighted Avg Price: ${weighted_price:.2f}")
            save_portfolio_to_csv(portfolio)
            return

        elif choice == "2":
            shares = get_positive_float("Enter new total shares: ")
            price = get_positive_float("Enter new purchase price per share: $")
            portfolio[symbol] = {"symbol": symbol, "shares": shares, "price": price}
            print(f">> Position for {symbol} has been updated.")
            save_portfolio_to_csv(portfolio)
            return

        else:
            print(">> Add stock operation cancelled.")
            return

    # New stock entry
    shares = get_positive_float("Enter number of shares: ")
    price = get_positive_float("Enter purchase price per share: $")

    portfolio[symbol] = {
        "symbol": symbol,
        "shares": shares,
        "price": price
    }
    print(f">> Successfully added {symbol} ({shares:.2f} shares @ ${price:.2f}) to portfolio.")
    save_portfolio_to_csv(portfolio)


def update_stock(portfolio: dict) -> None:
    """
    Update the quantity and/or purchase price of an existing stock.
    """
    print("\n--- Update Stock ---")
    if not portfolio:
        print(">> Portfolio is empty. Nothing to update.")
        return

    symbol = input("Enter stock symbol to update: ").strip().upper()

    if symbol not in portfolio:
        print(f">> Error: Stock '{symbol}' was not found in your portfolio.")
        return

    current = portfolio[symbol]
    print(f">> Found {symbol}: Current Shares = {current['shares']:.2f}, Current Price = ${current['price']:.2f}")

    print("\nWhat would you like to update?")
    print("1. Quantity (Shares) only")
    print("2. Purchase Price only")
    print("3. Both Quantity and Purchase Price")
    print("4. Cancel")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        new_shares = get_positive_float("Enter new quantity of shares: ")
        portfolio[symbol]["shares"] = new_shares
        print(f">> Updated {symbol} shares to {new_shares:.2f}.")
        save_portfolio_to_csv(portfolio)

    elif choice == "2":
        new_price = get_positive_float("Enter new purchase price: $")
        portfolio[symbol]["price"] = new_price
        print(f">> Updated {symbol} purchase price to ${new_price:.2f}.")
        save_portfolio_to_csv(portfolio)

    elif choice == "3":
        new_shares = get_positive_float("Enter new quantity of shares: ")
        new_price = get_positive_float("Enter new purchase price: $")
        portfolio[symbol]["shares"] = new_shares
        portfolio[symbol]["price"] = new_price
        print(f">> Updated {symbol}: {new_shares:.2f} shares @ ${new_price:.2f}.")
        save_portfolio_to_csv(portfolio)

    else:
        print(">> Update cancelled.")


def remove_stock(portfolio: dict) -> None:
    """
    Remove a stock from the portfolio after confirmation.
    """
    print("\n--- Remove Stock ---")
    if not portfolio:
        print(">> Portfolio is empty. Nothing to remove.")
        return

    symbol = input("Enter stock symbol to remove: ").strip().upper()

    if symbol not in portfolio:
        print(f">> Error: Stock '{symbol}' was not found in your portfolio.")
        return

    confirm = input(f"Are you sure you want to delete '{symbol}' from your portfolio? (y/n): ").strip().lower()
    if confirm in ("y", "yes"):
        removed = portfolio.pop(symbol)
        print(f">> Removed {symbol} ({removed['shares']:.2f} shares) from portfolio.")
        save_portfolio_to_csv(portfolio)
    else:
        print(">> Removal cancelled.")


def search_stock(portfolio: dict) -> None:
    """
    Search for a stock by symbol (supports exact and partial match).
    """
    print("\n--- Search Stock ---")
    if not portfolio:
        print(">> Portfolio is empty. Nothing to search.")
        return

    query = input("Enter stock symbol or part of it to search: ").strip().upper()
    if not query:
        print(">> Search query cannot be empty.")
        return

    matches = [stock for sym, stock in portfolio.items() if query in sym]

    if not matches:
        print(f">> No stocks found matching '{query}'.")
        return

    print(f"\n>> Found {len(matches)} matching stock(s):")
    print("-" * 55)
    print(f"{'Symbol':<12} | {'Shares':>10} | {'Price':>12} | {'Total Value':>12}")
    print("-" * 55)
    for stock in matches:
        stock_total = stock["shares"] * stock["price"]
        print(
            f"{stock['symbol']:<12} | "
            f"{stock['shares']:>10.2f} | "
            f"${stock['price']:>11.2f} | "
            f"${stock_total:>11.2f}"
        )
    print("-" * 55)


def display_menu() -> None:
    """Display the main interactive menu options."""
    print("\n" + "=" * 45)
    print("        STOCK PORTFOLIO TRACKER        ")
    print("=" * 45)
    print("1. Display Portfolio")
    print("2. Add Stock")
    print("3. Update Stock")
    print("4. Remove Stock")
    print("5. Search Stock")
    print("6. Save Portfolio to CSV")
    print("7. Exit")
    print("=" * 45)


def main() -> None:
    """Main application loop."""
    print("Initializing Stock Portfolio Tracker...")
    portfolio = load_portfolio_from_csv()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_portfolio(portfolio)
        elif choice == "2":
            add_stock(portfolio)
        elif choice == "3":
            update_stock(portfolio)
        elif choice == "4":
            remove_stock(portfolio)
        elif choice == "5":
            search_stock(portfolio)
        elif choice == "6":
            save_portfolio_to_csv(portfolio)
        elif choice == "7":
            # Auto-save before quitting
            save_portfolio_to_csv(portfolio)
            print("\nThank you for using Stock Portfolio Tracker. Goodbye!\n")
            break
        else:
            print(">> Invalid choice! Please select a valid option (1-7).")


if __name__ == "__main__":
    main()
