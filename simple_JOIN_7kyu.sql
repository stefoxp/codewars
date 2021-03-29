SELECT products.*, companies.name as company_name
FROM products
    INNER JOIN companies
        ON companies.id = products.company_id
