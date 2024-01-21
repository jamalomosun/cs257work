-- Find all of the earthquakes with a high magnitude between 0 and 90 latitude ordered by location
SELECT * FROM earthquakes WHERE magnitude BETWEEN 5 AND 10 AND latitude BETWEEN 0 AND 90
ORDER BY place DESC;

-- Find all of the earthquakes between 5 and 25 quaketime and between 0 and 120 longitude and between 45 and 90 latitude ordered by magnitude
SELECT * FROM earthquakes WHERE extract(hour from quaketime) BETWEEN 5 AND 25
INTERSECT
SELECT * FROM earthquakes WHERE longitude BETWEEN 0 AND 120 AND latitude BETWEEN 45 AND 90
ORDER BY magnitude DESC;

-- Find earthquakes between 3 and 8 magnitude ordered by quaketime
SELECT * FROM earthquakes WHERE magnitude BETWEEN 3 AND 8 ORDER BY quaketime DESC;
