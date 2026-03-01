Software Grabber

The Software Grabber is a logic-based data extraction engine that transforms web content into structured JSON and CSV repositories to power your application's backend.

1. Installation

Windows:

python -m venv venv
venv\Scripts\activate
pip install requests beautifulsoup4


macOS / Linux:

python3 -m venv venv
source venv/bin/activate
pip3 install requests beautifulsoup4


2. Configuration & Usage

Input Links: In data_grabber.py, update target_urls with your desired links.

Map Selectors: Update app_store_map with CSS selectors (e.g., "name": "h1.title").

Run: Execute python data_grabber.py.

3. Accessing Data

The engine creates a grabbed_data folder in your project directory:

CSV: Open app_store_catalog.csv for Excel/Spreadsheets.

JSON: Use app_store_catalog.json for app development.

4. Key Features

Identity Masking: Uses User-Agents to mimic real browsers.

Error Resilience: Built-in timeouts to prevent hanging.

Automated Building: Overwrites files with fresh data on every run.

Focus on your app's features; let the Grabber handle the data construction.
