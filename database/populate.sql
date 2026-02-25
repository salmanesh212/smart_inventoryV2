-- Sample data for the Smart Inventory System
-- Run this after schema.sql

USE business_management;

-- Products
INSERT INTO products (name, category, price, quantity_in_stock) VALUES
('Laptop Pro 15',        'Electronics',  1299.99, 25),
('Wireless Mouse',       'Electronics',   29.99,  150),
('Office Chair',         'Furniture',     349.99, 40),
('Standing Desk',        'Furniture',     599.99, 15),
('USB-C Hub',            'Electronics',   49.99,  200),
('Mechanical Keyboard',  'Electronics',   89.99,  75),
('Monitor 27"',          'Electronics',   399.99, 30),
('Desk Lamp',            'Furniture',      24.99, 100),
('Webcam HD',            'Electronics',   59.99,  60),
('Notebook Pack (3)',     'Stationery',     9.99, 300);

-- Customers
INSERT INTO customers (name, email) VALUES
('Alice Martin',   'alice.martin@email.com'),
('Bob Johnson',    'bob.johnson@email.com'),
('Carol Williams', 'carol.williams@email.com'),
('David Brown',    'david.brown@email.com'),
('Eve Davis',      'eve.davis@email.com');

-- Orders
INSERT INTO orders (customer_id, order_date) VALUES
(1, '2025-01-15'),
(2, '2025-01-20'),
(1, '2025-02-05'),
(3, '2025-02-14'),
(4, '2025-03-01'),
(5, '2025-03-10'),
(2, '2025-03-22'),
(1, '2025-04-02');

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(2, 6, 1),
(3, 5, 3),
(3, 7, 1),
(4, 4, 1),
(4, 8, 2),
(5, 9, 1),
(5, 10, 5),
(6, 1, 1),
(6, 6, 2),
(7, 2, 4),
(7, 3, 1),
(8, 7, 1),
(8, 5, 2);
