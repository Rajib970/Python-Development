from fastapi import FastAPI, Request
# import models 
# from .database import engine
# from .routers import auth
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="TodoApp/templates")

app.mount("/static",StaticFiles(directory="TodoApp/static"),name="static")


@app.get("/")
def test(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

### Pages
@app.get("/login-page")
def render_login_page(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@app.get("/register-page")
def render_login_page(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})

@app.get("/todo-page")
def render_todo_page(request:Request):
    return templates.TemplateResponse("todo.html",{"request":request})


@app.get("/healthy")
def health_check():
    return {'status':'Healthy'}

# app.include_router(auth.router)
# app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)

