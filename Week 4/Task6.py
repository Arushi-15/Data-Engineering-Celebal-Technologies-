/*African Cities : Query the names of all cities where the CONTINENT is 'Africa'.*/
SELECT ci.NAME
FROM CITY ci, COUNTRY co
WHERE ci.COUNTRYCODE = co.CODE
  AND co.CONTINENT = 'Africa';


