/*Weather Observation Station 19 : Query the Euclidean Distance between points and and format your answer to display decimal digits.
*/
  SELECT 
  CAST(
    SQRT(
      POWER(MAX(LAT_N) - MIN(LAT_N), 2) + 
      POWER(MAX(LONG_W) - MIN(LONG_W), 2)
    ) 
  AS DECIMAL(10, 4)) 
AS DISTANCE
FROM STATION;

