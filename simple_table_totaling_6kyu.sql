create temp sequence temp_seq;
SELECT 
    nextval('temp_seq') as rank, 
    CASE WHEN clan = '' THEN '[no clan specified]' ELSE clan END, 
    SUM(points) As total_points,
    COUNT(name) As total_people
FROM people
GROUP BY clan
ORDER BY total_points DESC
