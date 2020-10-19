import datetime
#from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from database import Base
from sqlalchemy import Column, DECIMAL, DateTime, Float, ForeignKey, String, Table, text,Boolean,Integer,Numeric
from sqlalchemy.dialects.mysql import BIT, INTEGER, LONGBLOB, MEDIUMTEXT, SMALLINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class Category(Base):
    __tablename__ = 'categories'

    CategoryID = Column(INTEGER(11), primary_key=True)
    CategoryName = Column(String(15), nullable=False, index=True)
    Description = Column(MEDIUMTEXT)
    Picture = Column(LONGBLOB)

class Customerdemographic(Base):
    __tablename__ = 'customerdemographics'

    CustomerTypeID = Column(String(10), primary_key=True)
    CustomerDesc = Column(MEDIUMTEXT)
class Customer(Base):
    __tablename__ = 'customers'

    CustomerID = Column(String(5), primary_key=True)
    CompanyName = Column(String(40), nullable=False, index=True)
    ContactName = Column(String(30))
    ContactTitle = Column(String(30))
    Address = Column(String(60))
    City = Column(String(15), index=True)
    Region = Column(String(15), index=True)
    PostalCode = Column(String(10), index=True)
    Country = Column(String(15))
    Phone = Column(String(24))
    Fax = Column(String(24))

    customerdemographics = relationship('Customerdemographic', secondary='customercustomerdemo')

class Employee(Base):
    __tablename__ = 'employees'

    EmployeeID = Column(INTEGER(11), primary_key=True)
    LastName = Column(String(20), nullable=False, index=True)
    FirstName = Column(String(10), nullable=False)
    Title = Column(String(30))
    TitleOfCourtesy = Column(String(25))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String(60))
    City = Column(String(15))
    Region = Column(String(15))
    PostalCode = Column(String(10), index=True)
    Country = Column(String(15))
    HomePhone = Column(String(24))
    Extension = Column(String(4))
    Photo = Column(LONGBLOB)
    Notes = Column(MEDIUMTEXT, nullable=False)
    ReportsTo = Column(ForeignKey('employees.EmployeeID'), index=True)
    PhotoPath = Column(String(255))
    Salary = Column(Float)

    parent = relationship('Employee', remote_side=[EmployeeID])
    territories = relationship('Territory', secondary='employeeterritories')

class Region(Base):
    __tablename__ = 'region'

    RegionID = Column(INTEGER(11), primary_key=True)
    RegionDescription = Column(String(50), nullable=False)



class Shipper(Base):
    __tablename__ = 'shippers'

    ShipperID = Column(INTEGER(11), primary_key=True)
    CompanyName = Column(String(40), nullable=False)
    Phone = Column(String(24))


class Supplier(Base):
    __tablename__ = 'suppliers'

    SupplierID = Column(INTEGER(11), primary_key=True)
    CompanyName = Column(String(40), nullable=False, index=True)
    ContactName = Column(String(30))
    ContactTitle = Column(String(30))
    Address = Column(String(60))
    City = Column(String(15))
    Region = Column(String(15))
    PostalCode = Column(String(10), index=True)
    Country = Column(String(15))
    Phone = Column(String(24))
    Fax = Column(String(24))
    HomePage = Column(MEDIUMTEXT)

class Order(Base):
    __tablename__ = 'orders'

    OrderID = Column(INTEGER(11), primary_key=True)
    CustomerID = Column(ForeignKey('customers.CustomerID'), index=True)
    EmployeeID = Column(ForeignKey('employees.EmployeeID'), index=True)
    OrderDate = Column(DateTime, default=datetime.datetime.utcnow(), index=True)
    RequiredDate = Column(DateTime)
    ShippedDate = Column(DateTime, index=True)
    ShipVia = Column(ForeignKey('shippers.ShipperID'), index=True)
    Freight = Column(DECIMAL(10, 4))
    ShipName = Column(String(40))
    ShipAddress = Column(String(60))
    ShipCity = Column(String(15))
    ShipRegion = Column(String(15))
    ShipPostalCode = Column(String(10), index=True)
    ShipCountry = Column(String(15))

    customer = relationship('Customer')
    employee = relationship('Employee')
    shipper = relationship('Shipper')

