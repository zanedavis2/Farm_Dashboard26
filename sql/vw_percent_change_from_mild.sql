WITH weather_avg AS (

    SELECT
        category,
        weather_condition,
        AVG(revenue) AS avg_revenue
    FROM `farm-dashboard-502817.farm_sample_dataset.vw_weather_impact`
    GROUP BY
        category,
        weather_condition

),

mild AS (

    SELECT
        category,
        avg_revenue AS mild_avg
    FROM weather_avg
    WHERE weather_condition = 'Mild'

)

SELECT

    w.category,
    w.weather_condition,

    ROUND(w.avg_revenue, 2) AS avg_revenue,

    ROUND(
        SAFE_DIVIDE(
            w.avg_revenue - m.mild_avg,
            m.mild_avg
        ) * 100,
        1
    ) AS pct_change_vs_mild

FROM weather_avg w

JOIN mild m
ON w.category = m.category

ORDER BY
    w.category,
    w.avg_revenue DESC;