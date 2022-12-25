-- Fill  product table

INSERT INTO product(product_id,name) 
VALUES (1,'Mesa'),(2,'Silla'),(3,'Armario');

-- Fill  country table

INSERT INTO country(country_id,country_name)
VALUES (1,'EEUU'),(2,'España'),(3,'Francia');


-- Fill of city table

INSERT INTO city(city_id,city_name,country_id)
VALUES (1,'New York',1),(2,'Valencia',2),(3,'Paris',3);

-- Fill of city store table

INSERT INTO store(store_id,name,city_id)
VALUES (1,'Tienda1',1),(2,'Tienda2',2),(3,'Tienda3',3);

-- Fill of users table

INSERT INTO users(user_id,name)
VALUES (1,'Juan'),(2,'Luis'),(3,'Maria');

