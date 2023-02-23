-- lists all shows contained in the db

SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
     LEFT OUTER JOIN tv_show_genres AS tsg
     ON ts.id = tsg.show_id
ORDER BY ts.title, tsg.genre_id;
