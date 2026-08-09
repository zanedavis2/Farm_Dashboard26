import pandas as pd
from datetime import date

from generator.generate_calendar import generate_calendar
from generator.generate_weather import generate_weather
from generator.generate_sales import generate_sales

from bigquery.upload import upload_dataframe
from bigquery.upload import date_exists


import config

# Configuration #

START_DATE = config.START_DATE
END_DATE = config.END_DATE


# Load Product Data #

products = pd.read_csv(config.PRODUCTS)
behavior = pd.read_csv(config.BEHAVIOR)


# Generate Calendar #

calendar = generate_calendar(
    date.today(),
    date.today()
)


# Generate weather

weather = generate_weather(
    calendar
)


# ----------------------------
# Generate sales
# ----------------------------

sales = generate_sales(
    calendar,
    weather,
    products,
    behavior
)


# ----------------------------
# Preview
# ----------------------------

print(sales.head())

print(
    f"Generated {len(sales)} sales rows"
)


# Avoid Duplicates

today = date.today()

if date_exists("fact_sales", "date", today):
    print("Today's sales already exist. Exiting.")
    quit()


# Upload to GBQ #


upload_dataframe(
    calendar,
    "dim_calendar"
)

upload_dataframe(
    weather,
    "dim_weather"
)

upload_dataframe(
    sales,
    "fact_sales"
)


print("Pipeline complete")
