"""
@ Author: Syed Muhammad Hussnain Raza
@ Date: September 23, 2025
@ Description: Downloads the laptops page from myshop.pk and saves it as an HTML file in the 'out' folder.
@ Dependencies: requests
@ Inputs: URL of the laptops page
@ Outputs: out/myshop_laptops.html
@ LastModified: September 24, 2025
"""

import os
import requests

# Create output folder if it doesn't exist
os.makedirs("out", exist_ok=True)

# Target URL
url = "https://myshop.pk/laptops-desktops-computers/laptops"

# Send GET request
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Check if successful
if response.status_code == 200:
    # Save HTML to file inside 'out' folder
    with open("out/myshop_laptops.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("✅ Page downloaded successfully and saved as out/myshop_laptops.html")
else:
    print(f"❌ Failed to download page. Status code: {response.status_code}")
