from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import psycopg2

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def show_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/questionnaire")
async def show_questionnaire(request: Request):
    return templates.TemplateResponse("questionnaire.html", {"request": request})


@app.post("/submit-form")
async def submit_form(request: Request):
    # Get the form data from the request body
    form_data = await request.form()

    # Extract the form data into variables
    q1 = form_data["question1"]
    q2 = form_data["question2"]
    q3 = form_data["question3"]
    q4 = form_data["question4"]
    q5 = form_data["question5"]
    q6 = form_data["question6"]
    q7 = form_data["question7"]
    q8 = form_data["question8"]
    q9 = form_data["question9"]
    q10 = form_data["question10"]
    q11 = form_data["question11"]
    q12 = form_data["question12"]
    q13 = form_data["question13"]
    q14 = form_data["question14"]
    q15 = form_data["question15"]
    q16 = form_data["question16"]
    q17 = form_data["question17"]
    q18 = form_data["question18"]
    q19 = form_data["question19"]

    #From info form
    name = form_data["first_name"] + ' ' + form_data["last_name"]
    age = form_data["age"]
    gender = form_data["gender"]
    occupation = form_data["occupation"]
    education = form_data["education"]

    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Apple0rangeBanana^$"
    )

    # Insert the form data into the database
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO response (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19)
        )
        cur.execute(
            "INSERT INTO users (name, age, gender, occupation, education) "
            "VALUES (%s, %s, %s, %s, %s)",
            (name, age, gender, occupation, education)
        )
        conn.commit()

    # Return a response indicating success
    return templates.TemplateResponse("success.html", {"request": request})


