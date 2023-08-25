from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text
from api.model.worker import Worker


class WorkerRepository:
    def __init__(self, database):
        self.database = database

    def get_worker(self, order_id):
        """
            Busca um entregador aleatório para realizar a entrega,
            caso a loja tenha entregadores exclusivos será buscado um entregador aleatório dos exclusivos
            :param order_id:
        """
        with self.database() as db:
            try:
                query = text(f"SELECT worker.id, worker.name, exclusive_worker.store_id FROM worker "
                             f"LEFT JOIN (SELECT store_id, worker_id FROM store_exclusive_worker ORDER BY RAND()) exclusive_worker "
                             f"ON worker.id = exclusive_worker.worker_id AND exclusive_worker.store_id = {order_id} "
                             f"ORDER BY exclusive_worker.store_id DESC, rand() "
                             f"LIMIT 1;")
                data = db.get_engine().connect().execute(query).mappings().all()
                return data
            except NoResultFound:
                return None

    def get_all(self):
        """
            Busca todos os entregadores cadastrados
        """
        with self.database() as db:
            try:
                data = db.session.query(Worker).all()
                return data
            except NoResultFound:
                return None
