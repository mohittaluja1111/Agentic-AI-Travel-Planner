import json


def get_places(city):

    try:

        with open("data/places.json", "r") as file:

            places = json.load(file)

        city_places = []

        for place in places:

            if place["city"].lower() == city.lower():

                city_places.append(place)

        if not city_places:

            return []

        sorted_places = sorted(
            city_places,
            key=lambda x: x["rating"],
            reverse=True
        )

        return sorted_places[:5]

    except Exception as error:

        print(error)

        return []