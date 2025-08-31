# Write your MySQL query statement below
SELECT
    p.product_name,
    SUM(unit) AS unit
FROM
    Products AS p
LEFT JOIN
    (
        SELECT
            *
        FROM
            Orders
        WHERE
            order_date BETWEEN '2020-02-01' AND '2020-02-29'
    ) AS o
ON
    p.product_id = o.product_id
GROUP BY
    p.product_id
HAVING
    SUM(o.unit) >= 100