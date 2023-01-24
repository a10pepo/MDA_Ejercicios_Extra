import mysql.connector
import os
import time

def insert_data(table_name, data):
    while True:
        try:
            connection = mysql.connector.connect(
                host= "172.24.224.1",
                port=3306,
                user="db_user",
                password="admin",
                database="app_db"
            )

            break

        except:
            print('Waiting for database to intialize')
            time.sleep(1)

            cursor = connection.cursor()

            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            cursor.execute(sql_query, tuple(data.values()))
            connection.commit()
            print("Data inserted successfully into table")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")



'''
-- Creation of store table
CREATE TABLE IF NOT EXISTS store (
  store_id INT NOT NULL,
  name varchar(250) NOT NULL,
  city_id INT NOT NULL,
  PRIMARY KEY (store_id),
  CONSTRAINT fk_city
      FOREIGN KEY(city_id) 
	  REFERENCES city(city_id)
);
'''

store_data = {
    "store_id" : 1467,
    "name" : "Mercadona",
    "city_id" : 2341,
}

insert_data("store", store_data)