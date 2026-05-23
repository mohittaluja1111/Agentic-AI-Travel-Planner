from tools.hotel_tool import get_hotels
from tools.places_tool import get_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget
from tools.travel_tips_tool import get_travel_tips


def generate_travel_plan(city, budget, days):

    hotels = get_hotels(city, budget)

    places = get_places(city)

    weather = get_weather(city)

    budget_info = estimate_budget(budget, days)

    travel_tips = get_travel_tips(city)

    flights = [
        {
            "airline": "IndiGo",
            "price": 4800,
            "departure": "14:00"
        },
        {
            "airline": "Air India",
            "price": 5200,
            "departure": "10:30"
        }
    ]

    itinerary = [
        {
            "day": 1,
            "plan": "Visit famous tourist attractions and local markets"
        },
        {
            "day": 2,
            "plan": "Explore historical places and enjoy local food"
        },
        {
            "day": 3,
            "plan": "Shopping, nightlife, and relaxation"
        }
    ]

    result = {
        "city": city,
        "budget": budget,
        "days": days,
        "weather": weather,
        "budget_info": budget_info,
        "hotels": hotels,
        "places": places,
        "travel_tips": travel_tips,
        "flights": flights,
        "itinerary": itinerary
    }

    return result