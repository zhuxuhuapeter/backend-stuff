import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime

from database import Base

class Order(Base):
    __tablename__ = "orders"

    OrderID = Column(Integer, primary_key=True, index=True)
    CustomerID =Column(String(length=5), unique=True, index=True)
    EmployeeID =Column(Integer)
    OrderDate = Column(DateTime, default=datetime.datetime.utcnow())
    RequiredDate = Column(DateTime, default=datetime.datetime.utcnow())
    ShippedDate = Column(DateTime, default=datetime.datetime.utcnow())
    ShipVia = Column(Integer)
    Freight = Column(Numeric(10,4))
    ShipName = Column(String(length=40))
    ShipAddress = Column(String(length=60))
    ShipCity = Column(String(length=15))
    ShipRegion = Column(String(length=15))
    ShipPostalCode = Column(String(length=10))
    ShipCountry = Column(String(length=15))

