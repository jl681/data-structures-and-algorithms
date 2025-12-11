/*
1、从Employees 和Salaries两个表查找employee_id
2、这个id只在这两张表中的任意一张
3、所以不需要的就是这两张表都有的；UNION ALL + COUNT
*/

SELECT employee_id FROM (
    SELECT employee_id FROM Employees
    UNION  ALL 
    SELECT employee_id FROM Salaries
)
GROUP BY employee_id
HAVING COUNT(*) = 1
ORDER BY employee_id;