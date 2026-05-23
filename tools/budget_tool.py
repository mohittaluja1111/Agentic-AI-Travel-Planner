def estimate_budget(budget, days):

    daily_budget = budget / days

    if daily_budget >= 5000:

        category = "Luxury"

    elif daily_budget >= 2500:

        category = "Mid-Range"

    else:

        category = "Budget Friendly"

    return {
        "total_budget": budget,
        "daily_budget": round(daily_budget, 2),
        "category": category
    }