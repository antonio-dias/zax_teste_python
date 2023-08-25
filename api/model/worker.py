from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float

base = declarative_base()


class Worker(base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    charge = Column(Float, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
