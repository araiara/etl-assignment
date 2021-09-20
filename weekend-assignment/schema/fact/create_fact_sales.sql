CREATE TABLE IF NOT EXISTS fact_sales (
  sales_id SERIAL PRIMARY KEY,
  bill_id INT NOT NULL,
  product_id INT NOT NULL,
  qty INT NOT NULL,
  gross_price FLOAT NOT NULL,
  tax_amt FLOAT NOT NULL,
  discount_amt FLOAT NOT NULL,
  net_bill_amt FLOAT NOT NULL,
  CONSTRAINT fk_fact_sales_bill_id
  FOREIGN KEY (bill_id)
    REFERENCES dim_bill(bill_id)
    ON DELETE CASCADE,
  CONSTRAINT fk_fact_sales_product_id
  FOREIGN KEY (product_id)
    REFERENCES dim_product(product_id)
    ON DELETE CASCADE
);
