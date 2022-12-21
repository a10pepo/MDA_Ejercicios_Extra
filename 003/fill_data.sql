-- Fill  product table

INSERT INTO product(product_id,name) 
VALUES (1,'Silla'),(2,'Armario'),(3,'Mesa');

-- Fill  country table

INSERT INTO country(country_id,country_name)
VALUES (1,'UK'),(2,'España'),(3,'PORTUGAL');

-- Fill of city table

INSERT INTO city(city_id,city_name,country_id)
VALUES (1,'LONDON',1),(2,'OLIVA',2),(3,'LISBOA',3);

-- Fill of city store table

INSERT INTO store(store_id,name,city_id)
VALUES (1,'T1',1),(2,'T2',2),(3,'T3',3);

-- Fill of users table

INSERT INTO users(user_id,name)
VALUES (1,'CARLOS'),(2,'PEDRO'),(3,'JORGE');

-- Fill of status_name table

INSERT INTO status_name(status_name_id,status_name)
VALUES (1,'END'),(2,'WORKING'),(3,'REPAIR');

-- Fill of sale table

INSERT INTO sale(sale_id,amount,date_sale,product_id,user_id,store_id)
VALUES (1,5,'01/01/1000 00:00:00',1,1,1),(2,6,'01/05/1000 08:00:30',2,2,2),(3,7,'01/08/1000 00:04:00',3,3,3);


-- Fill of order_status table

INSERT INTO order_status(order_status_id,update_at,sale_id,status_name_id)
VALUES (1,'01/01/1000 00:00:30',1,1),(2,'01/05/1000 08:00:30',2,2),(3,'01/08/1000 00:04:00',3,3);



