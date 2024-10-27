from itemadapter import ItemAdapter


class DarazscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        rating = adapter.get('rating')
        if rating == 'No rating':
            adapter['rating'] = 0.0 
        elif rating is not None:
            adapter['rating'] = float(rating)
        else:
            adapter['rating'] = 0.0

        stock = adapter.get('stock')
        adapter['stock'] = float(stock) if stock is not None else 0.0



        
        value = adapter.get('no_of_review')
        value = value.replace(' Ratings','')
        adapter['no_of_review']= float(value) if value is not None else 0.0

        price_keys= ['price','delivery_price']
        for price_key in price_keys:
            if value is not None:
                value = value.replace('Rs.', '')
                adapter[price_key] = float(value)
            else:
                adapter[price_key] = 0.0


        special_ratings = ['delivery_rating', 'seller_rating']
        for special_rating in special_ratings:
            value = adapter.get(special_rating)
            if value is None or value == 'Not enough data':
                value = '0'
            else:
                value = value.replace('%','')
            adapter[special_rating] = float(value)

        return item




