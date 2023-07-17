'1. Using COUNT, get the number of cities in the USA'
 SELECT COUNT city.Name from city LEFT JOIN country city.CountryCode = country.Code

 SELECT Count(Name)                                 
FROM country 
WHERE Continent="South America"     

'2. Find out the population and life expectancy for people in Argentina.'

    SELECT Population, LifeExpectancy from country WHERE Continent="Argentina";


'3. Using IS NOT NULL, ORDER BY, and LIMIT, which country has the highest life expectancy?'

SELECT Name, MAX(LifeExpectancy) AS MAX_LifeExpectancy
FROM country 
GROUP BY Name 
ORDER BY MAX_LifeExpectancy DESC 
LIMIT 1;

'4. Using JOIN ... ON, find the capital city of Spain.'

-- Used it to get the ID number 
select * from city WHERE Name="Madrid"

-- Shows the capital of Spain using its ID number
SELECT city.Name, country.Name FROM city LEFT JOIN country ON city.CountryCode = country.code WHERE city.ID = 653;

'5. Using JOIN ... ON, list all the languages spoken in the Southeast Asia region.'

SELECT countrylanguage.Language, country.Name FROM countrylanguage LEFT JOIN country ON countrylanguage.CountryCode = country.code WHERE country.Name = "Southeast Asia";

'6. Using a single query, list 25 cities around the world that start with the letter F.'

