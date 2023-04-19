from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import psycopg2
<<<<<<< HEAD
import bcrypt
from fastapi import FastAPI, Depends, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
=======
>>>>>>> parent of 663dd5a (Added a working signup and login page)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def show_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

<<<<<<< HEAD
#For signing up
@app.get("/usersignup")
async def show_home(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

class UserIn(BaseModel):
    email: str
    password: str
    name: str
    dob: str
    gender: str

def create_user(user: UserIn):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (email, password, name, dob, gender) VALUES (%s, %s, %s, %s, %s)",
            (user.email, hashed_password.decode("utf-8"), user.name, user.dob, user.gender)
        )
        conn.commit()

@app.post("/signup")
def signup(
    email: str = Form(...),
    password: str = Form(...),
    name: str = Form(...),
    dob: str = Form(...),
    gender: str = Form(...)
):
    user_data = UserIn(email=email, password=password, name=name, dob=dob, gender=gender)
    create_user(user_data)
    return {"message": "User created successfully"}

#Login Variables
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET = "44506ed6d57f65997ec91b173f2c228fffb91cb2fbc673c6"
manager = LoginManager(SECRET, '/login')


#Below is the section of code for logging in
def query_user(email: str):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT email, password FROM users WHERE email = %s",
            (email,)
        )
        result = cur.fetchone()
        conn.commit()

    if result:
        email, hashed_password = result
        return {"email": email, "password": hashed_password}
    else:
        return None

@app.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password.encode("utf-8")

    user = query_user(email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    stored_hashed_password = user['password'].encode("utf-8")
    if not bcrypt.checkpw(password, stored_hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token}



=======
>>>>>>> parent of 663dd5a (Added a working signup and login page)
@app.get("/questionnaire")
async def show_questionnaire(request: Request):
    return templates.TemplateResponse("questionnaire.html", {"request": request})

@app.get("/login")
async def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

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
    email = form_data["email"]

    # Connect to the database
    conn = psycopg2.connect(
        host='mis-database.cevtznumxb4e.us-west-1.rds.amazonaws.com',
        port='5432',
        database='mis-database',
        user="postgres",
        password="password123"
    )

    # Insert the form data into the database
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO survey_response (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19)
        )
        cur.execute(
            "INSERT INTO users (name, age, gender, occupation, education, email) "
            "VALUES (%s, %s, %s, %s, %s)",
            (name, age, gender, occupation, education, email)
        )
        conn.commit()

    # Return a response indicating success
    return templates.TemplateResponse("success.html", {"request": request})
