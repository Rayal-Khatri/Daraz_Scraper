# DarazScraper

## Overview

**DarazScraper** is a powerful web scraping tool designed for collecting product data from the Daraz e-commerce platform. It efficiently retrieves detailed product information including prices, ratings, delivery options, and stock status, storing the data in CSV format by default with optional database integration support.

## Features

- **Dual Spider System:**
  - `daraz_flash_sale`: Dedicated spider for flash sale items
  - `daraz_item`: Flexible spider for general product search
- **Data Collection:** Comprehensive product details including prices, ratings, and availability
- **Output Flexibility:** CSV output by default with database storage options
- **Dynamic Content Handling:** Uses Selenium for JavaScript-rendered content
- **Customizable Settings:** Configurable timeouts and page load strategies

## Prerequisites

- Python 3.6+
- Chrome browser
- ChromeDriver (matching your Chrome version)
- Required Python packages:
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

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
   - Select the version matching your Chrome browser
   - Add ChromeDriver to your system PATH

## Usage

### Scraping Flash Sale Items

To collect data from Daraz's current flash sale:

```bash
scrapy crawl daraz_flash_sale -O flash_sale_data.csv
```

### Scraping Search Results

To scrape products based on a search term:

```bash
scrapy crawl daraz_item -a search_term="laptop" -O laptop_search_data.csv
```

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

Common customizations include:
- Adding new fields to scrape
- Modifying parsing logic
- Implementing filters

### Settings Configuration

Adjust scraping behavior in `settings.py`:

```python
# Example settings
DOWNLOAD_DELAY = 2  # Time between requests
ROBOTSTXT_OBEY = True
SELENIUM_DRIVER_ARGUMENTS = ['--headless']  # Run in headless mode
```

## Data Structure

The scraped data includes:
- Product name
- Price (current and original)
- Discount percentage
- Rating and review count
- Seller information
- Stock status
- Delivery options

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
