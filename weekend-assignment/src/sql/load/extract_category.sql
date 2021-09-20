INSERT INTO dim_category (category)
SELECT DISTINCT p.category 
FROM product p;
