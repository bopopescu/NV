import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "KingOfBeasts",
    database = "ncserver",
)

my_cursor = mydb.cursor()

# sql_register_code = "SELECT registercode FROM register"
# my_cursor.execute(sql_register_code)
#
# code = my_cursor.fetchall()[0][0]
# print(code)
# print(type(code))
# my_cursor.execute('CREATE DATABASE ncserver')

# my_cursor.execute('SHOW DATABASES')
#
# for x in my_cursor:
#     print(x)
# if my_cursor.execute('SHOW DATABASES'):
#     my_cursor.execute("CREATE DATABASE ncserver")
#
# if my_cursor.execute('SHOW TABLES'):
# my_cursor.execute("CREATE TABLE register (ID INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL, registercode VARCHAR(255) NOT NULL)")
#
# print('Hello')
# my_cursor.execute('SHOW TABLES')
# for x in my_cursor:
#     print(x)
# my_cursor.execute('SELECT username FROM user')
# rows = my_cursor.fetchall()
# if rows:
#     print('Hello')
# print(rows)
# sql = "INSERT INTO register (registercode) VALUES ('265915167490')"
# # register = ("265915167490")
# my_cursor.execute(sql)
#
# mydb.commit()
# my_cursor.execute("CREATE TABLE users (userID INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, useradmin VARCHAR(255) NOT NULL)")
