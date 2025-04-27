import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')
# ... (CREATE TABLE pet and person_pet)

# Insert data
cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", [(1, 'James', 'Smith', 41), ...])
# ... (INSERT INTO pet and person_pet)

conn.commit()
conn.close()

print("Data loaded into pets.db")
