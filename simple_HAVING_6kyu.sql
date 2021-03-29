SELECT age, COUNT(id) As total_people
FROM people
GROUP BY age
HAVING COUNT(id) >= 10
