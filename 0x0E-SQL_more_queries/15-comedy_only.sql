-- script that lists all Comedy shows in the database

SELECT tv_shows.title FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'  ORDER BY tv_shows.title ASC;
