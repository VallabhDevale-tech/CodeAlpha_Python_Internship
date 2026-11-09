"""
=============================================================================
Project 3: Task Automation with Python Scripts
Author: CodeAlpha Python Internship
Description: A menu-driven automation utility featuring:
             1. Automatic File Organizer (sorts files by extension category)
             2. Email Extractor (extracts and deduplicates emails from text)
             3. Webpage Title Scraper (fetches & saves webpage titles)
=============================================================================
"""

import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# External dependencies for Web Scraping
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print(">> Warning: 'requests' or 'beautifulsoup4' is not installed.")
    print(">> Please install dependencies using: pip install -r requirements.txt\n")

# Default output directory relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "output"

# File extension categorization mapping for Feature 1
EXTENSION_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".odt", ".rtf"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".m4v"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"},
}


# =============================================================================
# FEATURE 1: AUTOMATIC FILE ORGANIZER
# =============================================================================

def get_category_for_extension(ext: str) -> str:
    """Return the category name for a given file extension."""
    ext_lower = ext.lower()
    for category, extensions in EXTENSION_CATEGORIES.items():
        if ext_lower in extensions:
            return category
    return "Other"


def get_collision_safe_path(target_dir: Path, original_filename: str) -> Path:
    """
    Generate a non-colliding target file path.
    If 'target_dir / original_filename' already exists, appends '_1', '_2', etc.
    before the extension so existing files are never overwritten.
    """
    destination = target_dir / original_filename
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    counter = 1
    while True:
        candidate = target_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def run_file_organizer() -> None:
    """
    Feature 1: Prompt user for source and destination folders,
    categorize files, move them safely without overwriting,
    and display a summary report.
    """
    print("\n" + "=" * 50)
    print("       FEATURE 1: AUTOMATIC FILE ORGANIZER       ")
    print("=" * 50)

    source_input = input("Enter the source folder path: ").strip().strip('"').strip("'")
    if not source_input:
        print(">> Error: Source folder path cannot be empty.")
        return

    source_path = Path(source_input).resolve()
    if not source_path.exists() or not source_path.is_dir():
        print(f">> Error: The folder '{source_path}' does not exist or is not a directory.")
        return

    dest_input = input("Enter the destination folder path (press Enter to organize inside source folder): ").strip().strip('"').strip("'")
    if dest_input:
        dest_path = Path(dest_input).resolve()
    else:
        dest_path = source_path

    try:
        dest_path.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        print(f">> Error creating destination directory '{dest_path}': {exc}")
        return

    # Scan for top-level regular files only (ignore subdirectories)
    items_to_move = [item for item in source_path.iterdir() if item.is_file()]

    if not items_to_move:
        print(f">> Notice: No regular files found to organize in '{source_path}'.")
        return

    print(f"\n>> Found {len(items_to_move)} file(s) to organize. Processing...")

    stats: dict[str, int] = {"Images": 0, "Documents": 0, "Videos": 0, "Audio": 0, "Other": 0}
    moved_count = 0

    for file_path in items_to_move:
        category = get_category_for_extension(file_path.suffix)
        category_dir = dest_path / category

        try:
            category_dir.mkdir(parents=True, exist_ok=True)
            safe_dest_file = get_collision_safe_path(category_dir, file_path.name)
            
            # Move file safely
            shutil.move(str(file_path), str(safe_dest_file))
            stats[category] += 1
            moved_count += 1
        except Exception as exc:
            print(f">> Error moving '{file_path.name}': {exc}")

    # Display final summary table
    print("\n" + "=" * 45)
    print("       ORGANIZATION SUMMARY REPORT       ")
    print("=" * 45)
    for cat, count in stats.items():
        print(f"{cat:<15}: {count} file(s) moved")
    print("-" * 45)
    print(f"Total Files Moved: {moved_count}")
    print(f"Destination Path : {dest_path}")
    print("=" * 45 + "\n")


# =============================================================================
# FEATURE 2: EMAIL EXTRACTOR
# =============================================================================

# RFC 5322 compatible regex pattern for valid email matching
EMAIL_REGEX_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


def extract_emails_from_text(raw_text: str) -> list[str]:
    """
    Search raw text for all email addresses and return a deduplicated
    list preserving the order of appearance.
    """
    matches = re.findall(EMAIL_REGEX_PATTERN, raw_text)
    
    seen = set()
    unique_emails = []
    for email in matches:
        # Strip trailing dot if matched punctuation at sentence end
        cleaned = email.rstrip(".")
        normalized = cleaned.lower()
        if normalized not in seen and "." in cleaned.split("@")[-1]:
            seen.add(normalized)
            unique_emails.append(cleaned)

    return unique_emails


