CREATE OR REPLACE MODEL
`farm-dashboard-502817.farm_sample_dataset.revenue_backtest_model`

OPTIONS(
    MODEL_TYPE='ARIMA_PLUS',
    TIME_SERIES_TIMESTAMP_COL='month_date',
    TIME_SERIES_DATA_COL='revenue',
    AUTO_ARIMA=TRUE
)

AS

SELECT *
FROM `farm-dashboard-502817.farm_sample_dataset.vw_revenue_training`;