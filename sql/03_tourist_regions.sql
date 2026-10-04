SELECT
    region,
    COUNT(value) AS years_with_data,
    SUM(value) AS total_tourists_thousands
FROM inbound_regions
WHERE year BETWEEN 2013 AND 2022
  AND region <> 'Total'
GROUP BY region
ORDER BY total_tourists_thousands DESC;