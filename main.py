import pandas as pd

from generator.generate_calendar import generate_calendar
from generator.generate_weather import generate_weather
from generator.generate_sales import generate_sales

from bigquery.upload import upload_dataframe

import config

# ----------------------------
# Configuration
# ----------------------------

START_DATE = config.START_DATE
END_DATE = config.END_DATE


# ----------------------------
# Load Product Data
# ----------------------------

products = pd.read_csv(config.PRODUCTS)
behavior = pd.read_csv(config.BEHAVIOR)

# ----------------------------
# Generate calendar
# ----------------------------

calendar = generate_calendar(
    START_DATE,
    END_DATE
)


# ----------------------------
# Generate weather
# ----------------------------

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


# ----------------------------
# Upload to BigQuery
# ----------------------------

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
