Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.

 

Example 1:

Input: 
Employees table:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
Output: 
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
Explanation: 
The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
The employee with ID 3 gets 0 bonus because their name starts with 'M'.
The rest of the employees get a 100% bonus.

#my solution
select employee_id, 
        case when employee_id % 2 != 0 then (case when name not like 'M%' then salary else 0 end)  
        else 0 end as bonus 
from Employees order by employee_id; 

--union前后的区别在于根据where条件得到的salary不同，所以这种思路是把salary分开算
SELECT employee_id ,salary AS bonus
FROM Employees
WHERE employee_id%2!=0 AND name NOT LIKE ('M%')
UNION 
SELECT employee_id ,salary*0 AS bonus
FROM Employees
WHERE employee_id%2=0 OR name LIKE ('M%')
ORDER BY employee_id;

--if + mode函数，应该是最先想到的
SELECT employee_id,
IF(MOD(employee_id,2)!=0 AND LEFT(name,1)!='M',salary,0) bonus
FROM Employees;

--和我的解法一样，但是1要注意使用left函数；
--其次是这里没有else，而是放到两个我很里面了，因为两个when是互斥的？
SELECT employee_id,
(CASE WHEN MOD(employee_id,2)!=0 AND LEFT(name,1)!='M' THEN salary
     WHEN MOD(employee_id,2)=0 OR LEFT(name,1)='M' THEN 0
END) bonus
FROM Employees
ORDER BY employee_id;

--正则
SELECT
    employee_id, 
CASE WHEN 
    MOD(employee_id, 2) = 1 AND name not rlike '^M' THEN salary ELSE 0 END AS bonus 
FROM
	Employees 
ORDER BY 
    employee_id;


select
    employee_id,
    if(
        employee_id&1 and name regexp '^[^M]',
        salary,
        0
    ) as bonus
from employees
order by employee_id;


