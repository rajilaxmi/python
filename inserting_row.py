# To insert a row 

import psycopg2
import json
from flask import Flask

app = Flask(__name__)
@app.route('/api/v1/adduser')

def inserting():
	result={}
	try:
		connection = psycopg2.connect(user = "postgres", password = 'Rahul07!', host = "127.0.0.1", port = "5432", database="project1")
		cursor = connection.cursor()
		
		query = "insert into usersign (Username, Password, Mail) values (%s, %s, %s)"
		row = ('Penny', 'NA', 'penny.na@bbt.com')
		cursor.execute(query, row)
		
		connection.commit()
		count = cursor.rowcount
		print(count, "Record inserted successfully into table.")
		
		query2 = "select * from usersign"
		cursor.execute(query2)
		
		print("Selecting rows from usersign table using cursor.fetchall")
		usersign_records = cursor.fetchall()
		
		print("Print each row and values")
		for i in usersign_records:
			result[i[0]] = {'Username': i[0], 'Mail': i[2]}
		return json.dumps(result)
		
	except (Exception, psycopg2.Error) as error:
		if(connection):
			print("Failed to insert record into the table")
	
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

#main
if __name__=='__main__':
	app.run()