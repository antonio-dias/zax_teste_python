from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from api.model.worker import Worker
from api.repository.worker_repository import WorkerRepository


class DatabaseMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
                            data=[
                                (
                                    [
                                        mock.call.query(Worker)
                                    ],
                                    [
                                        Worker(id=1, name="Moto 1", charge=2),
                                        Worker(id=2, name="Moto 2", charge=2),
                                        Worker(id=3, name="Moto 3", charge=3)
                                    ]
                                )
                            ]
                        )

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_get_all():
    worker_repository = WorkerRepository(DatabaseMock)
    response = worker_repository.get_all()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Worker)
    assert response[1].name == "Moto 2"
