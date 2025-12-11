/*
本题的核心是列转行
用UNION 或者是UNOION ALL
UNION包括去重，性能较低
而本例不需要去重
*/

SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 is not null
UNION  ALL
SELECT product_id, 'store2' AS store, store2 AS price FROM Products WHERE store2 is not null
UNION ALL
SELECT product_id, 'store3' AS store, store2 AS price FROM Products WHERE store3 is not null
;