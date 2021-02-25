SELECT DISTINCT l1.num AS ConsecutiveNums
FROM logs l1
    INNER JOIN logs l2 ON l1.id+1=l2.id
    INNER JOIN logs l3 on l2.id+1=l3.id
WHERE l1.num = l2.num AND l1.num = l3.num
