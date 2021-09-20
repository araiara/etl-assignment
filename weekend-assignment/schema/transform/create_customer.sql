CREATE TABLE IF NOT EXISTS customer (
  customer_id SERIAL PRIMARY KEY,
  user_name VARCHAR(10) UNIQUE,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  town VARCHAR(255) NOT NULL,
  active CHAR(1) NOT NULL
);
