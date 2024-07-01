import requests

def search_gifs(search_term, api_key, limit=5):
    url = f"https://api.giphy.com/v1/gifs/search"
    params = {
        'api_key': api_key,
        'q': search_term,
        'limit': limit
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  

        data = response.json()
        gif_urls = []
        for gif in data['data']:
            gif_urls.append(gif['images']['original']['url'])
        return gif_urls
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


    
api_key = 'Fw50p4luTUW97pO9beb8E6WeDlVWTlV9'

search_term = input("Enter a search term to find GIFs: ")
gif_urls = search_gifs(search_term, api_key)

if gif_urls:
    print(f"Here are the GIFs related to '{search_term}':")
    for url in gif_urls:
        print(url)
else:
    print(f"No GIFs found for '{search_term}'.")
