# Web Scraping with Playwright - README

## Overview
This project demonstrates how to use the **Playwright** library to perform web scraping tasks. Specifically, the script navigates to a webpage containing hotel listings, counts the number of hotel elements present, and allows further customization for more advanced scraping tasks.

---

## Prerequisites
Before running the project, ensure you have the following installed:

1. **Python 3.7 or higher**
2. **Playwright library**

---

## Installation Steps
1. Clone this repository or copy the code into a new Python file, e.g., `hotel_scraper.py`.
2. Open a terminal in your project directory.

### Install Playwright and Dependencies
Run the following commands:
```bash
pip install playwright
```

### Install Playwright Browsers
After installing the library, run:
```bash
playwright install
```
This command downloads the required browsers (Chromium, Firefox, and WebKit).

---

## How to Use
1. Open the script file `hotel_scraper.py` and set the variable `page_url` to the URL of the webpage you want to scrape.

   Example:
   ```python
   page_url = 'https://example.com/hotels'
   ```

2. Run the script:
   ```bash
   python hotel_scraper.py
   ```

3. The script will:
   - Launch a Chromium browser.
   - Navigate to the specified URL.
   - Identify and count hotel elements on the page.
   - Print the number of hotels found to the console.

---

## Code Explanation
### Key Components
1. **`sync_playwright`:**
   The main API to control browser automation synchronously.

2. **Browser Launch:**
   ```python
   browser = p.chromium.launch()
   ```
   This line launches the Chromium browser in headless mode (default).

3. **XPath Selection:**
   ```python
   hotels = page.xpath('//div[@data-testid="property-card"]')
   ```
   Locates hotel cards on the webpage using an XPath expression.

4. **Hotel Count:**
   ```python
   print(f'There are: {len(hotels)} hotels.')
   ```
   Outputs the total number of hotel elements found on the page.

### Customization
You can modify the XPath expression or extend the script to extract specific data, such as hotel names, prices, or ratings.

---

## Troubleshooting
### Common Issues
1. **Playwright Installation Errors:**
   - Ensure `pip` is updated:
     ```bash
     python -m pip install --upgrade pip
     ```
   - Reinstall Playwright:
     ```bash
     pip install playwright --force-reinstall
     ```

2. **Browser Launch Issues:**
   - Verify that Playwright browsers are installed using:
     ```bash
     playwright install
     ```

3. **XPath Errors:**
   - Check if the webpage structure or XPath selector has changed.

---

## Notes
- This script uses **Chromium** by default. You can change the browser to Firefox or WebKit by replacing `p.chromium` with `p.firefox` or `p.webkit`.
- The script assumes the webpage loads elements statically. For dynamic loading (e.g., via JavaScript), you may need to add a wait method, such as:
  ```python
  page.wait_for_selector('selector')
  ```

---

## References
- [Playwright Python Documentation](https://playwright.dev/python/)
- [XPath Syntax Guide](https://www.w3schools.com/xml/xpath_syntax.asp)

