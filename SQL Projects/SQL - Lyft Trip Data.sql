SELECT *
FROM trips;
-- Primary Key of Trips is "id" in Trips table

SELECT *
FROM riders;
-- Primary Key of Riders is "id" or the foreign key "rider_id" in Trips table

SELECT *
FROM cars;
-- Primary Key of Cars is "id" or the foreign key "car_id" in Trips table

SELECT riders.first,
  riders.last,
  cars.model
FROM riders, cars;

SELECT *
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;


SELECT *
FROM trips
INNER JOIN cars
  ON trips.car_id = cars.id;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT ROUND(AVG(cost), 2)
FROM trips;

SELECT *
FROM riders
WHERE total_trips < 500;

SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

SELECT count(status)
FROM cars
WHERE status = "active";

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;