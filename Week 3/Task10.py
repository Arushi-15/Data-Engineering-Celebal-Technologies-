//Average Population : Query the average population for all cities in CITY, rounded down to the nearest integer
SELECT co.CONTINENT, FLOOR(AVG(ci.POPULATION))
FROM CITY ci, COUNTRY co
WHERE ci.COUNTRYCODE = co.CODE
GROUP BY co.CONTINENT;
