from generator.generate_sales import generate_daily_sales
from bigquery.upload import upload_dataframe
from bigquery.upload import get_bigquery_client


client = get_bigquery_client()

print("Connected to BigQuery!")
print(client.project)

sales = generate_daily_sales()

print(sales)

upload_dataframe(
    sales,
    "sales"
)
