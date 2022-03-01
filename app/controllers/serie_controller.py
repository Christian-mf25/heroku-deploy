from flask import jsonify, request
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation

def series():
	series = Series.read_series()
	series_list = Series.serialize_serie(series)

	return jsonify({"data": series_list}), 200

def select_by_id(serie_id):
	serie = Series.read_by_id(serie_id)
	if serie is None:
		return {"error": "Not found"}
	selected_serie = Series.serialize_serie(serie)

	return jsonify({"data": selected_serie}), 200

def create():
	data = request.get_json()
	serie = Series(**data)

	try: 
		inserted_serie = serie.create_serie()
	
	except UniqueViolation as e:
		return jsonify({"error": e.args}), 422


	inserted_serie = Series.serialize_serie(inserted_serie)

	return jsonify(inserted_serie), 201
