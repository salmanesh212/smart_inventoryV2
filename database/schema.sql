-- Database is done by BoyWonder

DROP DATABASE IF EXISTS business_management;
CREATE DATABASE business_management;
USE business_management;

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10,2) DEFAULT 0.00,
    quantity_in_stock INT
);

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE OrderItem (
    orderitem_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE `Order` (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    orderitem_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (orderitem_id) REFERENCES OrderItem(orderitem_id)
);