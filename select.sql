/* WORK2*/
SELECT name, duration
FROM tracks
WHERE duration = (SELECT MAX(duration) FROM tracks);


SELECT name, duration
FROM tracks
WHERE duration >=210
ORDER BY duration DESC;

/*OR */
SELECT name
FROM tracks
WHERE duration >=210;



SELECT name
FROM collections
WHERE issued_year BETWEEN 2018 AND 2020;

SELECT  name
FROM singers
GROUP BY name
HAVING COUNT(regexp_match (name,'\s')) = 0;

SELECT name
FROM tracks
WHERE name LIKE '%my%' or name like '%мой%';

/* WORK3*/

SELECT g.name AS genre_name, COUNT(s.name) AS count
FROM singers AS s
JOIN genres_singers AS gs ON gs.singer_id = s.id
JOIN genres AS g ON g.id = gs.genre_id
GROUP BY genre_name;


SELECT a.name AS album_name, COUNT(t.name) AS count
FROM albums AS a
JOIN tracks AS t ON t.album_id = a.id
WHERE a.issued_year BETWEEN 2019 AND 2020
GROUP BY album_name;


SELECT a.name AS album_name, ROUND(AVG(t.duration),2) AS avg
FROM albums AS a
JOIN tracks AS t ON t.album_id = a.id
GROUP BY album_name;


SELECT name AS singer
FROM (
	SELECT singer_id
	FROM (
		SELECT a.id
		FROM albums  AS a 
		WHERE  a.issued_year = 2020
	) AS alb
	JOIN singers_albums AS sa ON sa.album_id = alb.id
) AS sng
JOIN singers AS s ON s.id != sng.singer_id;


SELECT name AS name_collection
	FROM(
		SELECT distinct (collection_id)
		FROM(
			SELECT id AS track_id
			FROM (
				SELECT sa.album_id
				FROM singers_albums  AS sa 
				WHERE  sa.singer_id = 1
			) AS sa
			JOIN tracks AS t ON t.album_id = sa.album_id
		)AS tmp
		JOIN tracks_collections AS tc ON tc.track_id = tmp.track_id
	) AS collect_ids
JOIN collections AS c ON c.id = collect_ids.collection_id;




