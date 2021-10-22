CREATE DATABASE IF NOT EXISTS edge_computers;
USE edge_computers;

-- Create Manager Table
CREATE TABLE IF NOT EXISTS manager(
	manager_id INT PRIMARY KEY AUTO_INCREMENT,
    manager_fname VARCHAR(255),
    manager_lname VARCHAR(255),
    store_name VARCHAR(255)
);

-- Create Vendor Table
CREATE TABLE IF NOT EXISTS vendor(
	vend_code INT PRIMARY KEY AUTO_INCREMENT,
    vend_addr VARCHAR(255),
    vend_name VARCHAR(255)
);

-- Create Customer Table
CREATE TABLE IF NOT EXISTS customer(
	cust_id INT PRIMARY KEY AUTO_INCREMENT,
    cust_fname VARCHAR(255),
    cust_lname VARCHAR(255),
    cust_email VARCHAR(255),
    cust_street VARCHAR(255),
    cust_city VARCHAR(255),
    cust_province VARCHAR(255),
    cust_postal_code VARCHAR(255),
    cust_country VARCHAR(255),
    cust_phone VARCHAR(255)
);

-- Create Product Table
CREATE TABLE IF NOT EXISTS product (
	prod_code INT AUTO_INCREMENT,
    vend_code INT,
    prod_name VARCHAR(255),
    price DECIMAL,
    PRIMARY KEY (prod_code),
    FOREIGN KEY (vend_code) REFERENCES vendor (vend_code)
);

-- Create Inventory Table
CREATE TABLE IF NOT EXISTS inventory(
	prod_code INT,
	prod_name VARCHAR(255),
    stock_quant INT,
    PRIMARY KEY (prod_code),
    FOREIGN KEY (prod_code) REFERENCES product (prod_code)
);

-- Create Invoice Table
CREATE TABLE IF NOT EXISTS invoice (
	inv_num INT AUTO_INCREMENT,
    manager_id INT NOT NULL,
    cust_id INT,
    time_of_sale TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (inv_num),
    FOREIGN KEY (manager_id) REFERENCES manager (manager_id),
    FOREIGN KEY (cust_id) REFERENCES customer (cust_id)
);

-- Create Invoice Line
CREATE TABLE IF NOT EXISTS invoice_line (
	line_num INT PRIMARY KEY AUTO_INCREMENT,
	prod_code INT,
    inv_num INT,
    quant_purchased INT NOT NULL,
    FOREIGN KEY (prod_code) REFERENCES product (prod_code),
    FOREIGN KEY (inv_num) REFERENCES invoice (inv_num)
);


insert into customer(cust_fname, cust_lname, cust_email, cust_street, cust_city, cust_province, cust_postal_code, cust_country, cust_phone) values('Florence', 'Tat', 'flo@flo.com', '123 Some Street', 'St. John''s', 'NL', 'A1B 2C3', 'Canada', '7091234567');
insert into customer(cust_fname, cust_lname, cust_email, cust_street, cust_city, cust_province, cust_postal_code, cust_country, cust_phone) values('Jack', 'Husk', 'jack@jack.com', '123 Other Street', 'St. John''s', 'NL', 'A1D 2E3', 'Canada', '7091357911');
insert into customer(cust_fname, cust_lname, cust_email, cust_street, cust_city, cust_province, cust_postal_code, cust_country, cust_phone) values('Zainab', 'Mehdee', 'zainab@zainab.com', '123 Any Street', 'Corner Brook', 'NL', 'A2B 3C4', 'Canada', '7092468101');
insert into manager(manager_fname, manager_lname, store_name) values('Chinonso', 'Mogo', 'Edge Computers');
insert into vendor(vend_addr, vend_name) values('246 That Street', 'ASUS');
insert into product(vend_code, prod_name, price) values(1, 'Z590 Motherboard', 200);
insert into inventory(prod_code, prod_name, stock_quant) values(1, 'Z590 Motherboard', 10);
insert into invoice(manager_id, cust_id) values(1, 1);
insert into invoice_line(prod_code, inv_num, quant_purchased) values(1, 1, 1);








