SELECT

    DATE(s.date) AS sale_date,

    c.weekday,
    c.month,
    c.season,
    c.is_weekend,

    w.temperature,
    w.rainfall,
    w.weather_condition,

    s.category,

    SUM(s.units_sold) AS units_sold,

    SUM(s.revenue) AS revenue,

FROM
    `farm-dashboard-502817.farm_sample_dataset.fact_sales` s

JOIN
    `farm-dashboard-502817.farm_sample_dataset.dim_weather` w
ON
    DATE(s.date) = DATE(w.date)

JOIN
    `farm-dashboard-502817.farm_sample_dataset.dim_calendar` c
ON
    DATE(s.date) = DATE(c.date)

GROUP BY

    sale_date,

    c.weekday,
    c.month,
    c.season,
    c.is_weekend,

    w.temperature,
    w.rainfall,
    w.weather_condition,

    s.category

ORDER BY
    sale_date,
    revenue DESC