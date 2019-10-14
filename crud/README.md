This is a simple flask application for CRUD operations on db table.

Usage instructions:
* pip3 install -r requirements.txt
* load the db dump in postgres db
* Adding a user(create a row in the table):
	* POST call : http://localhost:5000/api/v1/adduser
		* FORM params : 
			* name 
			* pass1
			* email
* Deleting a user
	* POST call : http://localhost:5000/api/v1/delete
		* FORM params:
			* name
			* value 

* Updating a user :
	* POST call http://localhost:5000/api/v1/updatecall
		* FORM params:
			* column1 (this is the column name which has to be updated)
			* rowv1 (value of the row value which has to be updated)
			* column2 (condition )
			* rowv2 (value of the condition)

* See all users(display)
	* GET call : http://localhost:5000/
		* Optional Query String params for searching a row(additional filter):
			* name

