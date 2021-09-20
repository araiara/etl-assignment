INSERT INTO customer (
    user_name, first_name, last_name, country, town, active
)
SELECT 
  user_name, 
  first_name,
  TRIM(last_name, '_'),
  INITCAP(country),
  town,
  active
FROM raw_customer;
