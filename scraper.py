from playwright.sync_api import sync_playwright
import re

# Paste your 10 Seed links here
URLS = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=56", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=57", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=58", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=59", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=60",
    "https://sanand0.github.io/tdsdata/js_table/?seed=61", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=62", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=63", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=64", 
    "https://sanand0.github.io/tdsdata/js_table/?seed=65"
]

def main():
    total_sum = 0
    
    with sync_playwright() as p:
        # Launch headless Chromium
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for url in URLS:
            if not url.startswith("http"):
                continue
                
            page.goto(url)
            
            # Extract all text from every table cell (<td>) on the page
            cells = page.locator("td").all_inner_texts()
            
            for cell in cells:
                # Find all numbers in the cell text (handles integers and decimals)
                numbers = re.findall(r'[-+]?\d*\.\d+|\d+', cell)
                for num in numbers:
                    total_sum += float(num)
                    
        browser.close()
        
    print(f"GRAND TOTAL SUM: {total_sum}")

if __name__ == "__main__":
    main()
