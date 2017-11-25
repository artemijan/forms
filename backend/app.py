import logging
from flask import Flask, g
from flask_cors import CORS
from flask_restful import Api


def create_app(config):
    """Main application factory."""
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    configure_views(app)
    configure_logging(app)

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    return app


def configure_views(app):
    """Configure API resource views."""
    from backend.views import (
        Form
    )

    api = Api(prefix="/api")
    api.add_resource(
        Form,
        "/form/<int:id>",
        endpoint="form"
    )
    api.add_resource(
        Form,
        "/form",
        endpoint="form-post"
    )
    api.init_app(app)


def configure_logging(app):
    """Configure application logging."""
    app_logger = logging.getLogger(__name__)
    if not app.debug:
        app_logger.setLevel(logging.ERROR)
    else:
        app_logger.setLevel(logging.DEBUG)
    app.logging = app_logger
