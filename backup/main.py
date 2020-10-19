
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app = FastAPI()

templates = Jinja2Templates(directory="venv/templates")
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("layout_good.html",{
        "request": request
    })

