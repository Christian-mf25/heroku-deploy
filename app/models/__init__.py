from os import getenv
import psycopg2


configs = {
	"host": getenv("DB_HOST"),
	"database": getenv("DB_NAME"),
	"user": getenv("DB_USER"),
	"password": getenv("DB_PASSWORD")
}


conn = psycopg2.connect(**configs)

class DatabaseCoennector:

	@classmethod
	def create_table(cls):
		cls.get_con_cur()
		query = """
			CREATE TABLE IF NOT EXISTS ka_series(
				id              BIGSERIAL PRIMARY KEY,
				serie           VARCHAR(100)NOT NULL UNIQUE,
				seasons         INTEGER NOT NULL,
				released_date   DATE NOT NULL,
				genre           VARCHAR(50) NOT NULL,
				imdb_rating     FLOAT NOT NULL
			);
		"""
		cls.cur.execute(query)
		cls.commit_and_close()

	@classmethod
	def get_con_cur(cls):
		cls.conn = psycopg2.connect(**configs)
		cls.cur = cls.conn.cursor()

	@classmethod
	def commit_and_close(cls):
		cls.conn.commit()
		cls.cur.close()
		cls.conn.close()