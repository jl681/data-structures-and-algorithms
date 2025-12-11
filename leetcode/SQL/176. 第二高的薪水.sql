
--  LIMIT 1 OFFSET 1 等价于 LIMIT 1,1
-- 如果没有第二高的薪水要输出null所以外面还要再包一层select
SELECT (
SELECT DISTINCT salary  ORDER BY salary DESC LIMIT 1 OFFSET 1  FROM Employee) 
AS secondHighestSalary;

select IFNULL((select distinct(Salary) 
from Employee
order by Salary desc
limit 1,1),null) as SecondHighestSalary;

--去除掉最大的以后第二大的
SELECT MAX(salary) AS secondHighestSalary FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

-- 窗口函数？？没有执行成功

select(
    select
        salary
    from (
        select
            distinct(salary),
            dense_rank() over(order by salary desc) rk  -- 注意，这边必须用dense_rank，这样在有重复薪水值的时候可以避免跳过2
        from Employee
    ) a where rk = 2
) as SecondHighestSalary
