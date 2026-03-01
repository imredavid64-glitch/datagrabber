import requests
from bs4 import BeautifulSoup
import json
import csv
import os

class SoftwareGrabber:
    """
    A logic-based scraper that extracts specific data points from URLs
    and builds a local data repository for application use.
    """
    
    def __init__(self, output_dir="grabbed_data"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def grab_url(self, url, selectors):
        """
        Grabs data from a URL based on a dictionary of CSS selectors.
        Example selectors: {'title': 'h1', 'price': '.app-header__price'}
        """
        print(f"[*] Fetching: {url}")
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            extracted_data = {}
            for key, selector in selectors.items():
                element = soup.select_one(selector)
                extracted_data[key] = element.get_text(strip=True) if element else "N/A"
                
            return extracted_data
        except Exception as e:
            print(f"[!] Error grabbing {url}: {e}")
            return None

    def build_dataset(self, name, data_list):
        """
        Saves grabbed data into JSON and CSV formats to build the foundation
        of your software's database.
        """
        json_path = os.path.join(self.output_dir, f"{name}.json")
        csv_path = os.path.join(self.output_dir, f"{name}.csv")

        # Save JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, indent=4)

        # Save CSV
        if data_list:
            keys = data_list[0].keys()
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                dict_writer = csv.DictWriter(f, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(data_list)
        
        print(f"[+] Data built successfully: {json_path} and {csv_path}")

# --- Logic to "Build the App" based on grabbed data ---
def run_grabber_engine():
    grabber = SoftwareGrabber()

    # Define what we want to grab (Example: Apple App Store Apps)
    # You can add as many URLs as you want to "build" your app's content
    target_urls = [
          "[https://example.com/item1](https://example.com/item1)",
        "[https://example.com/item2](https://example.com/item2)"
    ]

    # Map the site's CSS structure
    app_store_map = {
        "app_name": "h1.product-header__title",
        "developer": "h2.product-header__subtitle",
        "rating": "span.we-customer-ratings__averages__display",
        "price": "li.inline-list__item.inline-list__item--bulleted"
    }

    all_grabbed_apps = []

    for url in target_urls:
        data = grabber.grab_url(url, app_store_map)
        if data:
            all_grabbed_apps.append(data)

    # Build the database file that your app will read from
    grabber.build_dataset("app_store_catalog", all_grabbed_apps)

if __name__ == "__main__":
    run_grabber_engine()
