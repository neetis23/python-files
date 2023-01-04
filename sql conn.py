# pip install mysql-connector
import mysql.connector
#Open database connectivity
mydb = mysql.connector.connect(host="localhost", user='root', password="harshiv10", database="office")
# cursor method to create a cursor object
mycursor = mydb.cursor()

mycursor.execute("select * from employee")

result = mycursor.fetchall()
 
for i in result:
    print(i)
 
mydb.close()
