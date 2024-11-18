# DarazScraper

## Overview

**DarazScraper** is a powerful web scraping tool designed for collecting product data from the Daraz e-commerce platform. It efficiently retrieves detailed product information including prices, ratings, delivery options, and stock status, storing the data in CSV format by default with optional database integration support.

## Features

- **Dual Spider System:**
  - `daraz_flash_sale`: Dedicated spider for flash sale items
  - `daraz_item`: Flexible spider for general product search

## Prerequisites

- Python 3.6+
- Chrome browser
- ChromeDriver (Present in git: needs to match your Chrome version)
- Required Python packages (Present in virtual environment):
  - Scrapy
  - Selenium

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DarazScraper.git
   cd DarazScraper
   ```

2. Set up virtual environment:

   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Download ChromeDriver (If version doesnt match):
   - Visit [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
   - Select the version matching your Chrome browser
   - ⚠️ **Important:** Update SELENIUM_DRIVER_EXECUTABLE_PATH in settings.py to yout ChromeDriver path
  
     ![Replace Code here](https://drive.google.com/uc?id=1pWlTstacCMfH2AHCNFlkWQVx6ej16xo9 "Code Replace")


## Usage
Make sure you are inside the darazscraper folder 

### Scraping Flash Sale Items

To collect data from Daraz's current flash sale (Might take about 40 minutes):

```bash
scrapy crawl daraz_flash_sale -O <'dataset name'>.<'extension'>
```

### Scraping Search Results

- To scrape products based on a search term:

```bash
scrapy crawl daraz_item -O <'dataset name'>.<'extension'>
```
- Enter the name of the product that you want to search 
- Enter the number of pages you want to scrape.( Each page has 40 items and it takes about 6.1 minutes)
- Enter 999 to scrape all of the products


### Output Formats

- Use `-O` for overwriting output files
- Use `-o` for appending to existing files
- Supported formats:
  - CSV: `-O results.csv`
  - JSON: `-O results.json`
  - XML: `-O results.xml`

## Customization

### Spider Modification

The spiders can be customized in their respective files:
- `spiders/daraz_flash_sale.py`
- `spiders/daraz_item.py`


### Settings Configuration

```
SELENIUM_DRIVER_ARGUMENTS = [
    '--no-sandbox', 
    '--disable-dev-shm-usage'
    '--page-load-strategy=eager',
    '--disable-site-isolation-trials',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-images',
    '--blink-settings=imagesEnabled=false'
]
```
- Add '--headless' to run in headless mode (Without the browser)


## Data Structure

The scraped data includes:
- Product name
- Price
- Discount percentage
- Rating
- Review count
- Seller information
- Stock status
- Delivery Price

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Always check Daraz's terms of service and robots.txt before scraping. Consider implementing appropriate delays and respect the website's crawling policies.
