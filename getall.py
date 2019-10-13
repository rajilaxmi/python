# Fetching all data from the table / select all from table using postgres python
from flask import request
import psycopg2
import json
from flask import Flask

app = Flask(__name__)
@app.route('/api/v1/getall')
def fetching():	
	result={}
	#print(request.args.get('name'))
	try:
	# Fetching the records
		connection = psycopg2.connect(user = 'postgres', password = 'Rahul07!', host = '127.0.0.1', port = '5432', database = 'project1')
		cursor = connection.cursor()
		if request.args.get('name')==None:
			query = 'select * from usersign'
		else:
			query = "select * from usersign where Username ='%s'"%(request.args.get('name'))
			print(query)
		cursor.execute(query)
		print("Selecting rows from usersign table using cursor.fetchall")
		usersign_records = cursor.fetchall()
		
		print('Print each row and its value')
		for i in usersign_records:
			#print("Username: ", i[0])
			#print("Mail ID: ", i[2], "\n")
			result[i[0]]={'Username' : i[0], 'Mail ID' : i[2]}
		return json.dumps(result)	

# Error while fetching data from postgreSQL
	except (Exception, psycopg2.Error) as error:
		print("Error while fetching data from PostgreSQL", error)

# Closing the connection
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed.")
			
		

# main()
if __name__ == '__main__':
	app.run()