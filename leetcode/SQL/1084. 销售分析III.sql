/*
1、明确返回的数据和来自的表格
2、product表格里面的product在Sales表格有销售日期
3、Sales中的所有销售日期都必须落在2019-01-01 - 2019-03-31之间
    3.1 筛选出Sales表格中product_id不在这两个日期之间的
*/

SELECT product_id, product_name FROM Product
WHERE product_id not in(
SELECT sale_date FROM Sales WHERE datediff(sale_date,'2019-01-01') < 0 OR datediff(sale_date,'2019-03-31') > 0
);

SELECT p.product_id, p.product_name FROM Product p
RIGHT JOIN Sales s ON p.product_id = s.product_id
WHERE p.product_id not in (
    SELECT sale_date FROM Sales WHERE datediff(sale_date,'2019-01-01') < 0 OR datediff(sale_date,'2019-03-31') > 0
)