-- Find all of the earthquakes between 3 and 8 and order them by the time they occured descending
SELECT * FROM earthquakes WHERE magnitude BETWEEN 3 AND 8 ORDER BY quaketime DESC;

-- Find all the earthquakes that were between 5 and 10 magnitude and occured between 0 and 90 latitiude and order them by place decending 
SELECT * FROM earthquakes WHERE magnitude BETWEEN 5 AND 10 AND latitude BETWEEN 0 AND 90
ORDER BY place DESC;

-- Find all of the earthquakes between 5 and 25 quaketime and between 0 and 120 longitude and between 45 and 90 latitude ordered by magnitude
>>>>>>> 352ab7a51347b8ece946ec24142cb1d1b935c5ae
SELECT * FROM earthquakes WHERE extract(hour from quaketime) BETWEEN 5 AND 25
INTERSECT
SELECT * FROM earthquakes WHERE longitude BETWEEN 0 AND 120 AND latitude BETWEEN 45 AND 90
ORDER BY magnitude DESC;

