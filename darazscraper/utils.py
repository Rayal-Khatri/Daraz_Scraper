from darazscraper.items import Products
import time
from selenium.webdriver.common.by import By

def parse_item_page(self, response):
        driver = response.meta['driver']
        print("*************************THE ITEM IS BEING SCRAPED******************")
        Product = Products()
        # Scroll to the middle of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")  # Scroll to the middle
        time.sleep(3)
        try:
            rating = driver.find_element(By.CSS_SELECTOR, 'span.score-average').text.strip()
        except Exception as e:
            rating = 'No rating' 
        Product['name'] = response.css('.pdp-mod-product-badge-title::text').get()
        Product['price'] = response.css('.pdp-price_size_xl::text').get()
        Product['rating']=rating
        Product['no_of_review']= response.css('.pdp-review-summary__link::text').get()
        Product['delivery_price']= response.css('.delivery-option-item_type_standard .no-subtitle::text').get()
        Product['seller']= response.css('.seller-name__detail-name::text').get()
        Product['seller_rating']= response.css('.rating-positive::text').get()
        Product['delivery_rating' ]= response.css('.info-content:nth-child(2) .seller-info-value::text').get()
        Product['stock']= response.css('#module_quantity-input input').xpath('@max').get()
        return Product