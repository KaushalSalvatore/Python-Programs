import sqlite3
path = '/E:/PythonPrograms/SQLAlchemy-ORM/db-file/Car_Database.db'
sqliteConnection = sqlite3.connect(path)
cursor = sqliteConnection.cursor()
# Write a query and execute it with cursor
query = 'SELECT * from Customers'

cursori = cursor.execute(query)
 
# Fetch and output result
result = cursori.fetchall()
print('SQLite Version is {}'.format(result))


for row in cursori:
    if(row.gender == 'Male'):
        print(row)


# filter_result = session.query(Person).filter(Person.gender=='M')
# for record in filter_result:
#     print(record.firstname,"--",record.lastname)


# Close the cursor
cursor.close()