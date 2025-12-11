-- 编写一个 SQL 删除语句来 删除 所有重复的电子邮件，只保留一个id最小的唯一电子邮件。
-- 以 任意顺序 返回结果表。 （注意： 仅需要写删除语句，将自动对剩余结果进行查询）


--DELECT语句中涉及多个表时要指定删除的是哪个表

DELETE p1 FROM Person p1
LEFT JOIN Person p2 ON p1.email = p2.email AND p1.id > p2.id;

DELETE p1 FROM Person p1, Person p2 WHERE p1.email = p2.email AND p1.id > p2.id;