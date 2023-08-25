"""insert in tables

Revision ID: 392c4800c181
Revises: 3197081de7e9
Create Date: 2023-08-24 03:18:27.667928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from api.config.database import Database
from api.model.worker import Worker
from api.model.store import Store
from api.model.store_exclusive_worker import StoreExclusiveWorker
from api.model.order import Order
import datetime


# revision identifiers, used by Alembic.
revision: str = '392c4800c181'
down_revision: Union[str, None] = '3197081de7e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    database = Database()

    # Populando tabela de Trabalhadores
    op.execute(sa.insert(Worker).values(name="Moto 1", charge="2"))
    op.execute(sa.insert(Worker).values(name="Moto 2", charge="2"))
    op.execute(sa.insert(Worker).values(name="Moto 3", charge="2"))
    op.execute(sa.insert(Worker).values(name="Moto 4", charge="2"))
    op.execute(sa.insert(Worker).values(name="Moto 5", charge="3"))

    # Populando tabela de Lojas
    op.execute(sa.insert(Store).values(name="Loja 1", bonus_payment="5"))
    op.execute(sa.insert(Store).values(name="Loja 2", bonus_payment="5"))
    op.execute(sa.insert(Store).values(name="Loja 3", bonus_payment="15"))

    # Populando tabela de Trabalhadores que trabalham exclusivamente para algumas lojas
    op.execute(sa.insert(StoreExclusiveWorker).values(worker_id="4", store_id="1"))

    # Populando tabela de ordem de pedidos
    op.execute(sa.insert(Order).values(store_id="1", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="1", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="1", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="2", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="2", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="2", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="2", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="3", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="3", price="50", create_time=datetime.datetime.utcnow(), worker_id=None))
    op.execute(sa.insert(Order).values(store_id="3", price="100", create_time=datetime.datetime.utcnow(), worker_id=None))


def downgrade() -> None:
    op.execute(sa.delete(StoreExclusiveWorker))
    op.execute(sa.delete(Order))
    op.execute(sa.delete(Worker))
    op.execute(sa.delete(Store))
