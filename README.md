Software Grabber: Data-Building Engine

The Software Grabber is a logic-based data extraction utility designed to bridge the gap between raw web content and structured application databases. It acts as a "Builder Engine," transforming fragmented online information into standardized JSON and CSV repositories to power your software's backend.

1. Installation Guide

It is recommended to use a virtual environment to keep your global Python installation clean.

Windows:

python -m venv venv
venv\Scripts\activate
pip install requests beautifulsoup4


macOS / Linux:

python3 -m venv venv
source venv/bin/activate
pip3 install requests beautifulsoup4


2. Configuration & Usage

To build your custom dataset, you must configure the Target and the Map inside data_grabber.py:

Input Your Links: Locate the target_urls list inside the run_grabber_engine() function. Replace the example URLs with the direct links you want to grab data from.

target_urls = ["[https://example.com/item1](https://example.com/item1)", "[https://example.com/item2](https://example.com/item2)"]


Map Selectors: Update the app_store_map dictionary. Use your browser's "Inspect Element" tool to find the unique CSS class or ID for each data point.

For a title like <h1 class="main-title">, use "name": "h1.main-title".

For a price like <div id="price">, use "price": "#price".

Run the Engine: Execute the script from your terminal:

python data_grabber.py


3. Accessing Your Data

The engine automatically creates a folder named grabbed_data in your project directory.

For Spreadsheets: Open app_store_catalog.csv with Excel or Google Sheets.

For App Development: Use app_store_catalog.json to feed data into your app logic.

4. Key Capabilities

Identity Masking: Uses custom User-Agents to mimic real browser behavior and avoid basic bot detection.

Error Resilience: Built-in timeout management prevents the script from hanging during bulk extraction.

Automated Database: Automatically builds/overwrites files with the newest data on every run.

Focus on building your application's features; let the Software Grabber handle the heavy lifting of data construction.
