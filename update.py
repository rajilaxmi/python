# To update the values 

from flask import Flask
import psycopg2
import json
from flask import request

app = Flask(__name__)
@app.route('/api/v1/update/', methods = ['GET', 'POST'])

def update():
	result={}
	try:
		connection = psycopg2.connect(user = "postgres", password = 'Rahul07!', host = '127.0.01', port = '5432', database = 'project1')
		cursor = connection.cursor()
		print("PostgreSQL connection is successful.")
		
		if request.method == 'GET':
			result['Failure'] = "Please use POST call"
			return json.dumps(result)
		
		if request.method == 'POST':
			col1 = request.form(column1)
			row1 = request.form(rowv1)
			col2 = request.form(column2)
			row2 = request.form(rowv2)
			
			query = "update usersign set '%s' = '%s' where '%s' = '%s'"%(col1, row1, col2, row2)
			cursor.execute(query)
			connection.commit()
			count = cursor.rowcount
			print(count, "Record updated successfully.")
			
			query1= "select * from usersign"
			cursor.execute(query1)
			print("Selecting rows from usersign using cursor.fetchall()")
			usersign_records = cursor.fetchall()
			for i in usersign_records:
				result[i[0]]={ 'Username': i[0], 'Password': i[1], 'Email': i[2] }
			return json.dumps(result)
		
		else:
			result['Call'] = 'Please use POST call only'
			return json.dumps(result)
			
	except (Exception, psycopg2.Error) as error:
		if(connection):
			print("Failed to insert record into the table", error)
			
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed.")
		
# main
if __name__=='__main__':
	app.run()
	
	
			
