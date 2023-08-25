from dotenv import load_dotenv
from flask import Flask
from api.routes.order_router import order_router
from api.routes.worker_router import worker_router
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)
app.register_blueprint(order_router, url_prefix='/order')
app.register_blueprint(worker_router, url_prefix='/worker')
spec = FlaskPydanticSpec('flask', title="Teste ZAX")
spec.register(app)


if __name__ == '__main__':
    load_dotenv()

    app.run(debug=True, host='0.0.0.0', port=5000)
