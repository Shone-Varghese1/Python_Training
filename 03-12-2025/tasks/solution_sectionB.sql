-- Show all orders, even those without customer info.
select o.order_id,o.order_date,o.customer_id,
c.customer_name from 
orders o 
left join
customers c
on o.customer_id=c.customer_id;

-- Find all orders where customer_id is NULL.
select * from orders where customer_id is NULL;

-- Display orders with customer city (NULL when customer is missing).
select c.city,o.order_id from 
orders o 
left join
customers c
on o.customer_id=c.customer_id;

-- Show all customer names and the number of orders they placed (include zero).
select c.customer_name,count(o.customer_id) as no_of_orders from 
customers c left join orders o on  o.customer_id=c.customer_id
group by c.customer_name;

-- Show customers who have not placed ANY order.
select customer_name from customers where customer_id 
not in 
(select customer_id from orders where customer_id IS NOT NULL);


-- 16. Show all orders and label missing customers as “Guest Checkout”.

SELECT o.order_id,CASE
         WHEN c.customer_name IS NULL THEN 'Guest Checkout'
         ELSE c.customer_name
       END AS customer_name
FROM orders o left join customers c on o.customer_id=c.customer_id;


-- 17. Show orders that have missing product details.
select * from orders where product_id is NULL;


-- 18. Show orders placed by customers from Delhi or missing customer info.
select o.order_id,o.order_date,o.total_amount from 
customers c left join orders o on c.customer_id=o.customer_id 
where c.customer_id is null or c.city="Delhi";
-- 19. Count total orders including ones without customer linkage.
select count(*) as total_orders from orders ;
-- 20. Show the percentage of orders with missing customers.
select count(case when customer_id is null then 1 end) * 100 /count(*) as percentage_of_orders_missing_customers from orders;

