
import requests, json
import csv
from bs4 import BeautifulSoup

# URL to get access API to get weather details
url = "http://api.openweathermap.org/data/2.5/weather?q=County%20Monaghan&units=metric&appid=688e3e96f2954d9cfc65fffe4aa9f62c&current#current_XML"

# Enter your API key here 
api_key = "688e3e96f2954d9cfc65fffe4aa9f62c"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = 'County Monaghan'
  
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

# get method of requests module 
# return response object 
response = requests.get(complete_url) 
result = response.json() 
  
# Compare the cod key value and if it is not equal to 404 means it exists in the list

if result["cod"] != "404": 
 
    Weather = result["main"] 
  
    current_temperature = Weather["temp"] 
   
    current_FeelsLike = Weather["feels_like"] 
 
    current_temp_min = Weather["temp_min"] 
  
    # print following values 
    print(" Temperature = " +
                    str(current_temperature) + 
          "\n Feels Like = " +
                    str(current_FeelsLike) +
          "\n Minium Temperature = " +
                    str(current_temp_min) )
else: 
    print(" City Not Found ") 


