SELECT customer.customer_id, email, count(payment_id) As payments_count, 
    CAST(sum(amount) AS FLOAT) As total_amount
FROM customer
    INNER JOIN payment ON payment.customer_id = customer.customer_id
GROUP BY customer.customer_id, email
ORDER BY total_amount DESC
LIMIT 10
