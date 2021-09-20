INSERT INTO dim_location (town, country)
SELECT DISTINCT town, country
FROM customer;