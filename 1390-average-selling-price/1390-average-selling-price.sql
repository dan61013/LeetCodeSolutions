SELECT
    p.product_id,
    IFNULL(
        ROUND(
            SUM(p.price * us.units) / CAST(SUM(us.units) AS float)
            , 2)
        , 0) AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS us
ON
    p.product_id = us.product_id
WHERE
    us.purchase_date BETWEEN p.start_date AND p.end_date OR
    us.product_id IS NULL
GROUP BY
    p.product_id