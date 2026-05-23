import requests


# City coordinates
CITY_COORDINATES = {

    "goa": (15.2993, 74.1240),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "hyderabad": (17.3850, 78.4867),
    "kolkata": (22.5726, 88.3639),
    "jaipur": (26.9124, 75.7873)
}


def get_weather(city):

    try:

        city = city.lower()

        if city not in CITY_COORDINATES:
            return "City not found"

        latitude, longitude = CITY_COORDINATES[city]

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}"
            f"&longitude={longitude}"
            f"&daily=temperature_2m_max"
            f"&timezone=auto"
        )

        response = requests.get(url)

        weather_data = response.json()

        return weather_data

    except Exception as error:

        return f"Error: {str(error)}"