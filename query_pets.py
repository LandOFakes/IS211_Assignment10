import sqlite3

    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        person_id = int(input("Enter person ID (-1 to quit): "))
        if person_id == -1:
            break

        cursor.execute("SELECT ... FROM person WHERE id = ?", (person_id,))
        # ... (Fetch person data and print)

        cursor.execute("SELECT ... FROM pet JOIN person_pet ... WHERE person_id = ?", (person_id,))
        # ... (Fetch pets data and print)

    conn.close()
