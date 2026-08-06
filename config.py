from datetime import date
import os

PROJECT_ID = "farm-dashboard-502817"

DATASET_ID = "farm_sample_dataset"

##CREDENTIALS_PATH = "credentials/farm-dashboard-502817-4baf1e1a6668.json"

CREDENTIALS_PATH = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS",
    "credentials.json"
)

SALES_TABLE = "sales"


PRODUCTS = "data/products.csv"
BEHAVIOR = "data/product_behavior.csv"

START_DATE = "2024-01-01"
END_DATE = date.today()
