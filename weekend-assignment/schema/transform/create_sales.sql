CREATE TABLE IF NOT EXISTS sales (
  sales_id SERIAL PRIMARY KEY,
  bill_id INT NOT NULL,
  product_id INT NOT NULL,
  qty INT NOT NULL,
  gross_price FLOAT NOT NULL,
  tax_amt FLOAT NOT NULL,
  discount_amt FLOAT NOT NULL,
  net_bill_amt FLOAT NOT NULL,
  CONSTRAINT fk_sales_bill_id
  FOREIGN KEY (bill_id)
    REFERENCES bill(bill_id)
    ON DELETE CASCADE,
  CONSTRAINT fk_sales_product_id
  FOREIGN KEY (product_id)
    REFERENCES product(product_id)
    ON DELETE CASCADE
);
