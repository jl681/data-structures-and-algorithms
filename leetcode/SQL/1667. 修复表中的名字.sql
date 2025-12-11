/*
本题的核心在于如何处理字符串
将第一个字母大写，用UPPER函数
如何找到第一个字母？LEFT函数
*/

SELECT user_id,
CONCAT(UPPER(LEFT(name,1),LOWER(RIGHT(name,LENGTH(name) -1))) AS name 
FROM Users;