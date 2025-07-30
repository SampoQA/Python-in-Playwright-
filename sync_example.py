from playwright.sync_api import sync_playwright  

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=True to run in the background
    page = browser.new_page()  # Create a new page
    page.goto("https://na-yazyke-kitov.tilda.ws/")  # Navigate to the website
    page.wait_for_load_state("networkidle") # Wait for the page to load completely IMPORTANT FOR screenshot
    page.screenshot(path="screenshoot/homepage.png")  # Take a screenshot
    print(page.title())  # Print the page title
    browser.close()
