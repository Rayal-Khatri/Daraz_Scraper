import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.selector import Selector 
from ..utils import parse_item_page


class ClientSideSpider(scrapy.Spider):
    name = 'daraz_flash_sale'
    allowed_domains = ['https://www.daraz.com.np','www.daraz.com.np','daraz.com.np']  

    # Entry point for starting requests
    def start_requests(self):
        url = 'https://pages.daraz.com.np/wow/gcp/route/daraz/np/upr/router?hybrid=1&data_prefetch=true&prefetch_replace=1&at_iframe=1&wh_pid=%2Flazada%2Fchannel%2Fnp%2Fflashsale%2FeBQX2YfTXs&hide_h5_title=true&lzd_navbar_hidden=true&disable_pull_refresh=true&skuIds=105485983%2C128126693%2C129619760%2C128294831%2C157857545%2C122148470%2C129575275&spm=a2a0e.tm80335409.FlashSale.d_shopMore'
        yield SeleniumRequest(
            url=url, 
            wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, 'a.flash-unit-a')),
            wait_time= 2,
            callback=self.parse, 
        )



    def parse(self, response):
        driver = response.meta['driver']

        # -------------------------------TO LOAD MORE--------------------
        # while True:
        #     try:
        #         load_more_button = WebDriverWait(driver, 5).until(
        #             EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.button.J_LoadMoreButton'))
        #         )
        #         load_more_button.click()  

        #     except Exception as e:
        #         print("No more 'Load More' button found or unable to click:", e)
        #         break

        
        a = 0   # To scrape only 2 items for testing
        current_html = driver.page_source
        current_page_selector = Selector(text=current_html)
        items =  current_page_selector.css('a.flash-unit-a')
        
        print("************************************************************** TOTAL ITEMS ="+ str(len(items))+ "********************************************************")
        
        
        # -------------------------------------FOR SCRAPING INDIVIDUAL ITEMS-----------------------------------
        for item in items:
            next_url = "https:"+ item.xpath('@href').get()
            yield SeleniumRequest(
                url=next_url,
                wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, '.pdp-mod-product-badge-title')),
                wait_time=2,
                callback=self.parse_item_page_callback
            )
            # To scrape only 2 items for testing
            a +=1
            if a>1:
                break
            

        

    async def errback(self, failure):
        page = failure.request.meta['playwright_page']
        await page.close()

   

    def parse_item_page_callback(self, response):
        driver = response.meta['driver']
        product_data = parse_item_page(driver, response)
        yield product_data



