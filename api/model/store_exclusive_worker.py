from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, ForeignKey

base = declarative_base()


class StoreExclusiveWorker(base):
    __tablename__ = "store_exclusive_worker"

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey("worker.id"))
    store_id = Column(Integer, ForeignKey("store.id"))
