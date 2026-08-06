import pandas as pd
import numpy as np

from generator.demand_model import (
    calculate_product_demand
)


def generate_sales(
    calendar,
    weather,
    products,
    behavior
):

    sales = []


    # combine calendar and weather
    daily_conditions = calendar.merge(
        weather,
        on="date"
    )


    product_data = products.merge(
        behavior,
        on="product_id"
    )


    for _, day in daily_conditions.iterrows():

        for _, product in product_data.iterrows():


            units = calculate_product_demand(
                product,
                day
            )


            sales.append(
                {
                    "date": day["date"],
                    "product_id": product["product_id"],
                    "product_name": product["product_name"],
                    "category": product["category"],
                    "units_sold": units,
                    "price": product["price"],
                    "revenue": units * product["price"]
                }
            )


    return pd.DataFrame(sales)
