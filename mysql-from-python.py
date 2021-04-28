import os
import pymysql

username = os.getenv('GITPOD_USER')

connection = pymysql.connect(host='localhost',
                            user =username,
                            password ='',
                            db ='Chinook')
                            
        
try:
    with connection.cursor() as cursor:
        sql = "SELECT * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
