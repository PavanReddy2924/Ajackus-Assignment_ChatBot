import sqlite3

# Connect to SQLite database
def create_database():
    connection = sqlite3.connect(r'C:\Users\pavan\Desktop\Ajackus-Assignment\company.db')
    cursor = connection.cursor()

    # Create the tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Department TEXT,
                        Salary INTEGER,
                        Hire_Date TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Manager TEXT
                    )''')

    # Insert records into employees table
    employees_data = [
        (1, 'Alice', 'Sales', 50000, '2021-01-15'),
        (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
        (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
    ]
    cursor.executemany('''INSERT INTO employees (ID, Name, Department, Salary, Hire_Date)
                          VALUES (?, ?, ?, ?, ?)''', employees_data)

    # Display all records in the employees table
    print("The inserted records are:")
    data = cursor.execute('''SELECT * FROM employees''')
    for row in data:
        print(row)

    # Commit changes to the database and close connection
    connection.commit()
    connection.close()

# Call the function to create the database
create_database()
