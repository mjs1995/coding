# https://leetcode.com/problems/delete-duplicate-emails/
DELETE p1 
From Person p1, Person p2
where
    p1.Email = p2.Email and p1.ID > p2.ID
