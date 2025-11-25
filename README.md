WeatherWise Console Application
This project is a simple Python script that acts as a Real Time Weather Forecast Application for the command line. It fetches current weather data for any specified city using a public weather API.

Features
Real Time Data Fetches current temperature, humidity, wind speed, and weather condition.

City Search Prompts the user to enter a city name for immediate weather lookup.

API Integration Uses the OpenWeatherMap API for data retrieval.

Error Handling Gracefully handles network issues, invalid city names (404), and other request failures.

Technology
Language Python

Library requests for making HTTP API calls

Getting Started
Prerequisites
Python 3 installed on your system.

The requests library. Install it using pip:

Bash

pip install requests
An API Key from OpenWeatherMap.

Setup and Execution
Save the Code Save the provided Python code into a file named weather_script.py.

Insert API Key Open weather_script.py and replace the placeholder value:

Python

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
with your actual OpenWeatherMap key.

Run the Script Execute the file from your terminal:

Bash

python weather_script.py
Input When prompted, enter the name of the city you wish to check.

Example Output
After running the script and entering "London", the output will look similar to this:

Enter a city name: London
========================================
Weather in London, GB
========================================
Temperature: 15.2°C
Condition: Clouds
Humidity: 80%
Wind Speed: 3.6 m/s
========================================
Functions
get_weather(city_name)
Handles the API communication. It constructs the request URL with the API key and city name, performs the GET request, and handles any HTTP or connection errors.

display_weather_info(data)
Parses the JSON response data from the API and prints the essential weather details (city, country, temperature, humidity, condition, wind speed) to the console in a formatted block.

Author
Malaika Bala
