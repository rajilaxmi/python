# to delete a record from table

from flask import request
import psycopg2
import json
from flask import Flask

app = Flask(__name__)
@app.route('/api/v1/delete/', methods = ['GET', 'POST'])	

def delete():
	result={}
	try:
		connection = psycopg2.connect(user = "postgres", password = 'Rahul07!', host = "127.0.0.1", port = "5432", database="project1")
		cursor = connection.cursor()
		
		print("PostgreSQL connection has started")
		
		if request.method == 'GET':
			result['Failure'] = 'Please use POST call'
			return json.dumps(result)
		if request.method == 'POST':
			print("Elif executed.")
			print(request.form)
			#print("delete from usersign where %s = '%s'"%(col, row))
			col = request.form['name']
			print(request.form)
			row = request.form['value']
		

			print("delete from usersign where %s = '%s'"%(col, row))

			query = "delete from usersign where %s = '%s'"%(col, row)
			print("delete from usersign where %s = '%s'"%(col, row))
			cursor.execute(query)
			print("Query executed")
			connection.commit()
			count = cursor.rowcount
			print(count, "Record deleted successfully from the table.")
		
			query2 = "select * from usersign"
			cursor.execute(query2)
		
			print("Selecting rows from usersign table using cursor.fetchall")
			usersign_records = cursor.fetchall()
		
			print("Print each row and values")
			for i in usersign_records:
				result[i[0]] = {'Username': i[0], 'Mail': i[2]}
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
			print("PostgreSQL connection is closed")

#main
if __name__=='__main__':
	app.run()
		
			
			