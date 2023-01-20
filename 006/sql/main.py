from faker import Faker
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='mysql_user', password='admin', host='3306', database='mysql')
cursor = cnx.cursor()

# Create a Faker object
fake = Faker()

# Insert data into the product table
for i in range(10):
    product_id = fake.random_int(min=1, max=1000, step=1)
    product_name = fake.product_name_product()
    cursor.execute("INSERT INTO product (product_id, product_name) VALUES (%s, %s)", (product_id, product_name))

# Insert data into the country table
for i in range(10):
    country_id = fake.random_int(min=1, max=1000, step=1)
    country_name = fake.country()
    cursor.execute("INSERT INTO country (country_id, country_name) VALUES (%s, %s)", (country_id, country_name))

# Insert data into the city table
for i in range(10):
    country_id = fake.random_int(min=1, max=1000, step=1)
    city_id = fake.random_int(min=1, max=1000, step=1)
    city_name = fake.city()
    cursor.execute("INSERT INTO country (city_id, city_name, country_id) VALUES (%s, %s, %s)", (city_id, city_name, country_id))

# Insert data into the store table
for i in range(10):
    store_id = fake.random_int(min=1, max=1000, step=1)
    city_id = fake.random_int(min=1, max=1000, step=1)
    store_name = fake.company()
    cursor.execute("INSERT INTO country (store_id, city_id, store_name) VALUES (%s, %s, %s)", (store_id, city_id, store_name))

# Insert data into the user table
for i in range(10):
    user_id = fake.random_int(min=1, max=1000, step=1)
    user_name = fake.name()
    cursor.execute("INSERT INTO country (user_id, user_name) VALUES (%s, %s)", (user_id, user_name))

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
