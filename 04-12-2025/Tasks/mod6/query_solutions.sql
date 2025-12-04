select c.customer_name from customers c inner join orders o 
on c.customer_id=o.customer_id
group by customer_name having count(*)>2 ;

select product_name from products where product_id not in 
(select product_id from orders where product_id is not null);

select customer_name,sum(total_amount) as total_amount_spend
 from customers c inner join orders o 
 on c.customer_id =o.customer_id 
 group by c.customer_name;
 
 select c.customer_name,o.order_id from customers c
 left join orders o on 
 c.customer_id=o.customer_id;
 
 -- 45. Write SQL: all products and match orders even if no sale occurred (right join).
 select p.product_name,o.order_id from  orders o right join
 products p on o.product_id=p.product_id ;
 
 -- 46. Write SQL: find customers ordering from multiple categories.
 
 select c.customer_name,count(distinct category) from customers c 
 inner join  orders o on o.customer_id=c.customer_id 
 inner join products p on p.product_id=o.product_id
 group by customer_name having count(distinct category)>1;
 
 -- 47. Write SQL: list top 3 highest revenue orders.
 select order_id,total_amount from orders order by
 total_amount desc limit 3;
 
 -- 48. Write SQL: detect missing customer_id or product_id in orders.
 select * from orders where customer_id is null or 
 product_id is null;
 
-- 49. Write SQL: generate a report of (customer × month × total amount).
 select customer_name,date_format (order_date, '%y-%m' ) as month ,sum(total_amount)
 from customers c inner join orders o
 on o.customer_id=c.customer_id group by customer_name, month;
 
 -- 50. Write a SQL query using CROSS JOIN to generate all (customer × product) combinations.
 select customer_name,product_name from 
 customers cross join products order by customer_name asc;