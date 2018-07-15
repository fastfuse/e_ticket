from flask import Blueprint

# dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)
index_blueprint = Blueprint('index_blueprint', __name__)

from . import views
