import requests

class APIHandler:
    api_key = "5806995c2e7faa945b0de9add11473fa"
    def __init__(self):
        pass
    def geocoding(self):
        city_name = input("Input city: ")
        country_code = input("Input country code(ISO 3166): ")
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={APIHandler.api_key}")
        r_dict = response.json()
        return (r_dict[0]["lat"], r_dict[0]["lon"])
        #return r_dict

    def weather_data(self, lat, lon):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIHandler.api_key}&lang=de&units=metric") 
        r_dict = response.json()   
        return r_dict

if __name__ == "__main__":
    cords = (APIHandler().geocoding())  
    #print(cords) 
    print(APIHandler().weather_data(cords[0], cords[1])) 

