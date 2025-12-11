/*
1、因为是求两个连续空余的座位，所以我的想法是用左连接
2、类似于 [c1.seat_id, c1.free, c2.seat_id, c2.free][1，1，2，1] 
3、但是用‘ON c1.seat_id = c2.seat_id - 1’的条件会导致：
    最后一个seat_id的后两列为null，所以增加了‘OR c2.free is null’这个条件
    还会导致如果只有一个座位，也会被选出来
4、所以第一种做法的问题在于左连接的ON条件
*/ 
SELECT c1.seat_id
FROM Cinema c1
LEFT JOIN Cinema c2 ON c1.seat_id = c2.seat_id - 1
WHERE (c1.free != 0 AND c2.free != 0) OR c2.free is null；

-- 这种左连接的方式使得不会出现null，同时也解决了只有一列的问题
SELECT DISTINCT c1.seat_id
FROM Cinema c1
LEFT JOIN Cinema c2 ON ABS(c1.seat_id - c2.seat_id) = 1
WHERE c1.free = 1 AND c2.free =1
ORDER BY c1.seat_id;

--如果要求求出三个连续座位？
SELECT DISTINCT c1.seat_id
FROM Cinema c1
LEFT JOIN Cinema c2 ON ABS(c1.seat_id - c2.seat_id) = 1
LEFT JOIN Cinema c3 ON ABS(c1.seat_id - c3.seat_id) = 2
WHERE c1.free = 1 AND c2.free =1 AND c3.free = 1
ORDER BY c1.seat_id;