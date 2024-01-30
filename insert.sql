INSERT INTO genres(name) 
VALUES
('Рок'),
('Фолк'),
('Джаз');

INSERT INTO singers(name) 
VALUES
('ДДТ'),
('Сплин'),
('Хелависа'),
('Фрэнк Синатра');

INSERT INTO albums(name,issued_year) 
VALUES
('Актриса Весна',1992),
('Метель августа',2000),
('Гранатовый альбом',1998),
('All the Way',1961),
('Люцифераза',2018),
('Test',2020);

INSERT INTO tracks(name,album_id,duration) 
VALUES
('Дождь',1,303),
('Родина',1,278),
('Актриса весна',1,343),
('Ночь-Людмила',2,244),
('Летели облака',2,244),
('Катись, колесо!',3,167),
('Весь этот бред',3,186),
('Немного огня',5,262),
('Дракон-2018',5,246),
('All the Way',4,175),
('is my test',4,170),
('is my test no collection',4,170),
('testim2',6,173),
('testim',6,170);

INSERT INTO collections(name,issued_year) 
VALUES
('ДДТ лучшее',2001),
('Наш рок',2005),
('Рок и фолк',2020),
('My Soul',2021);

INSERT INTO genres_singers(genre_id,singer_id) 
VALUES
(1,1),
(1,2),
(2,3),
(3,4);

INSERT INTO singers_albums(singer_id,album_id) 
VALUES
(1,1),
(1,2),
(2,3),
(3,5),
(4,4),
(4,6);

INSERT INTO tracks_collections(collection_id,track_id) 
VALUES
(1,1),
(1,2),
(1,3),
(1,4),
(1,5),
(2,1),
(2,2),
(2,3),
(2,4),
(2,5),
(2,6),
(2,7),
(3,1),
(3,2),
(3,3),
(3,4),
(3,5),
(3,6),
(3,7),
(3,8),
(3,9),
(4,8),
(4,9),
(4,10),
(4,11);