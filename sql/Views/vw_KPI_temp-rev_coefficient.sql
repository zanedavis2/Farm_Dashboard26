SELECT
    category,
    ROUND(CORR(temperature, revenue), 3) AS corr
FROM `farm-dashboard-502817.farm_sample_dataset.vw_weather_impact`
GROUP BY category;