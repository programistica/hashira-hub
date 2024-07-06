from flask import Flask
from backend.api.v1.endpoints import api_v1_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.core.config.Config')
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')
    return app
