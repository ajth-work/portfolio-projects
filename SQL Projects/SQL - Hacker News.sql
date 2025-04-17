
-- Users who have a score greater than 200
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC

-- Add scores and divide by the number of stories to get the percentage
SELECT (517+309+304+282)/6366.0;

-- Find instances of a particular URL
SELECT url, user
FROM hacker_news
WHERE url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

-- Find which sites feed the most stories to Hacker News
SELECT CASE
    WHEN url LIKE "%github.com%" THEN "GitHub"
    WHEN url LIKE "%medium.com%" THEN "Medium"
    WHEN url LIKE "%nytimes.com%" THEN "New York Times"
    ELSE "OTHER"
  END AS "Source",
  COUNT(*) as "Count"
FROM hacker_news
GROUP BY 1;

-- Return time, average score, and number of stories
 SELECT strftime('%H',timestamp),
  AVG(score),
  COUNT(*)
 FROM hacker_news
 GROUP BY 1
 ORDER BY 2 DESC;

-- Use ROUND to round the average score to 2 decimal places
-- Use AS to rename the columns 
-- Filter to where timestamp is not null
SELECT strftime('%H',timestamp),
  ROUND(AVG(score),2) AS "Average Score",
  COUNT(*) as "Number of Stories"
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;