select e.left_operand, e.operator, e.right_operand,
       case when 
       e.operator = '<' then if(l.value < r.value, 'true', 'false')
       when e.operator = '>' then if(l.value > r.value, 'true', 'false')
       else if(l.value = r.value, 'true', 'false') end
       as value
from Expressions e
join Variables l on e.left_operand = l.name
join Variables r on e.right_operand = r.name
;
