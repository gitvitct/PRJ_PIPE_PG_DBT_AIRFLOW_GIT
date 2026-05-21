SELECT
    order_id,
    customer_id,
    amount,
    purchase_date::date AS purchase_day
FROM raw_sales