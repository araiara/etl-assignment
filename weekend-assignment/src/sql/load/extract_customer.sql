INSERT INTO dim_customer
SELECT
customer_id, user_name, first_name, last_name, l.location_id, active
FROM customer c
JOIN dim_location l
ON c.country = l.country
AND c.town = l.town;
