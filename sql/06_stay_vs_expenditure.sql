WITH accommodation AS (
    SELECT
        country,
        year,
        SUM(CASE WHEN indicator = 'Guests' THEN value END) AS guests,
        SUM(CASE WHEN indicator = 'Overnights' THEN value END) AS overnights
    FROM inbound_accommodation
    WHERE accommodation_type = 'Total'
      AND year BETWEEN 2013 AND 2022
      AND indicator IN ('Guests', 'Overnights')
      AND value IS NOT NULL
    GROUP BY country, year
),

country_data AS (
    SELECT
        a.country,
        a.year,
        a.overnights / NULLIF(a.guests, 0) AS length_of_stay,
        e.value AS travel_expenditure
    FROM accommodation a
    JOIN inbound_expenditure e
        ON a.country = e.country
        AND a.year = e.year
    WHERE e.expenditure_type = 'Travel'
      AND e.value IS NOT NULL
      AND a.guests IS NOT NULL
      AND a.overnights IS NOT NULL
),

country_avg AS (
    SELECT
        country,
        AVG(length_of_stay) AS avg_length_of_stay,
        AVG(travel_expenditure) AS avg_annual_travel_expenditure,
        COUNT(*) AS years_with_data
    FROM country_data
    GROUP BY country
    HAVING COUNT(*) >= 5
)

SELECT
    COUNT(*) AS countries,
    CORR(
        avg_length_of_stay,
        avg_annual_travel_expenditure
    ) AS correlation
FROM country_avg;