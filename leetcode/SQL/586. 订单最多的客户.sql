-- 订单最多的客户number
/*
1、首先明确要选出来的列和从哪个表选择
2、订单最多，就是GROUP BY customer_number， 然后count每个分组下面的行
3、关键是要找到订单最多，那就是count最多，所以要排序并且是倒序的第一个
*/

SELECT customer_number FROM Orders 
GROUP BY customer_number 
ORDER BY COUNT(order_number) Desc LIMIT 1;

--进一步扩展，如果订单最多的客户不止一个？
/*
1、还是要拿到最高的count，所以上述子句够用
2、拿到count等于最高的count的所有customer_number
*/

SELECT customer_number FROM Orders HAVING COUNT(*) = 
(SELECT COUNT(order_number) AS cnt  FROM Orders 
GROUP BY customer_number 
ORDER BY cnt Desc LIMIT 1);