from flask import request
import psycopg2
import json
from flask import Flask
import traceback

app = Flask(__name__)

DB_USERNAME ="postgres"
DB_PASSWORD ="1234"
DB_HOST = "127.0.0.1" 
DB_PORT = "5432"
DB_DATABASE ="test"

def make_db_connection():
	connection = psycopg2.connect(user = DB_USERNAME, password = DB_PASSWORD, host = DB_HOST, port = DB_PORT, database= DB_DATABASE)
	return connection

# To insert a row into the table
@app.route('/api/v1/adduser/', methods = ['GET', 'POST'])

def adduser():
	result={}
	try:
		connection = make_db_connection()
		cursor = connection.cursor()
		
		print("PostgreSQL connection has started")
		
		if request.method == 'GET':
			result['Failure'] = 'Please use POST call'
			return json.dumps(result)
		print("executing elif")	
		if request.method == 'POST':
			print("Elif executed.")
			if 'name' in request.form and 'pass1' in request.form and 'email' in request.form:
				uname = request.form['name']
				pwd = request.form['pass1']
				mail = request.form['email']
			elif 'name' in request.args and 'pass1' in request.args and 'email' in request.args:
				uname = request.args.get('name')
				pwd = request.args.get('pass1')
				mail = request.args.get('email')
			else:
				raise Exception("No args")		

			
			query = "insert into Sign (Username, Password, Mail) values ('%s', '%s', '%s')"%(uname,pwd,mail)
			cursor.execute(query)
			print("Query executed")
			connection.commit()
			count = cursor.rowcount
			print(count, "Record inserted successfully into table.")
		
			query2 = "select * from Sign"
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

# Error while fetching data from postgreSQL		
	except (Exception, psycopg2.Error) as error:
		if(connection):
			result[str(error)] = traceback.format_exc()
			print("Failed to delete record into the table %s %s"%( str(error),traceback.format_exc()))
			return json.dumps(result)

# Closing the connection	
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

# To update the table
@app.route('/api/v1/updatecall/', methods = ['GET', 'POST'])

def update():
	connection = None
	result={}
	try:
		connection = make_db_connection()
		cursor = connection.cursor()
		
		print("PostgreSQL connection has started")
		
		print(request.method)
		if request.method == 'POST':
			result['Failure'] = 'Please use POST call'
			return json.dumps(result)
		if request.method == 'GET':
			if 'column1' in request.form and 'rowv1' in request.form and 'column2' in request.form and 'rowv2' in request.form:
				col1 = request.form['column1']
				row1 = request.form['rowv1']
				col2 = request.form['column2']
				row2 = request.form['rowv2']

			elif 'column1' in request.args and 'rowv1' in request.args and 'column2' in request.args and 'rowv2' in request.args:
				col1 = request.args.get('column1')
				row1 = request.args.get('rowv1')
				col2 = request.args.get('column2')
				row2 = request.args.get('rowv2')
			else:
				raise Exception("No args")		
			
			query = "update Sign set %s = '%s' where %s = '%s'"%(col1, row1, col2, row2)
			cursor.execute(query)
			print("Query executed")
			connection.commit()
			count = cursor.rowcount
			print(count, "Record inserted successfully into table.")
		
			query2 = "select * from Sign"
			cursor.execute(query2)
		
			print("Selecting rows from Sign table using cursor.fetchall")
			usersign_records = cursor.fetchall()
		
			print("Print each row and values")
			for i in usersign_records:
				result[i[0]] = {'Username': i[0], 'Password': i[1], 'Mail': i[2]}
			return json.dumps(result)
		else:
			result['Call'] = 'Please use POST call only'
			return json.dumps(result)

# Error while fetching data from postgreSQL		
	except (Exception, psycopg2.Error) as error:
		if(connection):
			result[str(error)] = traceback.format_exc()
			print("Failed to delete record into the table %s %s"%( str(error),traceback.format_exc()))
			return json.dumps(result)

# Closing the connection
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


# To delete a row from the table
@app.route('/api/v1/delete/', methods = ['GET', 'POST'])	

def delete():
	result={}
	connection=None
	try:

		connection = make_db_connection()
		cursor = connection.cursor()
		
		print("PostgreSQL connection has started")
		
		if request.method == 'POST':
			result['Failure'] = 'Please use POST call'
			return json.dumps(result)
		if request.method == 'GET':
			if 'name' in request.form and 'value' in request.form:
				col = request.form['name']
				row = request.form['value']
			elif 'name' in request.args and 'value' in request.args:
				col = request.args.get('name')
				row = request.args.get('value')
			else:
				raise Exception("No args")		
			
			
			query = "delete from Sign where %s = '%s'"%(col, row)
			cursor.execute(query)
			print("Query executed")
			connection.commit()
			count = cursor.rowcount
			print(count, "Record deleted successfully from the table.")
		
			query2 = "select * from Sign"
			cursor.execute(query2)
		
			print("Selecting rows from Sign table using cursor.fetchall")
			usersign_records = cursor.fetchall()
		
			print("Print each row and values")
			for i in usersign_records:
				result[i[0]] = {'Username': i[0], 'Mail': i[2]}
			return json.dumps(result)
		else:
			result['Call'] = 'Please use POST call only'
			return json.dumps(result)

# Error while fetching data from postgreSQL		
	except (Exception, psycopg2.Error) as error:
		if(connection):
			result[str(error)] = traceback.format_exc()
			print("Failed to delete record into the table %s %s"%( str(error),traceback.format_exc()))
				return json.dumps(result)

# Closing the connection
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

#show all users
@app.route('/api/v1/getall')
def fetching():
	connection=None	
	result={}

	try:
	# Fetching the records
		connection = make_db_connection()
		cursor = connection.cursor()
		if request.args.get('name')==None:
			query = 'select * from Sign'
		else:
			query = "select * from Sign where Username ='%s'"%(request.args.get('name'))
		
		cursor.execute(query)
		print("Selecting rows from Sign table using cursor.fetchall")
		usersign_records = cursor.fetchall()
		
		print('Print each row and its value')
		for i in usersign_records:
			result[i[0]]={'Username' : i[0], 'Mail ID' : i[2]}
		return json.dumps(result)	

# Error while fetching data from postgreSQL
	except (Exception, psycopg2.Error) as error:
		if(connection):
			result[str(error)] = traceback.format_exc()
			print("Failed to delete record into the table %s %s"%( str(error),traceback.format_exc()))
			return json.dumps(result)

# Closing the connection
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed.")
			


#main
if __name__=='__main__':
	app.run()
		
