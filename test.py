from tools.budget_tool import estimate_budget

result = estimate_budget(
    flight_price=4500,
    hotel_price_per_night=3000,
    days=3
)

print(result)