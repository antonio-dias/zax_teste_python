from sqlalchemy.orm import declarative_base, relationship
from api.model.order import Order
from sqlalchemy import Column, String, Integer, Float

base = declarative_base()


class Store(base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bonus_payment = Column(Float, nullable=False)
