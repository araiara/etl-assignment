INSERT INTO dim_product
SELECT 
  product_id,
  product_name,   
  product_description,
  price,
  mrp,
  pieces_per_case,
  weight_per_case,
  uom,
  brand,
  c.category_id,
  tax_pc,
  discount_pc,
  active,
  created_by,
  created_date,
  updated_by,
  updated_date
FROM product p
JOIN dim_category c
ON p.category = c.category;
