SELECT

    c.month,

    EXTRACT(YEAR FROM s.date) AS year,

    c.season,

    s.category,

    s.date,

    SUM(s.units_sold) AS units_sold,

    SUM(s.revenue) AS revenue

FROM

    `farm-dashboard-502817.farm_sample_dataset.fact_sales` s

JOIN

    `farm-dashboard-502817.farm_sample_dataset.dim_calendar` c

ON

    DATE(s.date) = DATE(c.date)

GROUP BY

    c.month,
    year,
    c.season,
    s.category,
    s.date

ORDER BY

    year,
    c.month,
    revenue DESC;