class Product(Base):
    __tablename__ = 'products'

    ProductID = Column(INTEGER(11), primary_key=True)
    ProductName = Column(String(40), nullable=False, index=True)
    SupplierID = Column(ForeignKey('suppliers.SupplierID'), index=True)
    CategoryID = Column(ForeignKey('categories.CategoryID'), index=True)
    QuantityPerUnit = Column(String(20))
    UnitPrice = Column(DECIMAL(10, 4))
    UnitsInStock = Column(SMALLINT(2), server_default=text("0"))
    UnitsOnOrder = Column(SMALLINT(2), server_default=text("0"))
    ReorderLevel = Column(SMALLINT(2), server_default=text("0"))
    Discontinued = Column(BIT(1), nullable=False)

    category = relationship('Category')
    supplier = relationship('Supplier')


class Territory(Base):
    __tablename__ = 'territories'

    TerritoryID = Column(String(20), primary_key=True)
    TerritoryDescription = Column(String(50), nullable=False)
    RegionID = Column(ForeignKey('region.RegionID'), nullable=False, index=True)

    region = relationship('Region')



class OrderDetail(Base):
    __tablename__ = 'order details'

    OrderID = Column(ForeignKey('orders.OrderID'), primary_key=True, nullable=False)
    ProductID = Column(ForeignKey('products.ProductID'), primary_key=True, nullable=False, index=True)
    UnitPrice = Column(DECIMAL(10, 4), nullable=False)
    Quantity = Column(SMALLINT(2), nullable=False, server_default=text("1"))
    Discount = Column(Float(8, True), nullable=False, server_default=text("0"))

    order = relationship('Order')
    product = relationship('Product')


t_invoices = Table(
    'invoices', metadata,
    Column('ShipName', String(40)),
    Column('ShipAddress', String(60)),
    Column('ShipCity', String(15)),
    Column('ShipRegion', String(15)),
    Column('ShipPostalCode', String(10)),
    Column('ShipCountry', String(15)),
    Column('CustomerID', String(5)),
    Column('CustomerName', String(40)),
    Column('Address', String(60)),
    Column('City', String(15)),
    Column('Region', String(15)),
    Column('PostalCode', String(10)),
    Column('Country', String(15)),
    Column('Salesperson', Float(asdecimal=True), server_default=text("'0'")),
    Column('OrderID', INTEGER(11), server_default=text("'0'")),
    Column('OrderDate', DateTime),
    Column('RequiredDate', DateTime),
    Column('ShippedDate', DateTime),
    Column('ShipperName', String(40)),
    Column('ProductID', INTEGER(11)),
    Column('ProductName', String(40)),
    Column('UnitPrice', DECIMAL(10, 4), server_default=text("'0.0000'")),
    Column('Quantity', SMALLINT(2), server_default=text("'1'")),
    Column('Discount', Float(8, True), server_default=text("'0'")),
    Column('ExtendedPrice', Float(25, True)),
    Column('Freight', DECIMAL(10, 4), server_default=text("'0.0000'"))
)


t_order_details_extended = Table(
    'order details extended', metadata,
    Column('OrderID', INTEGER(11)),
    Column('ProductID', INTEGER(11)),
    Column('ProductName', String(40)),
    Column('UnitPrice', DECIMAL(10, 4), server_default=text("'0.0000'")),
    Column('Quantity', SMALLINT(2), server_default=text("'1'")),
    Column('Discount', Float(8, True), server_default=text("'0'")),
    Column('ExtendedPrice', Float(25, True))
)


t_order_subtotals = Table(
    'order subtotals', metadata,
    Column('OrderID', INTEGER(11)),
    Column('Subtotal', Float(25, True))
)


t_orders_qry = Table(
    'orders qry', metadata,
    Column('OrderID', INTEGER(11), server_default=text("'0'")),
    Column('CustomerID', String(5)),
    Column('EmployeeID', INTEGER(11)),
    Column('OrderDate', DateTime),
    Column('RequiredDate', DateTime),
    Column('ShippedDate', DateTime),
    Column('ShipVia', INTEGER(11)),
    Column('Freight', DECIMAL(10, 4), server_default=text("'0.0000'")),
    Column('ShipName', String(40)),
    Column('ShipAddress', String(60)),
    Column('ShipCity', String(15)),
    Column('ShipRegion', String(15)),
    Column('ShipPostalCode', String(10)),
    Column('ShipCountry', String(15)),
    Column('CompanyName', String(40)),
    Column('Address', String(60)),
    Column('City', String(15)),
    Column('Region', String(15)),
    Column('PostalCode', String(10)),
    Column('Country', String(15))
)


