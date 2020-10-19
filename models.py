# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Float, ForeignKey, String, Table, text
from sqlalchemy.dialects.mysql import INTEGER, LONGBLOB, LONGTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Order(Base):
    __tablename__ = 'orders'

    id = Column(INTEGER(11), primary_key=True, index=True)
    employee_id = Column(ForeignKey('employees.id'), index=True)
    customer_id = Column(ForeignKey('customers.id'), index=True)
    order_date = Column(DateTime)
    shipped_date = Column(DateTime)
    shipper_id = Column(ForeignKey('shippers.id'), index=True)
    ship_name = Column(String(50))
    ship_address = Column(LONGTEXT)
    ship_city = Column(String(50))
    ship_state_province = Column(String(50))
    ship_zip_postal_code = Column(String(50), index=True)
    ship_country_region = Column(String(50))
    shipping_fee = Column(DECIMAL(19, 4))
    taxes = Column(DECIMAL(19, 4))
    payment_type = Column(String(50))
    paid_date = Column(DateTime)
    notes = Column(LONGTEXT)
    tax_rate = Column(Float(asdecimal=True), server_default=text("0"))
    tax_status_id = Column(ForeignKey('orders_tax_status.id'), index=True)
    status_id = Column(ForeignKey('orders_status.id'), index=True, server_default=text("0"))

    customer = relationship('Customer')
    employee = relationship('Employee')
    shipper = relationship('Shipper')
    status = relationship('OrdersStatu')
    tax_status = relationship('OrdersTaxStatu')


class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(INTEGER(11), primary_key=True, index=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False, index=True)
    product_id = Column(ForeignKey('products.id'), index=True)
    quantity = Column(DECIMAL(18, 4), nullable=False)
    unit_price = Column(DECIMAL(19, 4))
    discount = Column(Float(asdecimal=True), nullable=False, server_default=text("0"))
    status_id = Column(ForeignKey('order_details_status.id'), index=True)
    date_allocated = Column(DateTime)
    purchase_order_id = Column(INTEGER(11), index=True)
    inventory_id = Column(INTEGER(11), index=True)

    order = relationship('Order')
    product = relationship('Product')
    status = relationship('OrderDetailsStatu')


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(INTEGER(11), primary_key=True)
    company = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    first_name = Column(String(50), index=True)
    email_address = Column(String(50))
    job_title = Column(String(50))
    business_phone = Column(String(25))
    home_phone = Column(String(25))
    mobile_phone = Column(String(25))
    fax_number = Column(String(25))
    address = Column(LONGTEXT)
    city = Column(String(50), index=True)
    state_province = Column(String(50), index=True)
    zip_postal_code = Column(String(15), index=True)
    country_region = Column(String(50))
    web_page = Column(LONGTEXT)
    notes = Column(LONGTEXT)
    attachments = Column(LONGBLOB)


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(INTEGER(11), primary_key=True)
    company = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    first_name = Column(String(50), index=True)
    email_address = Column(String(50))
    job_title = Column(String(50))
    business_phone = Column(String(25))
    home_phone = Column(String(25))
    mobile_phone = Column(String(25))
    fax_number = Column(String(25))
    address = Column(LONGTEXT)
    city = Column(String(50), index=True)
    state_province = Column(String(50), index=True)
    zip_postal_code = Column(String(15), index=True)
    country_region = Column(String(50))
    web_page = Column(LONGTEXT)
    notes = Column(LONGTEXT)
    attachments = Column(LONGBLOB)

    privileges = relationship('Privilege', secondary='employee_privileges')


class Shipper(Base):
    __tablename__ = 'shippers'

    id = Column(INTEGER(11), primary_key=True)
    company = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    first_name = Column(String(50), index=True)
    email_address = Column(String(50))
    job_title = Column(String(50))
    business_phone = Column(String(25))
    home_phone = Column(String(25))
    mobile_phone = Column(String(25))
    fax_number = Column(String(25))
    address = Column(LONGTEXT)
    city = Column(String(50), index=True)
    state_province = Column(String(50), index=True)
    zip_postal_code = Column(String(15), index=True)
    country_region = Column(String(50))
    web_page = Column(LONGTEXT)
    notes = Column(LONGTEXT)
    attachments = Column(LONGBLOB)


class OrdersStatu(Base):
    __tablename__ = 'orders_status'

    id = Column(TINYINT(4), primary_key=True)
    status_name = Column(String(50), nullable=False)

class OrdersTaxStatu(Base):
    __tablename__ = 'orders_tax_status'

    id = Column(TINYINT(4), primary_key=True)
    tax_status_name = Column(String(50), nullable=False)


class Product(Base):
    __tablename__ = 'products'

    supplier_ids = Column(LONGTEXT)
    id = Column(INTEGER(11), primary_key=True)
    product_code = Column(String(25), index=True)
    product_name = Column(String(50))
    description = Column(LONGTEXT)
    standard_cost = Column(DECIMAL(19, 4))
    list_price = Column(DECIMAL(19, 4), nullable=False)
    reorder_level = Column(INTEGER(11))
    target_level = Column(INTEGER(11))
    quantity_per_unit = Column(String(50))
    discontinued = Column(TINYINT(1), nullable=False, server_default=text("0"))
    minimum_reorder_quantity = Column(INTEGER(11))
    category = Column(String(50))
    attachments = Column(LONGBLOB)

class OrderDetailsStatu(Base):
    __tablename__ = 'order_details_status'

    id = Column(INTEGER(11), primary_key=True)
    status_name = Column(String(50), nullable=False)



t_employee_privileges = Table(
    'employee_privileges', metadata,
    Column('employee_id', ForeignKey('employees.id'), primary_key=True, nullable=False, index=True),
    Column('privilege_id', ForeignKey('privileges.id'), primary_key=True, nullable=False, index=True)
)


class Privilege(Base):
    __tablename__ = 'privileges'

    id = Column(INTEGER(11), primary_key=True)
    privilege_name = Column(String(50))
