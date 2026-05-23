import json


def get_hotels(city, budget):

    try:

        with open("data/hotels.json", "r") as file:

            hotels = json.load(file)

        city_hotels = []

        for hotel in hotels:

            if hotel["city"].lower() == city.lower():

                city_hotels.append(hotel)

        if not city_hotels:

            return []

        sorted_hotels = sorted(
            city_hotels,
            key=lambda x: x["price_per_night"]
        )

        return sorted_hotels[:5]

    except Exception as error:

        print(error)

        return []