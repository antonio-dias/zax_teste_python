from flask import Blueprint
from api.config.database import Database
from api.repository.order_repository import OrderRepository
from api.repository.worker_repository import WorkerRepository
from api.utils.format_return import format_return

order_router = Blueprint('order', __name__)


@order_router.route('/', methods=['GET'], defaults={'worker_id': None})
@order_router.route('/<int:worker_id>', methods=['GET'])
@format_return
def order(worker_id):
    try:
        order_repo = OrderRepository(Database)
        orders = order_repo.select_open_orders()
        if not worker_id:
            worker_repo = WorkerRepository(Database)
            order_id = orders[0].id
            worker = worker_repo.get_worker(order_id)
            worker_id = worker[0].id

        order_repo.save_worker(orders, worker_id)

        store_id = orders[0].store_id
        resume_payment = order_repo.get_resume(store_id, worker_id)
    except Exception as exception:
        print(exception)
        return {'message': 'Verifique os logs!', 'status': 'erro'}, 500

    return [dict(result._mapping) for result in resume_payment]
