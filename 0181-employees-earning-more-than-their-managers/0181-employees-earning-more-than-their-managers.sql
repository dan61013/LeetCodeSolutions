# Write your MySQL query statement below
SELECT
    name AS Employee
FROM
    Employee AS e1
WHERE
    e1.salary > (
        SELECT
            salary
        FROM
            Employee
        WHERE id = e1.managerId
    )