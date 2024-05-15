import psycopg2

# Connect to 'chinook' database
connection = psycopg2.connect(database="chinook", user="postgres", password="Lucyisl0st")

# Build a cursor object of the database
cursor = connection.cursor()

# First query; select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

#Second query; select only the "name" column from the "Artist" table
cursor.execute('SELECT "Name" FROM "Artist"')

# Fetch the results (multiple)
results = cursor.fetchall()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
