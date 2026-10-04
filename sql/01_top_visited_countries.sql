SELECT
    country,
    COUNT(value) AS years_with_data,
    SUM(value) AS total_tourists_thousands
FROM inbound_arrivals
WHERE indicator = 'Overnights visitors (tourists)'
  AND year BETWEEN 2013 AND 2022
GROUP BY country
HAVING COUNT(value) >= 5
ORDER BY total_tourists_thousands DESC
LIMIT 10;