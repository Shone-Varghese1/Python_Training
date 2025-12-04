-- List all orders with customer names and email.
select c.customer_name,c.email,o.order_id,o.order_date,
o.total_amount,o.product_id from customers c 
inner join
orders o
on c.customer_id=o.customer_id;


-- Show product name, category, price for every ordered product.
select product_name,category,price from products 
where product_id in (select distinct product_id from orders);

-- List all orders with customer name and product name.

select o.order_id,o.order_date,o.customer_id,o.total_amount,
c.customer_name,p.product_name from orders  o
inner join products p on o.product_id=p.product_id 
inner join customers c on o.customer_id=c.customer_id;

-- Show customer name and total_amount for all valid customer orders.

select c.customer_name,o.total_amount from customers c
inner join
orders o 
on o.customer_id=c.customer_id;

 -- List all Electronics products that have been ordered.
 select p.product_name from products as p inner join 
 orders o 
 on o.product_id=p.product_id where p.category="Electronics";

-- 6. Find customers who ordered Fashion products.
select c.customer_name from customers c 
inner join orders o on
o.customer_id=c.customer_id
inner join products p on
p.product_id=o.product_id
where p.category="Fashion";

-- Show all orders above 1000 with customer and product details.
select o.order_id,o.order_date,c.customer_name,
p.product_name from customers c 
inner join orders o on
o.customer_id=c.customer_id
inner join products p on
p.product_id=o.product_id
where o.total_amount>1000;


-- Show customers from Mumbai who placed at least one order.
select customer_name from customers 
where customer_id in (select customer_id from orders) 
and city= "Mumbai";


-- Show number of orders per customer (using INNER JOIN + GROUP BY).
select count(*) as no_of_orders,c.customer_name from customers c inner join 
orders o on o.customer_id=c.customer_id
 group by c.customer_name;
 
 -- List all customers and the total amount they have spent.
 select c.customer_name ,sum(o.total_amount) as amount_spent from customers c inner join 
orders o on o.customer_id=c.customer_id
 group by c.customer_name
