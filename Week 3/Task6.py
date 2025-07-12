//Weather Observation Station 3 : Query a list of CITY names from STATION for cities that have an even ID number
SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2) = 0;

