import requests
from datetime import datetime

api_key = '809574af50c3f5b93a8815ba29f62b90'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_data = requests.get(complete_api_link).json()

if api_data['cod'] not in range(200, 300):
    print(api_data['message'])
    quit()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

data = ["-------------------------------------------------------------",
        f"Weather Stats for - {location}  || {date_time}",
        "-------------------------------------------------------------",
        "Current temperature is: {:.2f} {}C".format(temp_city,chr(176)),
        f"Current weather desc  :{weather_desc}",
        f"Current Humidity      :{hmdt} %",
        f"Current wind speed    :{wind_spd} kmph"
       ]

data='\n'.join(data)
print(data)

with open('weather_report.txt','w') as file:
    file.write(data)
