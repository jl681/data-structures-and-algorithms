# Write your MySQL query statement below

SELECT c.customer_id
        ,c.customer_name
FROM Customers c
LEFT JOIN Orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING SUM(product_name = 'A') > 0
        AND
        SUM(product_name = 'B') > 0
        AND
        SUM(product_name = 'C') = 0
ORDER BY customer_id;