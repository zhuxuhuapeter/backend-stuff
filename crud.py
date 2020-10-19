from sqlalchemy.orm import Session

import models, schemas


def get_order(db: Session, id: int):
    return db.query(models.Order).filter(models.Order.id == id).first()


def get_order_by_customerid(db: Session, customerid: str):
    return db.query(models.Order).filter(models.Order.customerid == customerid).first()


def get_orders (db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: schemas.OrderCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Order(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_orderdetail(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.OrderDetail).offset(skip).limit(limit).all()


def create_OrderDetail(db: Session, item: schemas.OrderDetailCreate, orderid: int):
    db_orderdetail = models.OrderDetail(**orderdetail.dict(), orderid=orderid)
    db.add(db_orderdetail)
    db.commit()
    db.refresh(db_orderdetail)
    return db_orderdetail