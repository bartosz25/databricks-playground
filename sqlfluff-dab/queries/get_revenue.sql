    SELECT
        store_id
        ,count(order_id) total_orders
        ,SUM(revenue) AS total_revenue
    FROM {orders_table}
    GROUP BY 1