from bs4 import BeautifulSoup
import requests

base_url = 'url'

for page_number in range(1, 5):
    url = f'{base_url}{page_number}/'
    print(f"Fetching URL: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        web_content = response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the web page: {e}")
        continue  
    
    try:
        soup = BeautifulSoup(web_content, 'html.parser')
    except Exception as e:
        print(f"Error parsing the web page: {e}")
        continue 
    
    post_listing_div = soup.find('div', {'class': 'posts-listing'})

    if post_listing_div:
        
        feature_image_divs = post_listing_div.find_all('div', {'class': 'featured_image'})
        
        if not feature_image_divs:
            print("No <div> elements with class 'featured_image' found.")
        else:
            for j, feature_image_div in enumerate(feature_image_divs, start=1):
                print(f"Feature Image Div {j}:")
                # Find the next <p> tag following the 'featured_image' div
                next_p = feature_image_div.find_next_sibling('p')
                if next_p:
                    print(next_p.get_text())
                else:
                    print("No <p> tag found following this <div>.")
                print("-" * 20)
    else:
        print("No <div> with class 'posts-listing' found.")
        
    print(f"Page {page_number} completed")
