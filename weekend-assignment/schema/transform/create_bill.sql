CREATE TABLE IF NOT EXISTS bill (
  bill_id SERIAL PRIMARY KEY,
  bill_no INT NOT NULL,
  bill_date TIMESTAMP NOT NULL,
  bill_location VARCHAR(255) NOT NULL,
  customer_id INT NOT NULL,
  created_by VARCHAR(255) NOT NULL,
  updated_by VARCHAR(255) NOT NULL,
  created_date DATE NOT NULL,  
  updated_date DATE NOT NULL,
  CONSTRAINT fk_bill_customer_id
  FOREIGN KEY (customer_id)
    REFERENCES customer(customer_id)
);
