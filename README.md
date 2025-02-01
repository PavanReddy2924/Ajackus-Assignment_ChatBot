# Chat Assistant for SQLite Database

## Objective

A Python-based chat assistant that interacts with an SQLite database to answer user queries using natural language processing (NLP) and SQL queries.

## Supported Queries and Responses

1. **User Query:** Show all employees
   - **Bot Response:** 
     ```
     [(1, 'Alice', 'Sales', 50000, '2021-01-15'), 
      (2, 'Bob', 'Engineering', 70000, '2020-06-10'), 
      (3, 'Charlie', 'Marketing', 60000, '2022-03-20')]
     ```

2. **User Query:** Show employees in Sales
   - **Bot Response:** 
     ```
     [(1, 'Alice', 'Sales', 50000, '2021-01-15')]
     ```

3. **User Query:** Find the highest salary
   - **Bot Response:** 
     ```
     ('Bob', 70000)
     ```

## Setup Instructions

1. Clone the repository: git clone https://github.com/PavanReddy2924/Ajackus-Assignment_ChatBot.git 

2. Install dependencies: pip install -r requirements.txt

3. Run the application: python app.py

4. Access the assistant at `http://127.0.0.1:5000/`.




