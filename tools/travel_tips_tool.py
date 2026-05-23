def get_travel_tips(city):

    tips = {

        "mumbai": {
            "best_time": "November to February",
            "food": "Vada Pav, Pav Bhaji, Bombay Sandwich",
            "safety": "Avoid isolated areas late at night",
            "transport": "Use Mumbai Metro and Local Trains"
        },

        "goa": {
            "best_time": "October to March",
            "food": "Goan Fish Curry, Bebinca",
            "safety": "Avoid secluded beaches at night",
            "transport": "Rent scooters for easy travel"
        },

        "delhi": {
            "best_time": "October to March",
            "food": "Chole Bhature, Parathas",
            "safety": "Use trusted cabs at night",
            "transport": "Delhi Metro is best"
        }
    }

    city = city.lower()

    if city in tips:
        return tips[city]

    return {
        "best_time": "Information not available",
        "food": "Information not available",
        "safety": "Follow standard precautions",
        "transport": "Use local transport"
    }