-- Selecting all columns from the trips table
SELECT *
FROM trips;

-- Selecting all columns from the riders table
SELECT *
FROM riders;

-- Selecting all columns from the cars table
SELECT *
FROM cars;

-- Selecting riders first and last names along with car model from the riders and cars tables
SELECT riders.first,
  riders.last,
  cars.model
FROM riders, cars;

-- Selecting all columns from the trips table and joining with the riders table on rider_id
SELECT *
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;

-- Selecting all columns from the trips table and joining with the cars table on car_id
SELECT *
FROM trips
INNER JOIN cars
  ON trips.car_id = cars.id;

-- Selecting all columns from the riders table and creating a union with all columns in the riders2 table
SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

-- Producing the rounded average cost of trips from the trips table
SELECT ROUND(AVG(cost), 2)
FROM trips;

-- Selecting all riders from the riders table who have taken less than 500 trips
SELECT *
FROM riders
WHERE total_trips < 500;

-- Selecting all riders, with a union between the riders and riders2 tables, of those riders who have taken less than 500 trips
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

-- Producing the count of active status cars in the cars table
SELECT count(status)
FROM cars
WHERE status = "active";

-- Selecting the top 2 cars with the most completed trips
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;