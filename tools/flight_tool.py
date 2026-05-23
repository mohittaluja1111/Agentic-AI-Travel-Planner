import json


def search_flights(source, destination):

    try:

        with open("data/flights.json", "r") as file:
            flights = json.load(file)

        matching_flights = []

        for flight in flights:

            if (
                flight["from"].lower() == source.lower()
                and flight["to"].lower() == destination.lower()
            ):

                matching_flights.append(flight)

        if not matching_flights:
            return "No flights found"

        cheapest_flight = min(
            matching_flights,
            key=lambda x: x["price"]
        )

        return cheapest_flight

    except Exception as error:

        return f"Error: {str(error)}"