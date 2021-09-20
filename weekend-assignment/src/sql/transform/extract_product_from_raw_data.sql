INSERT INTO product (
  product_name, product_description, price, mrp, pieces_per_case, weight_per_case, uom, brand, category, tax_pc, discount_pc, active, created_by, created_date, updated_by, updated_date
)
SELECT 
  product_name,
  product_description,
  CAST (price AS FLOAT),
  CAST (mrp AS FLOAT),
  CAST (pieces_per_case AS INT),
  CAST (weight_per_piece AS FLOAT),
  uom,
  brand,
  CASE WHEN length(category) = 2
    THEN UPPER(category)
  ELSE INITCAP(category)
  END,
  CAST (tax_percent AS FLOAT),
  0,
  active,
  created_by,
  DATE(created_date),
  updated_by,
  DATE(updated_date)
from raw_product;
