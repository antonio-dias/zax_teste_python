from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float

base = declarative_base()


class Order(base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("store.id"))
    price = Column(Float, nullable=False)
    create_time = Column(DateTime, nullable=False)
    worker_id = Column(Integer, ForeignKey("worker.id"))

