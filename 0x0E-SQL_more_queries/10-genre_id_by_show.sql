-- lists all shows contained in a database that has at lease one genre link

SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
     INNER JOIN tv_show_genres AS tsg
     ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id ASC;
