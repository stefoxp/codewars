SELECT created_at::timestamp::date as day,
      description, 
      count(id) as count
FROM events
WHERE name = 'trained'
GROUP BY day, description
