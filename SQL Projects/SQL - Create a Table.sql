-- Create a table named "friends" with three columns: id, name, and birthday
CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

-- Insert a row into the table
INSERT INTO friends (id, name, birthday)
VALUES (1, "Ororo Munroe", "1940-05-30");

INSERT INTO friends (id, name, birthday)
VALUES (2, "Gregory Currency", "1994-02-01");

INSERT INTO friends (id, name, birthday)
VALUES (3, "Julio Smith", "1994-07-31");

-- Update name for a specific row in the table
-- This will change the name of the friend with id 1 to "Storm"
UPDATE friends
SET name = "Storm"
WHERE id = 1;

-- Add a new column to the table
ALTER TABLE friends
ADD COLUMN email TEXT;

-- Update a specific row in the table
UPDATE friends
SET email = "storm@codecademy.com"
WHERE id = 1;

-- Delete a specific row from the table
DELETE FROM friends
WHERE id = 1;

-- Select all rows from the table
SELECT *
FROM friends;