/*Weather Observation Station 5 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths*/

  (
  SELECT CITY, LENGTH(CITY) AS NAME_LENGTH
  FROM STATION
  ORDER BY LENGTH(CITY) ASC, CITY ASC
  LIMIT 1
)
UNION
(
  SELECT CITY, LENGTH(CITY) AS NAME_LENGTH
  FROM STATION
  ORDER BY LENGTH(CITY) DESC, CITY ASC
  LIMIT 1
);

