import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    # Get person info
    cursor.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()

    if not person:
        print("Person not found.")
        conn.close()
        return

    first_name, last_name, age = person
    print(f"{first_name} {last_name}, {age} years old")

    # Get pet info
    cursor.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    ''', (person_id,))
    pets = cursor.fetchall()

    for name, breed, age, dead in pets:
        status = "that was" if dead else "that is"
        print(f"{first_name} {last_name} owned {name}, a {breed}, {status} {age} years old")

    conn.close()

# Interactive loop
while True:
    try:
        person_id = int(input("Enter person ID (-1 to exit): "))
        if person_id == -1:
            break
        get_person_and_pets(person_id)
    except ValueError:
        print("Please enter a valid integer.")
