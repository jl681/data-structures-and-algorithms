
/*
本题的目的在于找到连续存在的数字
*/
--解法一： row_num()窗口函数
SELECT MIN(log_id) AS start_id
        ,MAX(log_id) AS end_id
FROM (
    SELECT log_id
            ,(log_id - ROW_NUMBER() OVER()) AS diff
    FROM Logs) temp
GROUP BY diff;

--解法二：要找到连续的数字，则数字的开始值减一和结束值加1都不在区间内
--先找到所有开始的id，比如1，2，3，7，8，10中，1，7，10减去1都不在表内
--再找到所有的结束id，比如3，8，10
--两个的笛卡尔积
SELECT l1.log_id AS start_id
        ,MIN(l2.log_id) AS end_id
FROM  (
    SELECT log_id
    FROM Logs
    WHERE (log_id - 1) NOT IN (SELECT log_id FROM Logs)
) l1, 
    (SELECT log_id
    FROM Logs
    WHERE (log_id + 1) NOT IN (SELECT log_id FROM Logs)) l2
WHERE l1.log_id <= l2.log_id;