SELECT
    sub.name,
    sub.bonus
FROM
    (
        SELECT
            e.empId,
            e.name,
            b.bonus
        FROM
            Employee AS e
        LEFT JOIN
            Bonus AS b
        ON
            e.empId = b.empId
    ) AS sub
WHERE
    sub.bonus < 1000 OR sub.bonus IS NULL
