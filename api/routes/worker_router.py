from flask import Blueprint
from api.config.database import Database
from api.repository.worker_repository import WorkerRepository

worker_router = Blueprint('worker', __name__)


@worker_router.route('/', methods=['GET'])
def worker():
    try:
        worker_repo = WorkerRepository(Database)
        workers = worker_repo.get_all()
    except Exception as exception:
        print(exception)
        return {'message': 'Verifique os logs!', 'status': 'erro'}, 500

    return [dict(result.as_dict()) for result in workers]
