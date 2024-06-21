import requests

def get_weather(api_key, lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': api_key,
        'lat': lat,
        'lon': lon,
        'units': 'metric',
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def get_geocode(api_key, place, limit=1):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "appid": api_key,
        "q": place,
        "limit": limit,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "API KEY" 
    place = input("Enter place: ")
    geocode_data = get_geocode(api_key, place)
    
    if geocode_data:
        lat = geocode_data[0]['lat']
        lon = geocode_data[0]['lon']
        weather_data = get_weather(api_key, lat, lon)
        
        if weather_data:
            print(f"Weather in {place}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Weather: {weather_data['weather'][0]['description']}")
        else:
            print("Failed to get weather data.")
    else:
        print("Failed to get geocode data.")
