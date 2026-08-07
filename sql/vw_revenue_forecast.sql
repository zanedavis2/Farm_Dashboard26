SELECT
    forecast_timestamp,
    forecast_value,
    prediction_interval_lower_bound,
    prediction_interval_upper_bound

FROM
ML.FORECAST(

MODEL
`farm-dashboard-502817.farm_sample_dataset.revenue_forecast_model`,

STRUCT(
6 AS horizon,
0.90 AS confidence_level
)

)