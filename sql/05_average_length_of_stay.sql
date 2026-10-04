SELECT
    country,
    COUNT(DISTINCT year) AS years_with_data,
    SUM(CASE WHEN indicator = 'Overnights' THEN value ELSE 0 END)
        / NULLIF(
            SUM(CASE WHEN indicator = 'Guests' THEN value ELSE 0 END),
            0
        ) AS average_length_of_stay
FROM inbound_accommodation
WHERE accommodation_type = 'Total'
  AND year BETWEEN 2013 AND 2022
  AND value IS NOT NULL
GROUP BY country
HAVING
    COUNT(DISTINCT year) >= 8
    AND SUM(CASE WHEN indicator = 'Guests' THEN value ELSE 0 END) > 0
ORDER BY average_length_of_stay DESC
LIMIT 10;