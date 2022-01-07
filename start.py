import json
import requests
import pprint
import mysql.connector


print('hello world')

# load API result into a variable
    # https://gorest.co.in/public/v1/users  -> Sample API


# r = requests.get("https://gorest.co.in/public/v1/users") 

# # print(r.json())
# pprint.pprint(r.json())


# Parse JSON API result 

# SQL_COMMAND = "INSERT INTO Person(PersonID,LastName,FirstName,Address,City) VALUES (2,'p','mahesh','karavadi','ongole')"
SQL_COMMAND = "select * from Person"
# Connect to database



# Run INSERT SQL into a table and insert API RESULT
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="python",
  password="python",
  database="python"
)

mycursor = mydb.cursor()

mycursor.execute(SQL_COMMAND)
# mydb.commit()
myresult = mycursor.fetchall()

for x in myresult:
  print(x)