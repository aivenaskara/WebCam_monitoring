from flask import Flask
from flask.templating import render_template
from flask_login import LoginManager, current_user, login_manager, login_required
from flask_migrate import Migrate

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.dataset.views import blueprint as dataset_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(dataset_blueprint)
    app.register_blueprint(user_blueprint)

    @app.route('/')
    def index():
        title = 'Проект "Сигнализация"'
        return render_template('index.html', page_title=title)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
