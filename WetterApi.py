import requests
import datetime

class APIHandler:
    api_key = "5806995c2e7faa945b0de9add11473fa"
    def __init__(self):
        self.weather = Weather()
        self.city_name = ""
    def geocoding(self):
        self.city_name = input("Input city: ")
        country_code = input("Input country code(ISO 3166): ")
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={self.city_name},{country_code}&limit=1&appid={APIHandler.api_key}")
        geo_dict = response.json()
        return (geo_dict[0]["lat"], geo_dict[0]["lon"])

    def weather_data(self, lat, lon):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIHandler.api_key}&lang=de&units=metric") 
        r_dict = response.json() 
        desription = r_dict["weather"][0]["description"]
        curr_temp = r_dict["main"]["temp"]
        humidity = r_dict["main"]["humidity"]
        wind_speed = r_dict["wind"]["speed"]
        curr_time = r_dict["dt"]
        self.weather.add_weather_data(self.city_name, desription, curr_temp, humidity, wind_speed, curr_time)
        return self.weather
    
class Weather:
    def __init__(self):
        pass
    def add_weather_data(self, name, desc, temp, humidity, wind_speed, curr_time):
        self.city_name = name
        self.description = desc
        self.curr_temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.curr_time = datetime.datetime.fromtimestamp(int(curr_time)).strftime('%d-%m-%Y %H:%M:%S')

class WeatherApp:
    def __init__(self):
        self.api = APIHandler()

    def get_weather(self):
        cords = self.api.geocoding()
        city_weather = self.api.weather_data(cords[0], cords[1])
        print(f"Ort: {city_weather.city_name}")
        print(f"Zeitpunkt: {city_weather.curr_time}")
        print(f"Wetter: {city_weather.description}")
        print(f"Temperatur: {city_weather.curr_temp} °C")
        print(f"Luftfeuchtigkeit: {city_weather.humidity} %")
        print(f"Windgeschwindigkeit: {city_weather.wind_speed} km/h\n")

    def execute(self):
        while True:
            print("Weather check App")
            inpt = input("Press 1 to check the weather of a city or press other key to exit: ")
            if inpt == "1":
                self.get_weather()
            else:
                print("exiting...")
                break 

if __name__ == "__main__":
    WeatherApp().execute()  
    

