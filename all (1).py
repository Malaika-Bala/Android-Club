import requests
import sys

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY" 
UNITS = "metric"

def get_weather(city_name):
    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("ERROR: API Key not set.")
        sys.exit(1)
        
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': UNITS
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"City '{city_name}' not found.")
        else:
            print(f"HTTP error: {http_err}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return None

def display_weather_info(data):
    if data is None:
        return

    city = data.get('name', 'N/A')
    country = data.get('sys', {}).get('country', 'N/A')
    
    main = data.get('main', {})
    temp = main.get('temp')
    humidity = main.get('humidity')
    
    weather_desc = data.get('weather', [{}])[0].get('description', 'No description')
    wind_speed = data.get('wind', {}).get('speed')
    
    print("\n" + "="*40)
    print(f"Weather in {city}, {country}")
    print("="*40)
    print(f"Temperature: {temp:.1f}°C")
    print(f"Condition: {weather_desc.title()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print("="*40 + "\n")


if __name__ == "__main__":
    city_input = input("Enter a city name: ").strip()
    
    if city_input:
        weather_data = get_weather(city_input)
        if weather_data:
            display_weather_info(weather_data)
    else:
        print("No city entered.")
