"""
@ Author: Syed Muhammad Hussnain Raza
@ Date: September 23, 2025
@ Description: Parses the saved HTML file (out/myshop_laptops.html) to extract product details:
              Title, Price, Description, Image URL.
              Saves the parsed data to out/products.json.
@ Dependencies: BeautifulSoup4, json, os
@ Inputs: out/myshop_laptops.html
@ Outputs: out/products.json
@ LastModified: September 24, 2025
"""

import os
import json
from bs4 import BeautifulSoup

# Ensure output folder exists
os.makedirs("out", exist_ok=True)

# Load saved HTML from 'out' folder
with open("out/myshop_laptops.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
product_cards = soup.find_all("li", class_="item product product-item")

products_list = []

for p in product_cards:
    # Title
    title_tag = p.find("a", class_="product-item-link")
    title = title_tag.get_text(strip=True) if title_tag else None

    # Price
    price_tag = p.find("span", class_="price")
    price = price_tag.get_text(strip=True) if price_tag else None

    # Description
    desc_tag = p.find("div", class_="mso_listing_detail")
    description = desc_tag.get_text(strip=True) if desc_tag else None

    # Image URL (handle lazy-loaded images)
    img_tag = p.find("img", class_="product-image-photo")
    if img_tag:
        image_url = img_tag.get("data-amsrc") or img_tag.get("src")
    else:
        image_url = None

    # Include only the 4 attributes
    product_dict = {
        "Title": title,
        "Price": price,
        "Description": description,
        "Image URL": image_url
    }

    products_list.append(product_dict)

# Save to JSON in 'out' folder
with open("out/products.json", "w", encoding="utf-8") as f:
    json.dump(products_list, f, ensure_ascii=False, indent=4)

print("✅ JSON file 'out/products.json' saved successfully with all products!")
