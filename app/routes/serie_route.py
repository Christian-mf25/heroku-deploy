from flask import Blueprint
from app.controllers import serie_controller

bp = Blueprint("series", __name__, url_prefix="/series")

bp.get("")(serie_controller.series)
bp.get("/<serie_id>")(serie_controller.select_by_id)
bp.post("")(serie_controller.create)