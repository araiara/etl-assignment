CREATE TABLE IF NOT EXISTS dim_product (
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(500) NOT NULL,   
  product_description VARCHAR(500) NOT NULL,
  price FLOAT NOT NULL,
  mrp FLOAT NOT NULL,
  pieces_per_case INT NOT NULL,
  weight_per_case FLOAT NOT NULL,
  uom CHAR(2) NOT NULL,
  brand VARCHAR(255) NOT NULL,
  category_id INT NOT NULL,
  tax_pc FLOAT NOT NULL,
  discount_pc FLOAT NOT NULL,
  active CHAR(1) NOT NULL,
  created_by VARCHAR(10) NULL,
  created_date DATE NOT NULL,
  updated_by VARCHAR(10) NOT NULL,
  updated_date DATE NOT NULL,
  CONSTRAINT fk_dim_product_category_id
  FOREIGN KEY (category_id)
    REFERENCES dim_category(category_id)
);
