from flask import Blueprint, Flask 
from app.routes.serie_route import bp as bp_serie

bp_api = Blueprint("api", __name__, url_prefix="/")

def init_app(app:Flask):

	bp_api.register_blueprint(bp_serie)
	app.register_blueprint(bp_api)
