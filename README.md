# MyShop Laptops Scraper

**Author:** Syed Muhammad Hussnain Raza  
**Date:** September 24, 2025

---

## Project Description

This project is a **modular web scraping tool** designed to extract product data (laptops) from this landing page of [myshop.pk](https://myshop.pk/laptops-desktops-computers/laptops) and save it into structured formats. The workflow is divided into three modules:

1. **html_getter.py** – Downloads the laptops page and saves it as an HTML file.
2. **html_parser.py** – Parses the saved HTML to extract **Title, Price, Description, and Image URL**. Saves data as `products.json`.
3. **excel_generator.py** – Reads `products.json` and generates an Excel file (`products.xlsx`) with auto-adjusted column widths.

This modular approach allows **easy debugging, testing, and future extension** (e.g., scraping multiple pages).

---

## Folder Structure

```
/project_root
│
├── html_getter.py
├── html_parser.py
├── excel_generator.py
├── out/                 # Output folder for saved files
|   ├── myshop_laptops.html
|   ├── products.json
|   ├── products.xlsx
└── README.md
```

---

## Dependencies

Make sure you have Python 3 installed. Install the required packages using `pip`:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

| Module           | Purpose                                    |
| ---------------- | ------------------------------------------ |
| `requests`       | Fetches web pages from myshop.pk           |
| `BeautifulSoup4` | Parses HTML content                        |
| `pandas`         | Handles structured data and Excel creation |
| `openpyxl`       | Excel writing and formatting support       |

---

## Usage

1. **Download HTML**

```bash
python html_getter.py
```

This will save `out/myshop_laptops.html`.

2. **Parse HTML to JSON**

```bash
python html_parser.py
```

This will generate `out/products.json` with product details.

3. **Generate Excel from JSON**

```bash
python excel_generator.py
```

This will generate `out/products.xlsx` with all products and auto-fitted columns.

---

## Notes

- The scripts are designed to work sequentially:
  1. `html_getter.py` → 2. `html_parser.py` → 3. `excel_generator.py`
- The parser handles **lazy-loaded images** (`data-amsrc`) to ensure correct product image URLs.
- You can update the URL in `html_getter.py` to scrape other categories if needed.
- The project is modular, so each script can also be run independently for testing or reuse.

---

## License

This project is open-source and free to use for personal and educational purposes.
