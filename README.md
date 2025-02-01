Chat Assistant for SQLite Database
Objective
A Python-based chat assistant that interacts with an SQLite database to answer user queries using natural language processing (NLP) and SQL queries.

Supported Queries and Responses
User Query: "Show all employees"

Bot Response:
bash
Copy
Edit
[(1, 'Alice', 'Sales', 50000, '2021-01-15'), 
 (2, 'Bob', 'Engineering', 70000, '2020-06-10'), 
 (3, 'Charlie', 'Marketing', 60000, '2022-03-20')]
User Query: "Show employees in Sales"

Bot Response:
css
Copy
Edit
[(1, 'Alice', 'Sales', 50000, '2021-01-15')]
User Query: "Find the highest salary"

Bot Response:
bash
Copy
Edit
('Bob', 70000)
Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/PavanReddy2924/Ajackus-Assignment_ChatBot.git
Install dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Run the application:

nginx
Copy
Edit
python app.py
Access the assistant at http://127.0.0.1:5000/
