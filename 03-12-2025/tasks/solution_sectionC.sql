-- 21. Show all products and the orders associated with them (NULL for unused products).
select p.product_name,o.order_id from products p right join orders o on p.product_id=o.product_id ;
-- 22. List products that have never been ordered.
select product_name from products where product_id not in (select product_id from orders where product_id is not null)
-- 23. Show Electronics products and the number of times they were ordered.
-- 25. List all products with their total sales, including those with zero sales.
-- 26. For each category, show number of ordered products (include zero).
-- 27. Show products that were ordered by customers from Bangalore.
-- 28. Show products missing from order table (never sold).
-- 29. Show the count of orders grouped by product name (including zero).
-- 30. Show products that appeared in at least one NULL customer order.