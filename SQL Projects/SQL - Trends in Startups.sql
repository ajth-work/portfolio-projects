-- Creates a table with startups' location and average number of employees, 
-- Grouped by location and having an average greater than 500
SELECT location, AVG(employees)
FROM startups 
GROUP BY location
HAVING AVG(employees) > 500;