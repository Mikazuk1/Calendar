import mysql.connector

# python
# from calendar_app import app, db
# app.app_context().push()
# db.create_all()

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd = "lolislife23",
    auth_plugin='mysql_native_password'
    )

my_cursor = mydb.cursor()

#my_cursor.execute("Create DATABASE calendar_db")
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)