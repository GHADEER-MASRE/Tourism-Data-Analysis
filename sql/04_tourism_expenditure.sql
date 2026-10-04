SELECT
    country,
    COUNT(DISTINCT year) AS years_with_data,
    AVG(value) AS average_annual_travel_expenditure_millions
FROM inbound_expenditure
WHERE year BETWEEN 2013 AND 2022
  AND expenditure_type = 'Travel'
  AND value IS NOT NULL
GROUP BY country
HAVING COUNT(DISTINCT year) >= 8
ORDER BY average_annual_travel_expenditure_millions DESC
LIMIT 10;