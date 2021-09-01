import requests
import json

API_KEY = "4a15ccbfba1199ff97f2b381fab0ed04"
LATITUDE = 27.664827
LONGITUDE = -81.515755


api_connection = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?"
                              f"lat={LATITUDE}&lon={LONGITUDE}&exclude=current,minutely,daily&appid={API_KEY}")

# THIS CHECKS STATUS CODE OF THE CONNECTION WITH API SERVER/
print(api_connection.status_code)

weather_info = api_connection.json()

# WRITES API RESPONSE INTO A JSON FILE, ADD INDENT ARG TO MAKE MORE READABLE
# with open("weather_data.json", "w") as info:
#     json.dump(weather_info, info, indent=1)

# OPEN FILE AS READ AND PULL DATA VIA DIC STYLE
with open("weather_data.json", "r") as info:
    my_area_info = json.load(info)
    index = 0
    for i in my_area_info['hourly']:
        index += 1
        for j in i['weather']:
            weather_code = j['id']
            if weather_code >=800:
                print(f"{index} Hour we will expect some rain")
            else:
                print(f"{index} Hour we will expect some clouds but no rain")
