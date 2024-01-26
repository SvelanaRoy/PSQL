CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS singers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS genres_singers (
	genre_id INTEGER REFERENCES genres(id),
	singer_id INTEGER REFERENCES singers(id),
	CONSTRAINT pk_singers PRIMARY KEY (genre_id, singer_id)
);

CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	issued_year INTEGER  CHECK (issued_year > 1500)
);

CREATE TABLE IF NOT EXISTS singers_albums (
	singer_id INTEGER REFERENCES singers(id),
	album_id INTEGER REFERENCES albums(id),
	CONSTRAINT pk_albums PRIMARY KEY (singer_id,album_id)
);

CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	album_id INTEGER NOT NULL REFERENCES albums(id),
	duration INTEGER  CHECK (duration > 0)
);

CREATE TABLE IF NOT EXISTS collections (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	issued_year INTEGER  CHECK (issued_year > 1500)
);

CREATE TABLE IF NOT EXISTS tracks_collections (
	collection_id INTEGER REFERENCES collections(id),
	track_id INTEGER REFERENCES tracks(id),
	CONSTRAINT pk_tracks PRIMARY KEY (collection_id,track_id)
);