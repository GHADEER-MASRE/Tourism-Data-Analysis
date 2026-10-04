WITH top_5 AS (
    SELECT
        country,
        SUM(value) AS total_tourists
    FROM inbound_arrivals
    WHERE indicator = 'Overnights visitors (tourists)'
      AND year BETWEEN 2013 AND 2022
    GROUP BY country
    HAVING COUNT(value) >= 5
    ORDER BY total_tourists DESC
    LIMIT 5
)

SELECT
    t.country,
    p.purpose,
    SUM(p.value) AS total_visitors
FROM top_5 t
JOIN inbound_purpose p
    ON t.country = p.country
WHERE p.year BETWEEN 2013 AND 2022
  AND p.purpose IN ('Personal', 'Business and professional')
GROUP BY
    t.country,
    p.purpose
ORDER BY
    t.country,
    total_visitors DESC;