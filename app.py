from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Function to create the database
def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

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

    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        employees_data = [
            (1, 'Alice', 'Sales', 50000, '2021-01-15'),
            (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
            (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
        ]
        cursor.executemany('''INSERT INTO employees (ID, Name, Department, Salary, Hire_Date)
                              VALUES (?, ?, ?, ?, ?)''', employees_data)

    conn.commit()
    conn.close()

# Convert natural language to SQL query
def parse_query(user_query):
    user_query = user_query.lower()

    if "employees" in user_query and "sales" in user_query:
        return "SELECT * FROM employees WHERE Department = 'Sales';"
    elif "employees" in user_query and "engineering" in user_query:
        return "SELECT * FROM employees WHERE Department = 'Engineering';"
    elif "employees" in user_query:
        return "SELECT * FROM employees;"
    elif "departments" in user_query:
        return "SELECT * FROM departments;"
    elif "highest salary" in user_query:
        return "SELECT Name, Salary FROM employees ORDER BY Salary DESC LIMIT 1;"
    else:
        return None

# Execute SQL Query
def execute_query(sql_query):
    if not sql_query:
        return "I'm sorry, I didn't understand your query."

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "No results found."

        return rows

    except sqlite3.Error as e:
        conn.close()
        return f"An error occurred: {str(e)}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    sql_query = parse_query(user_message)
    result = execute_query(sql_query)
    
    return jsonify({"response": str(result)})

if __name__ == "__main__":
    # Create the database if not exists
    create_database()

    # Run the app on Render's dynamic port (environment variable PORT)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
