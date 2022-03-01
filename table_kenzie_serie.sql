CREATE TABLE IF NOT EXISTS ka_series(
    id              BIGSERIAL PRIMARY KEY,
    serie           VARCHAR(100)NOT NULL UNIQUE,
    seasons         INTEGER NOT NULL,
    released_date   DATE NOT NULL,
    genre           VARCHAR(50) NOT NULL,
    imdb_rating     FLOAT NOT NULL
);

insert into 
	ka_series(serie, seasons, released_date, genre, imdb_rating)
values
	('CHANNEL zero', 4, '11/10/2016', 'DRama, FantSY', 7.2),	
	('Breaking Bad', 5, '20/01/2008', 'Drama', 9.4)
	('Vikings', 6, '03/03/2013', 'Drama, Guerra', 8.5)
	('Rick and Morty', 5, '02/12/2013', 'Comédia, Sitcom', 9.2)
	('Friends', 10, '22/09/1994', 'Comédia, Romance', 8.8);


-- {
-- 	"serie": "breaking bad",
-- 	"seasons": 5,
-- 	"released_date": "20/01/2008",
-- 	"genre": "drama",
-- 	"imdb_rating": 9.4
-- }

-- {
-- 	"serie": "Vikings",
-- 	"seasons": "6",
-- 	"released_date": "03/03/2013",
-- 	"genre": "Drama, Guerra",
-- 	"imdb_rating": "8.5"
-- }

-- {
-- 	"serie": "Rick and Morty",
-- 	"seasons": "5",
-- 	"released_date": "02/12/2013",
-- 	"genre": "Comédia, Sitcom",
-- 	"imdb_rating": 9.2
-- }

-- {
-- 	"serie": "friends",
-- 	"seasons": 10,
-- 	"released_date": "22/09/1994",
-- 	"genre": "comédia, romance",
-- 	"imdb_rating": 8.8
-- }