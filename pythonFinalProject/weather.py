from dotenv import load_dotenv
import requests
from pprint import pprint
import os

load_dotenv()

def get_current_weather(city):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data



if __name__ == "__main__":
    print('\n*** Get Current Weather Condition ***\n')


    city = input("\nPlease Enter a city name: ")

    waether_data = get_current_weather(city)

    print("\n")
    pprint(waether_data)
