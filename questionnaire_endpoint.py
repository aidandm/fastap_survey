from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import psycopg2

app = FastAPI()

@app.post("/submit-form")
async def submit_form(request: Request):
    # Get the form data from the request body
    form_data = await request.form()

    # Extract the form data into variables
    q1 = form_data["question1"]
    q2 = form_data["question1"]
    q3 = form_data["question1"]
    q4 = form_data["question1"]
    q5 = form_data["question1"]
    q6 = form_data["question1"]
    q7 = form_data["question1"]
    q8 = form_data["question1"]
    q9 = form_data["question1"]
    q10 = form_data["question1"]
    q11 = form_data["question1"]
    q12 = form_data["question1"]
    q13 = form_data["question1"]
    q14 = form_data["question1"]
    q15 = form_data["question1"]
    q16 = form_data["question1"]
    q17 = form_data["question1"]
    q18 = form_data["question1"]
    q19 = form_data["question1"]

    #From info form
    name = form_data["first_name"] + ' ' + form_data["last_name"]
    age = form_data["age"]
    gender = form_data["gender"]
    occupation = form_data["occupation"]
    education = form_data["education"]

    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="survey",
        user="postgres",
        password="Apple0rangeBanana^$"
    )

    # Insert the form data into the database
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO response () "
            "VALUES (%s, %s, %s, %s, %s)",
            (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19)
        )
        cur.execute(
            "INSERT INTO form_responses (name, age, gender, occupation, education) "
            "VALUES (%s, %s, %s, %s, %s)",
            ()
        )
        conn.commit()

    # Return a response indicating success
    return {"message": "Form submitted successfully!"}
