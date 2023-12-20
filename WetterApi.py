import requests

api_key = "5806995c2e7faa945b0de9add11473fa"

def geocoding():
    city_name = input("Input city: ")
    country_code = input("Input country code(ISO 3166): ")
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit=1&appid={api_key}")
    r_dict = response.json()
    return (r_dict[0]["lat"], r_dict[0]["lon"])

if __name__ == "__main__":
    print(geocoding())    

