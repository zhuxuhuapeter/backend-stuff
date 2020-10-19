from typing import List, Optional
import datetime
from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    quantity: Optional[int] = None
    unitprice:  Optional[float] = None


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetail(OrderDetailBase):
    orderid: int
    productid: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    id: int


class OrderCreate(OrderBase):
     id: int


class Order(OrderBase):

    id: int
    ship_name: str

    class Config:
        orm_mode = True