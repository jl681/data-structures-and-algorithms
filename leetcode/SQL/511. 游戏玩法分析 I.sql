
/*
1、首先明确选出来的字段和主表
2、因为不同的用户有多个登录日期，所以要分组
    2.1 group by
    2.2 distinct 和MIN一起用的话会导致结果只有一行？
3、第二列为每个组内的最小日期
    3.1 MIN
    3.2 如果是distinct 需要窗口函数

*/

SELECT player_id, MIN(event_date) AS first_login FROM Activity 
GROUP BY player_id;

SELECT DISTINCT player_id, MIN(event_date) OVER(PARTION BY player_id) AS first_login 
FROM Activity;
