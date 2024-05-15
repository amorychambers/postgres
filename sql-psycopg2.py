import psycopg2

# Connect to 'chinook' database
connection = psycopg2.connect(database="chinook", user="postgres", password="Lucyisl0st")

# Build a cursor object of the database
cursor = connection.cursor()

# First query; select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

#Second query; select only the "name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

#Third query; select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#Fourth query; select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')

#Fifth query; select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 51')

#Sixth query; select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
