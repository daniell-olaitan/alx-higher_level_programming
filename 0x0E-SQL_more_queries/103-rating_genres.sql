-- lists all genres by their rating

SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres AS tg
     INNER JOIN tv_show_genres AS tsg
     	   ON tg.id = tsg.genre_id
     INNER JOIN tv_shows AS ts
     	   ON tsg.show_id = ts.id
     INNER JOIN tv_show_ratings AS tsr
     	   ON tsr.show_id = ts.id
GROUP BY tg.name
ORDER BY rating DESC;
