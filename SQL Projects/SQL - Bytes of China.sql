-- Create restaurant table
CREATE TABLE restaurant (
  id int PRIMARY KEY,
  name varchar(20),
  description varchar(1000),
  rating decimal,
  telephone char(10),
  hours varchar(100)
);

-- Create address table
CREATE TABLE address (
  id int PRIMARY KEY,
  street_number varchar(10),
  street_name varchar(20),
  city varchar(20),
  state varchar(15),
  google_map_link varchar(50),
  restaurant_id int REFERENCES restaurant(id) UNIQUE
);

-- Create category table
CREATE TABLE category (
  id char(2) PRIMARY KEY,
  name varchar(20),
  description varchar(200)
);

-- Create dish table
CREATE TABLE dish (
  id int PRIMARY KEY,
  name varchar(50),
  description varchar(200),
  hot_and_spicy boolean
);

-- Create review table
CREATE TABLE review (
  id int PRIMARY KEY,
  rating decimal,
  description varchar(100),
  date date,
  restaurant_id int REFERENCES restaurant(id)
);

-- Create categories_dishes table
CREATE TABLE categories_dishes (
  category_id char(2) REFERENCES category(id),
  dish_id int REFERENCES dish(id),
  PRIMARY KEY (category_id, dish_id),
  price money
);

-- Validate restaurant Primary Key
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'restaurant';

-- Validate address Primary Key
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'address';

-- Validate category Primary Key
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'category';

-- Validate dish Primary Key
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'dish';

-- Validate review Primary Key and foreign keys
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'review';

-- Validate categories_dishes keys
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'categories_dishes';

-- INSERT SAMPLE DATA BELOW:

/* 
 *--------------------------------------------
 Insert values for restaurant
 *--------------------------------------------
 */
INSERT INTO restaurant VALUES (
  1,
  'Bytes of China',
  'Delectable Chinese Cuisine',
  3.9,
  '6175551212',
  'Mon - Fri 9:00 am to 9:00 pm, Weekends 10:00 am to 11:00 pm'
);

/* 
 *--------------------------------------------
 Insert values for address
 *--------------------------------------------
 */
INSERT INTO address VALUES (
  1,
  '2020',
  'Busy Street',
  'Chinatown',
  'MA',
  'http://bit.ly/BytesOfChina',
  1
);

/* 
 *--------------------------------------------
 Insert values for review
 *--------------------------------------------
 */
INSERT INTO review VALUES (
  1,
  5.0,
  'Would love to host another birthday party at Bytes of China!',
  '05-22-2020',
  1
);

INSERT INTO review VALUES (
  2,
  4.5,
  'Other than a small mix-up, I would give it a 5.0!',
  '04-01-2020',
  1
);

INSERT INTO review VALUES (
  3,
  3.9,
  'A reasonable place to eat for lunch, if you are in a rush!',
  '03-15-2020',
  1
);

/* 
 *--------------------------------------------
 Insert values for category
 *--------------------------------------------
 */
INSERT INTO category VALUES (
  'C',
  'Chicken',
  null
);

INSERT INTO category VALUES (
  'LS',
  'Luncheon Specials',
  'Served with Hot and Sour Soup or Egg Drop Soup and Fried or Steamed Rice  between 11:00 am and 3:00 pm from Monday to Friday.'
);

INSERT INTO category VALUES (
  'HS',
  'House Specials',
  null
);

/* 
 *--------------------------------------------
 Insert values for dish
 *--------------------------------------------
 */
INSERT INTO dish VALUES (
  1,
  'Chicken with Broccoli',
  'Diced chicken stir-fried with succulent broccoli florets',
  false
);

INSERT INTO dish VALUES (
  2,
  'Sweet and Sour Chicken',
  'Marinated chicken with tangy sweet and sour sauce together with pineapples and green peppers',
  false
);

INSERT INTO dish VALUES (
  3,
  'Chicken Wings',
  'Finger-licking mouth-watering entree to spice up any lunch or dinner',
  true
);

