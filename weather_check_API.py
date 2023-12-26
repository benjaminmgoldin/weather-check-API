import requests

#Enter your API key below from openweathermap
API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input ("Please enter a city name:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

#Code currently displays temperature in fahrenheit, the API currently provides temperature in kelvin
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = (data["main"]["temp"] * 1.8 - 459.67)
    
    print("Weather:", weather)
    print("Temperature:", temperature, "fahreinheit")    
else:
    print("This city is not recognized")
