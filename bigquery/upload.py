from google.cloud import bigquery
from google.oauth2 import service_account
import config


def get_bigquery_client():
    credentials = service_account.Credentials.from_service_account_file(
        config.CREDENTIALS_PATH
    )

    client = bigquery.Client(
        credentials=credentials,
        project=config.PROJECT_ID
    )

    return client


def upload_dataframe(df, table_name):

    client = get_bigquery_client()

    table_id = (
        f"{config.PROJECT_ID}."
        f"{config.DATASET_ID}."
        f"{table_name}"
    )

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    print(f"Uploaded {len(df)} rows to {table_name}")


def date_exists(table_name, date_column, check_date):

    client = get_bigquery_client()

    query = f"""
    SELECT COUNT(*) AS cnt
    FROM `{config.PROJECT_ID}.{config.DATASET_ID}.{table_name}`
    WHERE {date_column} = @check_date
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(
                "check_date",
                "DATE",
                check_date
            )
        ]
    )

    results = client.query(query, job_config=job_config).result()

    count = list(results)[0].cnt

    return count > 0
