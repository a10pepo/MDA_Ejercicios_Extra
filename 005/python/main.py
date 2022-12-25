import pymysql
import time
from faker import Faker



#CONEXION A MYSQL

import pymysql.cursors

while True:
    try:
        connection = pymysql.connect( host="db",
                                    user= "root" , 
                                    passwd="my_secret_password", 
                                    db="db",
                                    port=3306,
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        break

    except:
        print('Waiting for database to intialize')
        time.sleep(1)

print("DB connected")

fake = Faker()

def insert_product_data(sql,x,y):
     return cursor.execute(sql, (x, y))

with connection:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `product` (`product_id`, `name`) VALUES (%s, %s)"
        insert_product_data(sql,1,"mesa")
        insert_product_data(sql,2,"Armario")
        insert_product_data(sql,3,"Silla")
    connection.commit()



