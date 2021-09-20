CREATE TABLE IF NOT EXISTS dim_customer (
  customer_id SERIAL PRIMARY KEY,
  user_name VARCHAR(10) UNIQUE,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  location_id INT NOT NULL,
  active CHAR(1) NOT NULL,
  CONSTRAINT fk_dim_customer_location_id
    FOREIGN KEY (location_id)
    REFERENCES dim_location(location_id)
);
