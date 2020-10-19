
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from models import Order, OrderDetail
from fastapi.middleware.cors import CORSMiddleware
import crud, models, schemas

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = SessionLocal()
    try:        
        yield db
    finally :
        db.close()



@app.get("/order/")
def read_orders(skip: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@app.get("/order/{id}", response_model=schemas.Order)
#@app.get("/order/{id}")
def read_order(id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, id=id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order





