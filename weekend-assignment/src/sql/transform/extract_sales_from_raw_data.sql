INSERT INTO sales (
    bill_id, product_id, qty, gross_price, tax_amt, discount_amt, net_bill_amt
)
SELECT
b.bill_id,
p.product_id,
CAST (qty AS INT),
CAST (gross_price AS FLOAT),
CAST (tax_amt AS FLOAT),
CAST (discount_amt AS FLOAT),
CAST (net_bill_amt AS FLOAT)
FROM raw_sales r_w
JOIN bill b
ON CAST(r_w.bill_no AS INT) = b.bill_no
JOIN product p
ON CAST(r_w.product_id AS INT) = p.product_id;
