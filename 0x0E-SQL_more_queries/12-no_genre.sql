-- lists all shows without genre in the db

SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
     LEFT OUTER JOIN tv_show_genres AS tsg
     ON tsg.show_id IS NULL
ORDER BY ts.title, tsg.genre_id;
