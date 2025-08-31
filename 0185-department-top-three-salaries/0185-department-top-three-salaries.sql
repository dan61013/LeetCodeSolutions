# Write your MySQL query statement below
SELECT
    d.name AS Department,
    e1.name AS Employee,
    e1.salary AS Salary
FROM
    Employee AS e1
LEFT JOIN
    Department AS d
ON
    e1.departmentId = d.id
-- 將每一row資料與不重複的salaries清單進行比較
-- 只將0, 1, 2(取3)的資料保
WHERE 3 >
    (
        SELECT
            -- DISTINCT -> drop duplicate
            COUNT(DISTINCT e2.salary)
        FROM
            Employee AS e2
        WHERE
            e2.salary > e1.salary AND
            -- 在同一個department進行比較
            e1.departmentId = e2.departmentId 
    )