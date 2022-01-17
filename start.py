import json
import requests
import pprint
import mysql.connector
import pandas as pd 
link = "https://gorest.co.in/public/v1/users"

# 1. Call API
response = requests.get(link)
result = json.loads(response.text)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="python",
  password="python",
  database="python"
)
mycursor = mydb.cursor()


# 2. Get rows from response
for i in range(0, 20):
    row = result['data'][i]
    SQL_COMMAND = "INSERT INTO `users`(`id`,`name`,`email`,`gender`,`status`)VALUES("+str(row['id'])+",'"+row['name']+"','"+row['email']+"','"+row['gender']+"','"+row['status']+"')"
    mycursor.execute(SQL_COMMAND)
    mydb.commit()

print("Completed ")
