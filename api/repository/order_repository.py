from api.model.order import Order
from api.model.store import Store
from api.model.worker import Worker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text


class OrderRepository:
    def __init__(self, database):
        self.database = database

    def get_resume(self, store_id, worker_id):
        """
            Busca um resumo do entregador com o pedido que foi atendido
            :param store_id:
            :param worker_id:
        """
        with self.database() as db:
            try:
                data = db.session.query(Order) \
                    .join(Store, Order.store_id == Store.id) \
                    .join(Worker, Order.worker_id == Worker.id) \
                    .with_entities(
                        Order.id,
                        Store.name.label("store_name"),
                        Store.bonus_payment.label("store_bonus_payment"),
                        Worker.name.label("worker_name"),
                        Worker.charge.label("worker_charge"),
                        Order.price
                    ) \
                    .filter(Order.store_id == store_id and Order.worker_id == worker_id) \
                    .all()
                return data
            except NoResultFound:
                return None

    def select_open_orders(self):
        """
            Busca todas os pedidos que estão em aberto de 1 loja
        """
        with self.database() as db:
            try:
                query = text("SELECT * FROM `order` WHERE store_id = (select store_id from `order` where worker_id is NULL limit 1)")
                data = db.get_engine().connect().execute(query).mappings().all()
                return data
            except NoResultFound:
                return None

    def save_worker(self, orders, worker_id):
        """
            Atualiza os pedidos que o entregador irá atender
            :param orders:
            :param worker_id:
        """
        with self.database() as db:
            try:
                for order in orders:
                    db.session.query(Order).filter(Order.id == order.id).update({"worker_id": worker_id})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