def run_email_extractor() -> None:
    """
    Feature 2: Accept a text file, extract all email addresses with regex,
    deduplicate them, display them, and save them to a file.
    """
    print("\n" + "=" * 50)
    print("          FEATURE 2: EMAIL EXTRACTOR             ")
    print("=" * 50)

    input_file_str = input("Enter path to text file (.txt): ").strip().strip('"').strip("'")
    if not input_file_str:
        print(">> Error: File path cannot be empty.")
        return

    input_path = Path(input_file_str).resolve()
    if not input_path.exists() or not input_path.is_file():
        print(f">> Error: File '{input_path}' does not exist or is not a valid file.")
        return

    # Read file content safely with fallback encodings
    content = ""
    try:
        with open(input_path, mode="r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(input_path, mode="r", encoding="latin-1") as f:
                content = f.read()
        except Exception as exc:
            print(f">> Error reading file: {exc}")
            return
    except Exception as exc:
        print(f">> Error opening file: {exc}")
        return

    emails = extract_emails_from_text(content)

    print(f"\n>> Extraction complete! Found {len(emails)} unique email address(es).")

    if not emails:
        print(">> No valid email addresses found in the specified file.")
        return

    print("\n--- Extracted Emails ---")
    for idx, email in enumerate(emails, start=1):
        print(f" {idx}. {email}")
    print("-" * 30)

    # Prompt user for output location or default to output/extracted_emails.txt
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    default_save_path = DEFAULT_OUTPUT_DIR / "extracted_emails.txt"

    out_prompt = f"Enter output file path (press Enter for default: '{default_save_path}'): "
    out_input = input(out_prompt).strip().strip('"').strip("'")

    save_path = Path(out_input).resolve() if out_input else default_save_path

    try:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, mode="w", encoding="utf-8") as out_file:
            for email in emails:
                out_file.write(email + "\n")
        print(f">> Successfully saved {len(emails)} email(s) to '{save_path}'.\n")
    except Exception as exc:
        print(f">> Error writing output file: {exc}\n")


# =============================================================================
# FEATURE 3: WEBPAGE TITLE SCRAPER
# =============================================================================

def run_webpage_title_scraper() -> None:
    """
    Feature 3: Ask user for a URL, fetch the webpage using requests,
    parse the title using BeautifulSoup, display the title, and save it
    to an output text file. Handles invalid URLs and network errors gracefully.
    """
    print("\n" + "=" * 50)
    print("       FEATURE 3: WEBPAGE TITLE SCRAPER          ")
    print("=" * 50)

    url_input = input("Enter webpage URL (e.g., https://www.python.org): ").strip()
    if not url_input:
        print(">> Error: URL cannot be empty.")
        return

    # Automatically prepend 'https://' if protocol is missing
    target_url = url_input
    if not target_url.startswith(("http://", "https://")):
        target_url = "https://" + target_url

    print(f">> Fetching webpage: {target_url} ...")

    # Standard browser user-agent header to avoid bot rejections
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.MissingSchema:
        print(f">> Error: Invalid URL schema in '{target_url}'.")
        return
    except requests.exceptions.ConnectionError:
        print(f">> Error: Unable to connect to '{target_url}'. Check your internet connection or URL.")
        return
    except requests.exceptions.Timeout:
        print(f">> Error: Request timed out while connecting to '{target_url}'.")
        return
    except requests.exceptions.HTTPError as http_err:
        print(f">> HTTP Error encountered: {http_err}")
        return
    except Exception as exc:
        print(f">> Unexpected error fetching webpage: {exc}")
        return

    # Parse HTML using BeautifulSoup
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.title and soup.title.string:
            title_text = soup.title.string.strip()
        else:
            title_text = "(No <title> tag found on webpage)"
    except Exception as exc:
        print(f">> Error parsing HTML: {exc}")
        return

    print("\n" + "-" * 45)
    print(f"URL   : {target_url}")
    print(f"Title : {title_text}")
    print("-" * 45)

    # Save title to output file
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    default_save_path = DEFAULT_OUTPUT_DIR / "scraped_titles.txt"

    out_prompt = f"Enter output file path (press Enter for default: '{default_save_path}'): "
    out_input = input(out_prompt).strip().strip('"').strip("'")
    save_path = Path(out_input).resolve() if out_input else default_save_path

    try:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(save_path, mode="a", encoding="utf-8") as out_file:
            out_file.write(f"[{timestamp}]\n")
            out_file.write(f"URL   : {target_url}\n")
            out_file.write(f"Title : {title_text}\n")
            out_file.write("-" * 50 + "\n")

        print(f">> Successfully appended title to '{save_path}'.\n")
    except Exception as exc:
        print(f">> Error saving scraped title: {exc}\n")


# =============================================================================
# MAIN MENU DRIVER
# =============================================================================

def display_menu() -> None:
    """Display the main automation application menu."""
    print("\n" + "=" * 45)
    print("         TASK AUTOMATION UTILITY         ")
    print("=" * 45)
    print("1. Automatic File Organizer")
    print("2. Email Extractor")
    print("3. Webpage Title Scraper")
    print("4. Exit")
    print("=" * 45)


def main() -> None:
    """Main execution loop for Task Automation."""
    print("Welcome to the Task Automation Suite!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            run_file_organizer()
        elif choice == "2":
            run_email_extractor()
        elif choice == "3":
            run_webpage_title_scraper()
        elif choice == "4":
            print("\nThank you for using Task Automation Utility. Goodbye!\n")
            break
        else:
            print(">> Invalid choice! Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()
