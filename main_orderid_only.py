import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from models import Order
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

class OrderRequest(BaseModel):
     CustomerID: str

def get_db():
    db = SessionLocal()
    try:        
        yield db
    finally :
        db.close()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    """
    display orders
    """
    orders = db.query(Order).all()
   #print(orders)
    return templates.TemplateResponse("home.html", {
        "request": request,
        "orders" : orders
    })
      # "request": request,
       # "orders" : orders

     

@app.post("/order")
def create_order(order_request: OrderRequest, db: Session = Depends(get_db)):
    """
    Add orders to db
    """
    
    order = Order()
    order.CustomerID = order_request.CustomerID
    db.add(order)
    db.commit()
    return{
        
        
        "code":"success",
        "message":"order created"
        
    }


