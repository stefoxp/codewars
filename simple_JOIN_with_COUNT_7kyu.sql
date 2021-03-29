SELECT people.id, people.name, count(toys.id) As toy_count
FROM people
    INNER JOIN toys
        ON toys.people_id = people.id
GROUP BY people.id, people.name
