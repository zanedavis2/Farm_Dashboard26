import random
from datetime import date

import pandas as pd


products = pd.read_csv("data/products.csv")

def generate_daily_sales():
  rows = []
  today = date.today()
  for _, product in products.iterrows():
    quantity = random.randint(
            int(product["min_daily_units"]),
            int(product["max_daily_units"])
        )
    
    revenue = round(quantity * product["price"], 2)
    
    rows.append({
            "sale_date": today,
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "category": product["category"],
            "quantity": quantity,
            "price": product["price"],
            "revenue": revenue
        })
  sales_df = pd.DataFrame(rows)

  return sales_df

