import unittest
from unittest import mock
from unittest.mock import patch, MagicMock, Mock

from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from api.model.worker import Worker
from api.model.store import Store
from api.model.order import Order
from api.repository.order_repository import OrderRepository


class DatabaseMock:
    def __init__(self):
        mock_conn = mock.MagicMock()
        self.__engine = mock.MagicMock()
        self.__engine.connect.return_value.__enter__.return_value = mock_conn
        self.session = UnifiedAlchemyMagicMock(
                            data=[
                                (
                                    [
                                        mock.call.query(Order),
                                        mock.call.join(Store, Order.store_id == Store.id),
                                        mock.call.join(Worker, Order.worker_id == Worker.id),
                                        mock.call.with_entities(
                                            Order.id,
                                        ),
                                        mock.call.filter(Order.store_id == 1 and Order.worker_id == 1)
                                    ],
                                    [
                                        [Order(id="1", store_id=1, price=50, create_time="2023-08-23 00:00:00",
                                               worker_id=1)]
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


@patch.object(
    OrderRepository(DatabaseMock), "__init__", Mock(return_value=None)
)
class MyTest(unittest.TestCase):
    def test_select_open_orders(self):
        mock_app = MagicMock()
        expected_value = Order(id="1", store_id=1, price=50, create_time="2023-08-23 00:00:00",
                                               worker_id=1)
        mock_app.return_value = expected_value
        order_repository = OrderRepository(DatabaseMock)
        response = order_repository.select_open_orders()
        response = mock_app
        self.assertEqual(response, mock_app)
