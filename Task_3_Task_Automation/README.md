# Task 3: Task Automation with Python Scripts

A multi-functional, menu-driven desktop automation suite developed in Python for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Description

This project provides an automation toolkit combining three practical real-world workflows into a single menu-driven console application:
1. **Automatic File Organizer**: Scans unorganized directories and moves files into organized category folders (`Images`, `Documents`, `Videos`, `Audio`, `Other`) based on file extensions, with built-in collision detection to prevent overwriting existing files.
2. **Email Extractor**: Scans text files, extracts email addresses using regular expressions, deduplicates them, and writes the clean list to an output file.
3. **Webpage Title Scraper**: Connects to target websites using HTTP requests, extracts their HTML `<title>` tags using `BeautifulSoup`, and logs them with timestamps to an output file.

---

## 🚀 Features

### Feature 1: Automatic File Organizer
- **Intelligent Extension Mapping**:
  - `Images`: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.tiff`, `.ico`
  - `Documents`: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.xls`, `.pptx`, `.ppt`, `.csv`, `.odt`, `.rtf`
  - `Videos`: `.mp4`, `.mkv`, `.mov`, `.avi`, `.wmv`, `.flv`, `.webm`, `.m4v`
  - `Audio`: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`, `.wma`
  - `Other`: All other files (e.g., `.zip`, `.rar`, `.exe`, `.py`, extensionless files)
- **Automatic Directory Creation**: Creates target category folders on demand.
- **Accidental Overwrite Prevention**: If a destination file already exists, appends numerical suffixes (e.g., `filename_1.ext`, `filename_2.ext`) to ensure zero data loss.
- **Subdirectory Preservation**: Skips subdirectories so existing folder hierarchies are not disrupted.
- **Summary Report**: Prints a clean breakdown table showing the number of files moved per category.

### Feature 2: Email Extractor
- **Regex Extraction**: Employs an RFC-compatible regular expression to identify valid email patterns.
- **Case-Insensitive Deduplication**: Removes duplicate emails while preserving formatting.
- **Punctuation Stripping**: Safely handles emails placed at the ends of sentences (e.g. `user@example.com.`).
- **File Persistence**: Saves deduplicated emails to `output/extracted_emails.txt` or a user-specified path.

### Feature 3: Webpage Title Scraper
- **HTTP Fetching**: Fetches web content via `requests` with standard browser headers and timeout handling.
- **Protocol Normalization**: Automatically prepends `https://` if omitted by the user.
- **HTML Parsing**: Uses `BeautifulSoup` to locate and extract the `<title>` tag.
- **Persistent Logging**: Appends scraped titles and URLs alongside timestamps to `output/scraped_titles.txt`.
- **Fault-Tolerant**: Gracefully handles network failures, timeouts, HTTP errors (404/500), and missing title tags.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3.10+
- **Standard Library**:
  - `os` & `pathlib`: Cross-platform path resolution and file handling.
  - `shutil`: Secure file operations and moving.
  - `re`: Regular expressions for pattern recognition and email extraction.
  - `datetime`: Timestamp generation for scrapings.
- **Third-Party Libraries**:
  - `requests`: HTTP client for web fetching.
  - `beautifulsoup4` (`bs4`): HTML parsing and DOM navigation.

---

## 🧠 Python Concepts Demonstrated

1. **Filesystem Management (`pathlib.Path`, `shutil.move`, `os.path`)**: Handling directories, file extensions, and non-destructive moves.
2. **Regular Expressions (`re.findall`)**: Matching complex string patterns and text processing.
3. **Web Scraping & DOM Traversal**: Interacting with HTTP APIs and parsing HTML trees with BeautifulSoup.
4. **Data Deduplication**: Employing sets for $O(1)$ duplicate checking while preserving sequence.
5. **Defensive Programming & Exception Handling**:
   - `requests.exceptions.ConnectionError`, `requests.exceptions.Timeout`, `requests.exceptions.HTTPError`
   - `UnicodeDecodeError` with fallback encoding support (`utf-8` and `latin-1`).
   - File collision avoidance algorithm.

---

## 📂 Project Structure

```text
Task_3_Task_Automation/
│
├── automation.py       # Main menu-driven automation suite
├── requirements.txt    # External dependencies (requests, beautifulsoup4)
├── README.md           # Documentation and instructions
└── output/             # Output folder for extracted emails and scraped titles
    └── .gitkeep
```

---

## ⚙️ Installation & Setup

1. Open your terminal or VS Code terminal in the project directory:
   ```bash
   cd Task_3_Task_Automation
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 How to Run the Project

Run the main automation script:
```bash
python automation.py
```

---

## 🖥️ Sample Output

### Main Menu
```text
Welcome to the Task Automation Suite!

=============================================
         TASK AUTOMATION UTILITY         
=============================================
1. Automatic File Organizer
2. Email Extractor
3. Webpage Title Scraper
4. Exit
=============================================
Enter your choice (1-4): 
```

### 1. Automatic File Organizer Output
```text
==================================================
       FEATURE 1: AUTOMATIC FILE ORGANIZER       
==================================================
Enter the source folder path: D:\Downloads
Enter the destination folder path (press Enter to organize inside source folder): 

>> Found 5 file(s) to organize. Processing...

=============================================
       ORGANIZATION SUMMARY REPORT       
=============================================
Images         : 2 file(s) moved
Documents      : 1 file(s) moved
Videos         : 1 file(s) moved
Audio          : 0 file(s) moved
Other          : 1 file(s) moved
---------------------------------------------
Total Files Moved: 5
Destination Path : D:\Downloads
=============================================
```

### 2. Email Extractor Output
```text
==================================================
          FEATURE 2: EMAIL EXTRACTOR             
==================================================
Enter path to text file (.txt): sample_contacts.txt

>> Extraction complete! Found 3 unique email address(es).

--- Extracted Emails ---
 1. internship@codealpha.com
 2. support@techdomain.org
 3. student.help@university.edu
------------------------------
Enter output file path (press Enter for default: '.../output/extracted_emails.txt'): 
>> Successfully saved 3 email(s) to '.../output/extracted_emails.txt'.
```

### 3. Webpage Title Scraper Output
```text
==================================================
       FEATURE 3: WEBPAGE TITLE SCRAPER          
==================================================
Enter webpage URL (e.g., https://www.python.org): python.org
>> Fetching webpage: https://python.org ...

---------------------------------------------
URL   : https://python.org
Title : Welcome to Python.org
---------------------------------------------
Enter output file path (press Enter for default: '.../output/scraped_titles.txt'): 
>> Successfully appended title to '.../output/scraped_titles.txt'.
```

---

## 🏆 Internship Evaluation Checklist

- [x] Menu-driven utility with 3 distinct automation workflows
- [x] Feature 1: Asks for source & destination, organizes into 5 categories
- [x] Feature 1: Creates folders automatically & prevents overwriting (`_1`, `_2`)
- [x] Feature 1: Displays complete summary report
- [x] Feature 2: Reads `.txt` file, extracts emails with regex
- [x] Feature 2: Deduplicates emails and displays total count
- [x] Feature 2: Saves clean emails to text file
- [x] Feature 3: Accepts URL, fetches via requests, extracts title via BeautifulSoup
- [x] Feature 3: Saves title & URL with timestamps
- [x] Feature 3: Handles invalid URLs, network/connection errors gracefully
