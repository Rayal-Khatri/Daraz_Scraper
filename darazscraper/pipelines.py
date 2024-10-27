from itemadapter import ItemAdapter 

class DarazscraperPipeline: 
    def process_item(self, item, spider): 
        adapter = ItemAdapter(item) 

        # Handle rating
        rating = adapter.get('rating') 
        if rating == 'No rating': 
            adapter['rating'] = 0.0  
        elif rating is not None: 
            adapter['rating'] = float(rating) 
        else: 
            adapter['rating'] = 0.0 

        # Handle stock
        stock = adapter.get('stock') 
        adapter['stock'] = float(stock) if stock is not None else 0.0 

        # Handle number of reviews
        reviews_value = adapter.get('no_of_review') 
        if reviews_value is not None:
            reviews_value = reviews_value.replace(' Ratings', '') 
            adapter['no_of_review'] = float(reviews_value) 
        else:
            adapter['no_of_review'] = 0.0 

        # Handle price and delivery_price
        price_value = adapter.get('price') 
        if price_value is not None:
            price_value = price_value.replace('Rs.', '').replace(',', '')  # Remove Rs. and commas
            adapter['price'] = float(price_value) 
        else:
            adapter['price'] = 0.0 

        delivery_price_value = adapter.get('delivery_price') 
        if delivery_price_value is not None:
            delivery_price_value = delivery_price_value.replace('Rs.', '').replace(',', '')  # Remove Rs. and commas
            adapter['delivery_price'] = float(delivery_price_value) 
        else:
            adapter['delivery_price'] = 0.0 

        # Handle special ratings
        special_ratings = ['delivery_rating', 'seller_rating'] 
        for special_rating in special_ratings: 
            value = adapter.get(special_rating) 
            if value is None or value == 'Not enough data': 
                value = '0' 
            else: 
                value = value.replace('%', '') 
            adapter[special_rating] = float(value) 

        return item
