create database retail_app;
use retail_app;

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
email VARCHAR(80),
city VARCHAR(50)
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT NULL,
total_amount DECIMAL(10,2),
product_id INT NULL
);

CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1, 'Aisha Khan', 'aisha@xyz.com', 'Mumbai'),
(2, 'Rahul Sharma', 'rahul@xyz.com', 'Delhi'),
(3, 'John Daniel', 'john@xyz.com', 'Bangalore'),
(4, 'Meera Iyer', 'meera@xyz.com', 'Chennai'),
(5, 'Sanjay Patel', 'sanjay@xyz.com', 'Hyderabad');



INSERT INTO products VALUES
(101, 'Laptop HP 15', 'Electronics', 52000),
(102, 'Samsung Phone A54', 'Electronics', 28000),
(103, 'Jeans Blue Fit', 'Fashion', 1500),
(104, 'T-Shirt Classic', 'Fashion', 700),
(105, 'Wireless Mouse', 'Accessories', 900),
(106, 'Rice 5KG Bag', 'Groceries', 320),
(107, 'Olive Oil 1L', 'Groceries', 540),
(108, 'Printer Canon G2012', 'Electronics', 12500);



INSERT INTO orders VALUES
(1001, '2024-01-05', 1, 52000, 101),
(1002, '2024-01-06', 2, 28000, 102),
(1003, '2024-01-07', 3, 1500, 103),
(1004, '2024-01-07', 1, 700, 104),
(1005, '2024-01-08', 2, 900, 105),
(1006, '2024-01-08', NULL, 320, 106), -- customer unknown
(1007, '2024-01-09', 1, 540, NULL), -- product unknown
(1008, '2024-01-10', 3, 12500, 108),
(1009, '2024-01-10', 4, 320, 106),
(1010, '2024-01-11', NULL, 700, 104), -- customer null
(1011, '2024-01-12', 2, 540, 107);



