SELECT u.id, u.username, p.id, p.name, c.id, c.name, p.price, s.price, s.quantity, p.quantity, s.updated_at
FROM users u
JOIN sales s
ON u.id = s.user_id
JOIN products p
ON p.id = s.product_id
JOIN categories c
ON c.id = p.category_id;