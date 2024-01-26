/* WORK2*/
SELECT name, duration
FROM tracks
WHERE duration = (SELECT MAX(duration) FROM tracks);

SELECT name, duration
FROM tracks
WHERE duration >=210
ORDER BY duration DESC;

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


