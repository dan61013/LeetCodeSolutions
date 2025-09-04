SELECT
    w2.id
FROM
    Weather AS w1
JOIN
    Weather AS w2
ON
    w1.recordDate = date_sub(w2.recordDate, INTERVAL 1 DAY)
WHERE
    w2.temperature > w1.temperature