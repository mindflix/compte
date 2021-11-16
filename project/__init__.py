from flask import Flask
from project import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    from . import db
    db.init_app(app)

    from .main import main_bp
    app.register_blueprint(main_bp)
    app.add_url_rule('/', endpoint='index')

    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.add_url_rule('/auth', endpoint='auth')

    from .task import task_bp
    app.register_blueprint(task_bp, url_prefix="/task")
    app.add_url_rule('/task', endpoint='task')

    from .counting import counting_bp
    app.register_blueprint(counting_bp, url_prefix="/counting")
    app.add_url_rule('/counting', endpoint='counting')

    return app
