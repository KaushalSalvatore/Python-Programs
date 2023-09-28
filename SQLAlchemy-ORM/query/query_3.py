import sqlite3

sqliteConnection = sqlite3.connect('person.db')
cursor = sqliteConnection.cursor()
print('DB Init')
# Write a query and execute it with cursor
query = 'SELECT * from people'
cursori = cursor.execute(query)
 
# Fetch and output result
result = cursori.fetchall()
print('SQLite Version is {}'.format(result))

for row in cursori:
    print(row)

# Close the cursor
cursor.close()





