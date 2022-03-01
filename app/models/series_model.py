from app.models import DatabaseCoennector

class Series(DatabaseCoennector):
	serie_keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

	def __init__(self, *args, **kwargs):
		self.serie = kwargs["serie"].title()
		self.seasons = kwargs["seasons"]
		self.released_date = kwargs["released_date"]
		self.genre = kwargs["genre"].title()
		self.imdb_rating = kwargs["imdb_rating"]

	@staticmethod
	def serialize_serie(data, keys=serie_keys):
		if type(data) is tuple:
			return dict(zip(keys, data))
		if type(data) is list:
			return [dict(zip(keys, serie)) for serie in data]

	@classmethod
	def read_series(cls):
		cls.create_table()
		cls.get_con_cur()
		query = """
			SELECT * FROM ka_series;
		"""
		cls.cur.execute(query)
		series = cls.cur.fetchall()
		cls.commit_and_close()

		return series
	
	@classmethod
	def read_by_id(cls, id_selected):
		cls.create_table()
		cls.get_con_cur()
		query = """
			SELECT * FROM 
				ka_series
			WHERE id = %s
		"""
		cls.cur.execute(query, id_selected)
		serie = cls.cur.fetchone()
		cls.commit_and_close()
		return serie
	
	def create_serie(self):
		self.create_table()
		self.get_con_cur()
		query = """
			INSERT INTO
				ka_series("serie", "seasons", "released_date", "genre", "imdb_rating")
			VALUES
				(%s, %s, %s, %s, %s)
			RETURNING *
		"""

		query_values = list(self.__dict__.values())
		self.cur.execute(query, query_values)
		inserted_serie = self.cur.fetchone()
		
		self.commit_and_close()

		return inserted_serie