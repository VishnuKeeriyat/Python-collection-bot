from playwright.sync_api import sync_playwright
import pandas as pd

def main():
    with sync_playwright() as p:

        checkingin_date = '2023-05-11'
        checkingout_date = '2023-05-12'

        page_url = f'https://www.booking.com/searchresults.en-gb.html?ss=London%2C+Greater+London%2C+United+Kingdom&ssne=Inverness&ssne_untouched=Inverness&label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4ApP286IGwAIB0gIkZTRmZTA0NDAtZTUxNi00MmQ5LTk0ODItOGJlZjk4MWU3OGVh2AIF4AIB&sid=4e74e6c6529d671c1eef7cd1bb415ec6&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2601889&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=24546598a925025f&ac_meta=GhAyNDU0NjU5OGE5MjUwMjVmIAAoATICZW46Bmxvbm9kbkAASgBQAA%3D%3D&checkin=2023-05-11&checkout=2023-05-12&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url, timeout=60000)
        
        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are: {len(hotels)} hotels.')

        hotels_dict = []
        for hotel in hotels:
            hotels_dict['hotel'] = xhotel.locator('div[@data-testid="title"]').inner_text()

            hotels_dict['price'] = hotel.locator('/div[@data-testid="price-and-discounted price"').inner_text()
            hotels_dict['score'] = hotel.locator('/div[@data-testid="review-score"]/div[1]').inner_text()
            hotels_dict['avg review'] = hotel.locator('/div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotels_dict['reviews count'] = hotel.locator('/div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            
            hotels_dict.append(hotels_dict)
        
        df = pd.DataFrame(hotels_dict)
        df.to.excel('hotels_list.xlsx' , index=False)
        df.to.excel('hotels_list.csv' , index=False)

        browser.close()
if __name__ == '__main__':
    main()