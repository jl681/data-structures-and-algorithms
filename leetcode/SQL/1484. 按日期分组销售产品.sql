/*
1、明确需要选出的列和表
2、需要处理的是第三列，如果把该日期下的所有产品用逗号连接起来
3、GROUP_CONCAT函数用来处理，处理的就是group by的一个组，第二个是顺序，第三是seperator
4、注意处理顺序和distinct
*/

SELECT sell_date, COUNT(DISTINCT product) AS num_sold , 
GROUP_CONCAT(DISTINCT product, ORDER BY product, seperator ',')  AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;