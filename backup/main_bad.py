import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Order
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

class OrderRequest(BaseModel):
     customerid: str

def get_db():
    db = SessionLocal()
    try:        
        yield db
    finally :
        db.close()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/tms_env")
def create_order(order_request: OrderRequest, db: Session = Depends(get_db)):
    order = Order()
    order.customerid = order_request.customerid
  #  db.add(order)
  #  db.commit()
    return{
        
        
        "code":"success",
        "message":"order created"
    }


