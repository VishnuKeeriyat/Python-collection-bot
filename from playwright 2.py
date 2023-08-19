from playwright.sync_api import sync_playwright

...

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(page_url)

        hotels = page.xpath('//div[@data-testid="property-card"]')
        print(f'There are: {len(hotels)} hotels.')

        # Rest of your code...
