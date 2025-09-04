SELECT
    eu.unique_id,
    e.name
FROM
    EmployeeUNI AS eu
RIGHT JOIN
    Employees AS e
ON
    eu.id = e.id