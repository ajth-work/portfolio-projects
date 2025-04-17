SELECT location, AVG(employees)
FROM startups 
GROUP BY location
HAVING AVG(employees) > 500;