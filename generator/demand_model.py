import numpy as np


def calculate_product_demand(product, day):

    demand = product["avg_daily_units"]


    # Temperature effect

    if product["temperature_sensitivity"] == "high":

        if day["temperature"] > 80:
            demand *= 1.5

        elif day["temperature"] < 50:
            demand *= 0.5


    elif product["temperature_sensitivity"] == "medium":

        if day["temperature"] > 80:
            demand *= 1.35

    elif product["temperature_sensitivity"] == "low":

        if day["temperature"] < 55:
            demand *= 1.35 



    # Rain effect

    if day["rainfall"] > .25:

        if product["rain_sensitivity"] == "high":
            demand *= .3

        elif product["rain_sensitivity"] == "medium":
            demand *= .7


    # Season effect

    if product["preferred_season"] != "All":

        if day["season"] == product["preferred_season"]:

            if product["season_strength"] == "high":
                demand *= 1.5

            elif product["season_strength"] == "medium":
                demand *= 1.25

        else:

            if product["season_strength"] == "high":
                demand *= .5

    

    if day["weekday"] == "Friday":
        demand *= 1.25
    elif day["weekday"]=="Saturday":
        demand *= 1.3
    elif day["weekday"]=="Sunday":
        demand *= 1.2


    
    if day["year"] == "2024":
        demand *= 0.9

    if day["year"] == "2026":
        demand *= 1.1

    if day["year"] == "2027":
        demand *= 1.15
    


    # Random daily variation

    demand *= np.random.normal(
        1,
        .20
    )


    return max(
        0,
        int(demand)
    )
