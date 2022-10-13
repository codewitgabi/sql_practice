import sqlite3


with sqlite3.connect("mysql.db") as conn:
	cursor = conn.cursor()
	
	try:
		cursor.execute("""
			CREATE TABLE person (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name VARCHAR(50) NOT NULL,
			age INT NOT NULL,
			date_of_birth DATE NOT NULL,
			email VARCHAR(150))
			""")
	except sqlite3.OperationalError:
		pass
	
	"""
	DROP statement:
		Delete databases or tables or anything that can be dropped.
	#cursor.execute("DROP TABLE person")
	"""
	
	"""
	INSERT ... INTO statement:
		Adding records to our database tables
	cursor.execute("INSERT INTO person (id, name, age, date_of_birth, email) VALUES (3, 'Josh Jay', 17, '2005-07-28', 'jay@gmail.com')")
	"""
	
	"""
	SELECT ... FROM statement:
		For getting columns or rows from our database table.
		
		syntax:
			SELECT * FROM table: For getting all rows from the table
			SELECT <column> FROM table
			SELECT <column1>, <column2> FROM table
	"""
	
	"""
	ORDER BY statement:
		For sorting records in our table
		
		SELECT * FROM table ORDER BY <column> ASC - default - Ascending order
		SELECT * FROM table ORDER BY <column> DESC - Descending order
	"""
	
	"""
	DISTINCT statement:
		To get unique rows from a table. i.e avoiding repetition from returned data
		
		SELECT DISTINCT <column> FROM table
	"""
	
	"""
	WHERE ... AND statement:
		Selects records from the data when certain conditions are met
		
		syntax:
			SELECT <column> FROM table WHERE <columnx> = y
			SELECT <column> FROM table WHERE <columnx> = y AND <columny> = z
			SELECT <column> FROM table WHERE <columnx> = y AND (<columny> = z OR <columnb> = c)
			
	"""
	
	"""
	Comparison Operations:
		Helps to compare and perform simple arithmetic, logical, bitwise operations.
		<> not equal to
		= equal to
		
		SELECT [operation]
		
		SELECT 2 * 2, SELECT 4 = 3 etc
	"""
	
	"""
	IN statement
	Checks if a condition is met with the values specified in brackets.
	
	syntax:
		SELECT * FROM table WHERE <column> IN (*condition)
	"""
	
	"""
	BETWEEN statement
	This checks if a condition is met for a range of values.
	
	SELECT * FROM table WHERE <column> BETWEEN start AND stop
	"""
	
	"""
	LIKE and iLIKE statement
	For querying data that matches a particular pattern. The wildcards - % or _ are used to match patterns.
	% matches patterns before or after a search e.g %something%
	_ matches a number of characters e.g ___p matches 3 characters and then a p
	
	SELECT * FROM table WHERE column LIKE '%pattern'
	"""

	for i in cursor.execute("SELECT age, COUNT(*) FROM person GROUP BY age ORDER BY COUNT(*) DESC ; "):
		print(i)