t_product_sales_for_1997 = Table(
    'product sales for 1997', metadata,
    Column('CategoryName', String(15)),
    Column('ProductName', String(40)),
    Column('ProductSales', Float(25, True))
)


t_products_above_average_price = Table(
    'products above average price', metadata,
    Column('ProductName', String(40)),
    Column('UnitPrice', DECIMAL(10, 4), server_default=text("'0.0000'"))
)


t_products_by_category = Table(
    'products by category', metadata,
    Column('CategoryName', String(15)),
    Column('ProductName', String(40)),
    Column('QuantityPerUnit', String(20)),
    Column('UnitsInStock', SMALLINT(2), server_default=text("'0'")),
    Column('Discontinued', BIT(1), server_default=text("'b''0'''"))
)


t_quarterly_orders = Table(
    'quarterly orders', metadata,
    Column('CustomerID', String(5)),
    Column('CompanyName', String(40)),
    Column('City', String(15)),
    Column('Country', String(15))
)

t_alphabetical_list_of_products = Table(
    'alphabetical list of products', metadata,
    Column('ProductID', INTEGER(11), server_default=text("'0'")),
    Column('ProductName', String(40)),
    Column('SupplierID', INTEGER(11)),
    Column('CategoryID', INTEGER(11)),
    Column('QuantityPerUnit', String(20)),
    Column('UnitPrice', DECIMAL(10, 4), server_default=text("'0.0000'")),
    Column('UnitsInStock', SMALLINT(2), server_default=text("'0'")),
    Column('UnitsOnOrder', SMALLINT(2), server_default=text("'0'")),
    Column('ReorderLevel', SMALLINT(2), server_default=text("'0'")),
    Column('Discontinued', BIT(1), server_default=text("'b''0'''")),
    Column('CategoryName', String(15))
)
t_category_sales_for_1997 = Table(
    'category sales for 1997', metadata,
    Column('CategoryName', String(15)),
    Column('CategorySales', Float(25, True))
)


t_current_product_list = Table(
    'current product list', metadata,
    Column('ProductID', INTEGER(11), server_default=text("'0'")),
    Column('ProductName', String(40))
)


t_customer_and_suppliers_by_city = Table(
    'customer and suppliers by city', metadata,
    Column('City', String(15)),
    Column('CompanyName', String(40)),
    Column('ContactName', String(30)),
    Column('Relationship', String(9))
)


t_sales_by_category = Table(
    'sales by category', metadata,
    Column('CategoryID', INTEGER(11), server_default=text("'0'")),
    Column('CategoryName', String(15)),
    Column('ProductName', String(40)),
    Column('ProductSales', Float(25, True))
)


t_sales_totals_by_amount = Table(
    'sales totals by amount', metadata,
    Column('SaleAmount', Float(25, True)),
    Column('OrderID', INTEGER(11), server_default=text("'0'")),
    Column('CompanyName', String(40)),
    Column('ShippedDate', DateTime)
)

t_employeeterritories = Table(
    'employeeterritories', metadata,
    Column('EmployeeID', ForeignKey('employees.EmployeeID'), primary_key=True, nullable=False),
    Column('TerritoryID', ForeignKey('territories.TerritoryID'), primary_key=True, nullable=False, index=True)
)

t_customercustomerdemo = Table(
    'customercustomerdemo', metadata,
    Column('CustomerID', ForeignKey('customers.CustomerID'), primary_key=True, nullable=False),
    Column('CustomerTypeID', ForeignKey('customerdemographics.CustomerTypeID'), primary_key=True, nullable=False, index=True)
)


t_summary_of_sales_by_quarter = Table(
    'summary of sales by quarter', metadata,
    Column('ShippedDate', DateTime),
    Column('OrderID', INTEGER(11), server_default=text("'0'")),
    Column('Subtotal', Float(25, True))
)


t_summary_of_sales_by_year = Table(
    'summary of sales by year', metadata,
    Column('ShippedDate', DateTime),
    Column('OrderID', INTEGER(11), server_default=text("'0'")),
    Column('Subtotal', Float(25, True))
)