Software Grabber: The Data-Building Engine

The Software Grabber is a logic-based data extraction utility designed to bridge the gap between raw web content and structured application databases. It acts as a "Builder Engine," transforming fragmented online information into standardized JSON and CSV repositories to power your software's backend.

1. Installation Guide

Set up your environment by running these commands in your terminal:

Windows:

python -m venv venv
venv\Scripts\activate
pip install requests beautifulsoup4


macOS / Linux:

python3 -m venv venv
source venv/bin/activate
pip3 install requests beautifulsoup4


2. Configuration & Usage

To build your dataset, you must configure the "Target" and the "Map" inside data_grabber.py:

Input Your Links: Locate the target_urls list. Replace the examples with the direct links you want to grab data from.

target_urls = ["[https://example.com/item1](https://example.com/item1)", "[https://example.com/item2](https://example.com/item2)"]


Map Selectors: Update the app_store_map dictionary. Right-click a webpage element -> Inspect to find the CSS class or ID.

For <h1 class="title">, use "name": "h1.title".

For <div id="price">, use "price": "#price".

Run the Engine: Execute the script:

python data_grabber.py


3. Accessing Your Data

The engine automatically creates a folder named grabbed_data in your project directory.

For Spreadsheets: Open app_store_catalog.csv with Excel or Google Sheets.

For App Development: Use app_store_catalog.json for your database logic.

4. Key Capabilities

Identity Masking: Uses custom User-Agents to mimic real browser behavior and avoid blocks.

Error Resilience: Built-in timeout management prevents crashes during bulk extraction.

Data Building: Automatically overwrites files with the newest data to keep your app catalog current.

By automating data acquisition, the Software Grabber allows you to focus on building features while it handles the heavy lifting of data construction.
