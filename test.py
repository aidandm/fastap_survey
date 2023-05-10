import psycopg2
import random

# Replace these variables with your own PostgreSQL database credentials
db_name = "your_db_name"
db_user = "your_db_user"
db_password = "your_db_password"
db_host = "your_db_host"
db_port = "your_db_port"

# Connect to the database
connection = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
cursor = connection.cursor()

# Define the number of users, questions, and answers to generate
num_users = 10
num_questions = 5
num_answers = 50

# Generate normalized data for the Answers table
for _ in range(num_answers):
    user_id = random.randint(1, num_users)
    question_id = random.randint(1, num_questions)
    answer = random.randint(1, 7)

    # Insert the generated data into the Answers table
    cursor.execute(
        "INSERT INTO Answers (User_id, Question_id, Answer) VALUES (%s, %s, %s);",
        (user_id, question_id, answer)
    )

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
