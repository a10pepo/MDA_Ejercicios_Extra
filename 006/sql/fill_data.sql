-- Insert data into product table
INSERT INTO product (product_id, name) VALUES (1, 'Shoes');
INSERT INTO product (product_id, name) VALUES (2, 'Sweaters');

-- Insert data into country table
INSERT INTO country (country_id, country_name) VALUES (1, 'Spain');
INSERT INTO country (country_id, country_name) VALUES (2, 'Portugal');

-- Insert data into city table
INSERT INTO city (city_id, city_name, country_id) VALUES (1, 'Valencia', 1);
INSERT INTO city (city_id, city_name, country_id) VALUES (4, 'Lisbon', 2);

-- Insert data into store table
INSERT INTO store (store_id, name, city_id) VALUES (1, 'Nude Project', 1);
INSERT INTO store (store_id, name, city_id) VALUES (2, 'Carhartt', 1);

-- Insert data into users table
INSERT INTO users (user_id, name) VALUES (1, 'Dario Fernandez');
INSERT INTO users (user_id, name) VALUES (2, 'Ruben Garcia');

-- Insert data into status_name table
INSERT INTO status_name (status_name_id, status_name) VALUES (1, 'Pending');
INSERT INTO status_name (status_name_id, status_name) VALUES (2, 'Shipped');

-- Insert data into sale table
INSERT INTO sale (sale_id, amount, date_sale, product_id, user_id, store_id) VALUES ('sale1', 583.00, '16-01-2023 12:44:00', 2, 1, 1);
INSERT INTO sale (sale_id, amount, date_sale, product_id, user_id, store_id) VALUES ('sale2', 777.00, '16-01-2023 12:44:00', 1, 2, 1);

-- Insert data into order_status table
INSERT INTO order_status (order_status_id, update_at, sale_id, status_name_id) VALUES ('order1', '16-01-2023 12:44:00', 'sale1', 2);
INSERT INTO order_status (order_status_id, update_at, sale_id, status_name_id) VALUES ('order2', '16-01-2023 12:44:00', 'sale2', 2);