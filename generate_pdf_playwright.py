from playwright.sync_api import sync_playwright
import os

def generate_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Load the local HTML file
        url = f"file://{os.path.abspath('index.html')}"
        page.goto(url)
        
        # Wait for network idle to ensure fonts/images load
        page.wait_for_load_state('networkidle')
        
        # Generate PDF
        # Using 10mm vertical margins (approx 2.5%) as requested
        page.pdf(
            path="Anna_Margareth_Njau_Resume.pdf",
            format="A4",
            print_background=True,
            margin={"top": "10mm", "bottom": "10mm", "left": "0mm", "right": "0mm"}
        )
        
        browser.close()
        print("PDF generated successfully using Playwright.")

if __name__ == "__main__":
    generate_pdf()
