CREATE TABLE IF NOT EXISTS dim_location (
  location_id SERIAL PRIMARY KEY,
  town VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL
);
