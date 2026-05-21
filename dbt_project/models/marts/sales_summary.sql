SELECT
    purchase_day,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_sales,
    AVG(amount) AS average_ticket
FROM {{ ref('stg_sales') }}
GROUP BY purchase_day