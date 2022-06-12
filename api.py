import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


CITY = input("Enter the city name: ")
# CITY = "Mhow"
API_KEY = "eede56c9de2ca2b0bc5d104f8803a8e3"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
   data = response.json()

   main = data['main']
   wind = data['wind']
   
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   
   windSpeed = wind['speed']
   windDegree = wind['deg'] 
   
   report = data['weather']
   
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Wind speed : {windSpeed}")
   print(f"Wind degree: {windDegree}")
   print(f"Weather Report: {report[0]['description']}")

else:
   print("Error in the HTTP request")


