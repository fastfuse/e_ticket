import os

from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Login
login = LoginManager(app)
login.login_view = 'login'

# Admin
admin = Admin(app)

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# logger instance
logger = app.logger


# ===========================================

@app.shell_context_processor
def make_shell_context():
    """
    Add db and models to shell context.
    """
    return {'db': db, 'models': models}


from application import models

from .admin import admin_blueprint
# from .auth import auth_blueprint
from .index import index_blueprint
from .api import api_blueprint

app.register_blueprint(admin_blueprint)
# app.register_blueprint(auth_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(api_blueprint)