INSERT INTO dish VALUES (
  4,
  'Beef with Garlic Sauce',
  'Sliced beef steak marinated in garlic sauce for that tangy flavor',
  true
);

INSERT INTO dish VALUES (
  5,
  'Fresh Mushroom with Snow Peapods and Baby Corns',
  'Colorful entree perfect for vegetarians and mushroom lovers',
  false
);

INSERT INTO dish VALUES (
  6,
  'Sesame Chicken',
  'Crispy chunks of chicken flavored with savory sesame sauce',
  false
);

INSERT INTO dish VALUES (
  7,
  'Special Minced Chicken',
  'Marinated chicken breast sauteed with colorful vegetables topped with pine nuts and shredded lettuce.',
  false
);

INSERT INTO dish VALUES (
  8,
  'Hunan Special Half & Half',
  'Shredded beef in Peking sauce and shredded chicken in garlic sauce',
  true
);

/*
 *--------------------------------------------
 Insert valus for cross-reference table, categories_dishes
 *--------------------------------------------
 */
INSERT INTO categories_dishes VALUES (
  'C',
  1,
  6.95
);

INSERT INTO categories_dishes VALUES (
  'C',
  3,
  6.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  1,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  4,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  5,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  6,
  15.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  7,
  16.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  8,
  17.95
);

-- Start by selecting all the data from each table to verify the data was inserted correctly
SELECT * FROM restaurant;
SELECT * FROM address;
SELECT * FROM category;
SELECT * FROM dish;
SELECT * FROM review;
SELECT * FROM categories_dishes;

-- Task 10 - Selecting restaurant name, address, and telephone number
SELECT 
  restaurant.name as Restaurant, 
  address.street_number, 
  address.street_name,
  restaurant.telephone as Telephone
FROM restaurant, address;

-- Task 11 - Selecting the best rating from review table
SELECT review.rating as best_rating
FROM review
ORDER BY rating DESC
LIMIT 1;

-- Task 12 - Selecting dishes with their price and category, ordered by dish name
SELECT 
  dish.name as dish_name, 
  categories_dishes.price as price, 
  category.name as category
FROM dish
JOIN categories_dishes on dish.id = categories_dishes.dish_id
JOIN category on categories_dishes.category_id = category.id
ORDER BY dish.name;

-- Task 13 - Selecting dishes with their price and category, ordered by category name
SELECT 
  dish.name as dish_name, 
  categories_dishes.price as price, 
  category.name as category
FROM dish
JOIN categories_dishes on dish.id = categories_dishes.dish_id
JOIN category on categories_dishes.category_id = category.id
ORDER BY category.name;

-- Task 14 - Selecting spicy dishes with their price and category
SELECT 
  dish.name as spicy_dish_name, 
  categories_dishes.price as price, 
  category.name as category
FROM dish
JOIN categories_dishes on dish.id = categories_dishes.dish_id
JOIN category on categories_dishes.category_id = category.id
WHERE dish.hot_and_spicy = TRUE
ORDER BY dish.name;

-- Task 15 - Count the number of dishes in each category and group by dish_id
SELECT categories_dishes.dish_id, COUNT(dish_id) as dish_count
FROM categories_dishes
GROUP BY dish_id;

-- Task 16 - Find dishes that are in more than one category
SELECT categories_dishes.dish_id, COUNT(dish_id) as dish_count
FROM categories_dishes
GROUP BY dish_id
HAVING COUNT(dish_id) > 1;

-- Task 17 - Selecting dishes that are in more than one category, grouped by dish name.
SELECT 
  dish.name as dish_name,
  COUNT(categories_dishes.dish_id) as dish_count 
FROM categories_dishes
JOIN dish on dish.id = categories_dishes.dish_id
GROUP BY dish.name
HAVING COUNT(categories_dishes.dish_id) > 1;

-- Task 18 - Selcting the best rating and description from review table
SELECT 
  rating as best_rating,
  description
FROM review
WHERE rating = (
  SELECT MAX (rating) FROM review
);