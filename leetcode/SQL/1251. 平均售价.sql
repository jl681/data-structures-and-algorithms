-- 按照我之前的解法
--如果出现一个日期期间内有多个出售记录会很麻烦
SELECT p.product_id, cast(SUM(p.price * us.units) / SUM(us.units) as decimal(10,2)) AS average_price FROM Prices p
LEFT JOIN UnitsSold us ON us.product_id = p.product_id AND us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id


--优化以后，可以一个产品id，一个日期和一个售卖把所有的选择出来
--再从这个合集里选择
SELECT product_id, ROUND(SUM(sales)/SUM(units), 2) AS average_price FROM (
SELECT p.product_id, p.price * us.units AS sales, us.units FROM Prices p
LEFT JOIN UnitsSold us ON us.product_id = p.product_id 
WHERE us.purchase_date BETWEEN p.start_date AND p.end_date
) T
GROUP BY p.product_id 