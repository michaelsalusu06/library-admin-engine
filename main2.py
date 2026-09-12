import sqlite3

conn = sqlite3.connect("library_engine.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT,
    city TEXT,
    age INTEGER
);

CREATE TABLE IF NOT EXISTS borrowings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    book_title TEXT,
    fee REAL,
    days_borrowed INTEGER
);
""")

cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    cursor.executescript("""
    INSERT INTO students (firstname, lastname, city, age) VALUES
    ('Alex', 'Rivers', 'London', 22),
    ('Sarah', 'Chen', 'Paris', 26),
    ('Jordan', 'Taylor', 'London', 17),
    ('Elena', 'Rostova', 'New York', 68),
    ('Marcus', 'Vance', 'Paris', 20);

    INSERT INTO borrowings (student_id, book_title, fee, days_borrowed) VALUES
    (1, 'Introduction to Python', 2.50, 5),
    (1, 'Data Science Essentials', 5.00, 10),
    (2, 'Introduction to Python', 2.50, 3),
    (3, 'SQL Query Mastery', 4.00, 7),
    (4, 'Classic Literature Vol 1', 0.00, 2);
    """)
    conn.commit()

option = -1
history = []

while option != 0:
    print("\n--- CAMPUS LIBRARY SYSTEM ---")
    print("1. Search for students")
    print("2. Access tier classifier")
    print("3. Borrowing and fee revenue report")
    print("4. Search history")
    print("0. Exit")

    option = int(input("Input options(0-4): "))
    
    if option == 1:
        search = input("Student name: ")
        history.append(search)

        search_param = f"%{search}%"
        cursor.execute(
            """
            SELECT firstname, lastname, age, (firstname || '.' || lastname || '@library.com') AS email
            FROM students
            WHERE firstname LIKE ? OR lastname LIKE ?
        """,
            (search_param, search_param),
        )

        results = cursor.fetchall()
        print("\n--- Search Results ---")
        if results:
            for row in results:
                print(
                    f"Name: {row[0]} {row[1]} | Age: {row[2]} | Email: {row[3]}"
                )
        else:
            print("No matching students found.")

    elif option == 2:
        cursor.execute("""
            SELECT firstname, lastname, age,
            CASE
                WHEN age >= 65 THEN 'Senior Scholar Pass: Priority room booking & extended loan limits'
                WHEN age >= 25 AND age <= 64 THEN 'Graduate & Research Pass: Full database access & specialized collections'
                WHEN age >= 18 AND age <= 24 THEN 'Undergraduate Pass: Standard catalog borrowing privileges'
                ELSE 'Junior Pass: General catalog access'
            END AS access_tier
            FROM students;
        """)

        results = cursor.fetchall()
        print("\n--- Student Access Tiers ---")
        for row in results:
            print(f"{row[0]} {row[1]} (Age {row[2]}): {row[3]}")

    elif option == 3:
        print("\n--- Borrowing and Fee Revenue Report ---")
        cursor.execute("""
            SELECT students.firstname, students.lastname, SUM(borrowings.fee) AS total_fee
            FROM students
            LEFT JOIN borrowings ON students.id = borrowings.student_id
            GROUP BY students.id;
        """)

        results = cursor.fetchall()
        for row in results:
            fee = row[2] if row[2] is not None else 0.0
            print(f"Student: {row[0]} {row[1]} | Total Fees: ${fee:.2f}")

    elif option == 4:
        print("\n--- Search History ---")
        if not history:
            print("No history available.")
        else:
            historylen = len(history) - 1
            while historylen >= 0:
                print(f"- {history[historylen]}")
                historylen = historylen - 1

    elif option == 0:
        print("Have a good day")

    else:
        print("Option invalid")

conn.close()