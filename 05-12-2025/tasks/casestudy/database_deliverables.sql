CREATE DATABASE subscription_app;
USE subscription_app;
CREATE TABLE subscriptions (
sub_id INT PRIMARY KEY,
customer_name VARCHAR(50),
start_date DATE,
expiry_date DATE,
created_at DATETIME,
plan_type VARCHAR(20) -- Monthly, Quarterly, Yearly
);
INSERT INTO subscriptions VALUES
(1, 'Aisha Khan', '2025-12-05', '2026-01-05', '2024-12-15 10:30:00', 'Monthly'),
(2, 'Rahul Sharma', '2025-12-04', '2026-01-04', '2025-01-05 09:45:00', 'Monthly'),
(3, 'Imran Ali', '2025-12-03', '2026-01-04', '2025-02-10 14:12:00', 'Monthly'),
(4, 'Meera Iyer', '2025-12-02', '2026-01-02', '2025-03-01 17:05:00', 'Monthly'),
(5, 'Sanjay Patel', '2025-12-03', '2026-04-03', '2025-02-20 13:00:00', 'Quarterly');
INSERT INTO subscriptions VALUES
(6, 'Shone Varghese', '2025-11-04', '2025-12-04', '2024-12-15 10:30:00', 'Monthly'),
(7, 'David Philip', '2025-11-07', '2025-12-07', '2024-12-15 10:30:00', 'Monthly');

INSERT INTO subscriptions VALUES
(8, 'Derick mark', '2025-08-15', '2025-12-15', '2024-12-15 10:30:00', 'Quarterly'),
(9, 'Matt Henry', '2024-12-17', '2025-12-17', '2023-12-15 10:30:00', 'Yearly');
select * from subscriptions;



# 1. Write SQL to fetch all subscriptions expiring within 10 days.
select *
from subscriptions
where expiry_date <= CURDATE() + INTERVAL 10 DAY;


# 2. Write SQL to find customers who subscribed in the current month.
select customer_name from subscriptions where MONTH(start_date) = MONTH(CURDATE()) AND YEAR(start_date) = YEAR(CURDATE());


# 3. Fetch all yearly plans and sort by expiry_date.
select * from subscriptions where plan_type="yearly";


# 4. Identify all subscriptions lasting more than 30 days (Quarterly/Yearly).
select * from subscriptions where plan_type in ('yearly', 'Quarterly');


# 5. Write SQL to check data quality: expiry_date < start_date.
select count(*) from subscriptions where expiry_date < start_date;




