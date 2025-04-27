import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    person_id = int(input("Enter person ID (-1 to quit): "))
    if person_id == -1:
        break
        
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person_data = cursor.fetchone()

    if person_data:
        first_name, last_name, age = person_data
        print(f"{first_name} {last_name}, {age} years old")

        cursor.execute('''
            SELECT p.name, p.breed, p.age
            FROM pet p
            JOIN person_pet pp ON p.id = pp.pet_id
            WHERE pp.person_id = ?
        ''', (person_id,))
        pets_data = cursor.fetchall()

        if pets_data:
            print("Pets:")
            for name, breed, age in pets_data:
                print(f"  {name}, a {breed}, that was {age} years old")
        else:
            print(f"{first_name} {last_name} has no pets.")
    else:
        print(f"Person with ID {person_id} not found.")

conn.close()
