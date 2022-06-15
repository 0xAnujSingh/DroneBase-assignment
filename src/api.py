import requests, json
import datetime

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "eede56c9de2ca2b0bc5d104f8803a8e3"

def validate(date): 
   # date = input("Enter date for scheduled fight (in DD/MM/YYYY): ")
   ex_date = datetime.datetime.strptime(date, "%d/%m/%Y")
   try:
      dt = datetime.datetime.now()
      # print(dt)
      datetime.datetime.strptime(date, '%d/%m/%Y')
      if ex_date > dt:
         return 1
      else:
         print("You entered wrong date")
         return 0
   except ValueError:
      raise ValueError("Incorrect data format, should be DD-MM-YYYY")

def getWeather(cityName):
   url = f"{BASE_URL}?q={cityName}&appid={API_KEY}"

   response = requests.get(url)

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
      
      print(f"{cityName:-^30}".upper())
      print(f"Temperature: {temperature}")
      print(f"Humidity: {humidity}")
      print(f"Pressure: {pressure}")
      print(f"Wind speed : {windSpeed}")
      print(f"Wind degree: {windDegree}")
      print(f"Weather Report: {report[0]['description']}")

   else:
      print("Error in the HTTP request")
