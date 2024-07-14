# sql/postsql

## database

- an organized collection of data
- gives us a mothid of accessing and manipulating the data

examples:
- flat files, like excel
- document model databases (NoSQL) -> documents iso tables
- Relation Databases -> Oracle, MySQL, SQLServer, PostSQL

Relation database
- data is stored in tables
- tables can be linked together

## SQL: structured query language

language for talking to retional databases
create tables, insert data, retrieve data

Tables
- column (fields)
    - data type (integer, string, etc) 
        - id integer (primary key) 
        - first_name/last_name/city: var char (30)
        - char
- rows of fata (records)
    - should be unique

Relational Database: link tables

## Data Types

Numeric Data types:
- INT: store while numbers
- NUMERIC(P,S): 1.79, 45,789 -> p=5 (total digit), s=3 (after the .)
- serial: auto increment (primary key)

String Data types:
- CHAR(N): fixed length string of length N
- VARCHAR(N): var length string of max length of N
- TEXT: var length string with no max length

Time data types:
- TIME HH:MM:SS
- DATE YYYY-MM-DD
- TIMESTAMP YYYY-MM-DD HH:MM:SS

other data types:
- BOOLEAN: true or False
- ENUM: list of values input by the user -> user creates a list of values

## Primary Keys, Foreign Keys

Primary key: 
- column or combination
- Must be unique and cannot be null
- Only 1 primary key

Foreign Key:
- used to link 2 tables together
- a column where the values match the values of another tables primary key column
- table with primary key is called the reference, or parent table
- table with the foreign key is called the chile table
- A table can contain multiple foreign keys

## constraints

Unique constraint -> e.g. email address -> every email must be unique
Not NULL constraint -> data must exist
Check constaint -> satisfy a specific boolean expression

## create tables

-- Database: movie_data

-- DROP DATABASE IF EXISTS movie_data;

CREATE DATABASE movie_data
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- create the directors table

CREATE TABLE directors (
	director_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30) NOT NULL,
	date_of_birth DATE,
	nationality VARCHAR(20)
);

SELECT * FROM directors;

-- create the actors table

CREATE TABLE actors (
	actor_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	gender CHAR(1),
	date_of_birth DATE
);

SELECT * FROM actors;

-- create the movies table (with a foreign key)

CREATE TABLE movies (
	movie_id SERIAL PRIMARY KEY,
	movie_name VARCHAR(50) NOT NULL,
	movie_length INT,
	movie_lang VARCHAR(20),
	release_date DATE,
	age_certificate VARCHAR(5),
	director_id INT REFERENCES directors (director_id)
);

SELECT * FROM movies;

-- create the movie_revenues table (with a foreign key)

CREATE TABLE movie_revenues (
	revenue_id SERIAL PRIMARY KEY,
	movie_id INT REFERENCES movies (movie_id),
	domestic_takings NUMERIC(6,2),
	international_takings NUMERIC(6,2)
);

SELECT * FROM movie_revenues;

-- create the movies_actors table (junction table)

CREATE TABLE movie_actors (
	movie_id INT REFERENCES movies (movie_id),
	actor_id INT REFERENCES actors (actor_id),
	PRIMARY KEY (movie_id, actor_id)
);

SELECT * FROM movie_actors;


## modifying tables

-- Database: test

-- DROP DATABASE IF EXISTS test;

CREATE DATABASE test
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- modifying tables and add a column

CREATE TABLE examples (
	example_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30)
);


SELECT * FROM examples;

ALTER TABLE examples 
ADD COLUMN email VARCHAR(50) UNIQUE;

ALTER TABLE examples 
ADD COLUMN nationality VARCHAR(30),
ADD COLUMN age INT NOT NULL;

-- modify data type

ALTER TABLE examples 
ALTER COLUMN nationality TYPE CHAR(3);

-- modify multiple data type at once

ALTER TABLE examples 
ALTER COLUMN last_name TYPE VARCHAR(50),
ALTER COLUMN email TYPE VARCHAR(80);

-- deleting tables from a database

CREATE TABLE practice (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	price NUMERIC(4,2)
);

SELECT * FROM practice;

DROP TABLE practice;

## Examples:

-- 1.Create a new database called owners_pets

-- 2. Create the owners table

CREATE TABLE owners (

	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	city VARCHAR(30),
	state CHAR(2)
);

SELECT * FROM owners;

-- 3. Create the pets table (with a foreign key)

CREATE TABLE pets (

	id SERIAL PRIMARY KEY, 
	species VARCHAR(30),
	full_name VARCHAR(30),
	age INT, 
	owner_id INT REFERENCES owners(id)
);

SELECT * FROM pets;

-- 4. Add an email column to the owners table

ALTER TABLE owners
ADD COLUMN email VARCHAR(50) UNIQUE;

SELECT * FROM owners;

-- 5. Change the data type of the last_name column in the owners table to VARCHAR(50).

ALTER TABLE owners
ALTER COLUMN last_name TYPE VARCHAR(50);

SELECT * FROM owners;

## Data manipulation

insert, update, delete data in tables

### INSERT

INSERT INTO examples (first_name, last_name, email, nationality, age)
VALUES ('David','Mitchell','dmitch@gmaial.com','GBR',43);

INSERT INTO examples (first_name, last_name, email, nationality, age)
VALUES ('Emily','Watson','ewatson@gmaial.com','USA',29),
	('Theo','Scott','tscott@gmail.com','AUS',33),
	('Emily','Smith','esmith@gmail.com','GBR',29),
	('Jim','Burr','jburr@gmail.com','USA',54);

-> string single or double quotes
-> int: no qoutes

SELECT * FROM examples;

### UPDATE

UPDATE examples
SET email = 'david.mitchel@gmail.com'
WHERE example_id = 1;

UPDATE examples
SET nationality = 'CAN'
WHERE nationality = 'USA';

UPDATE examples
SET first_name = 'James', age=55
WHERE example_id = 5;

### DELETE

/*
DELETE FROM tablename
WHERE columnname = 'value';
*/

DELETE FROM examples
WHERE example_id = 2;

DELETE FROM examples
WHERE nationality = 'GBR';

-> delete all data
DELETE FROM examples;

## RETRIEVE DATA FROM A TABLE

SELECT * FROM directors;

SELECT first_name FROM directors;

SELECT first_name, last_name FROM directors;

### WHERE clause

SELECT * FROM movies
WHERE age_certificate = '15';

-> AND

SELECT * FROM movies
WHERE age_certificate = '15'
AND movie_lang = 'Chinese';

-> OR

SELECT * FROM movies
WHERE age_certificate = '15'
OR movie_lang = 'Chinese';

SELECT * FROM movies
WHERE age_certificate = '15'
AND movie_lang = 'English'
AND director_id = 27;

#### LOGICAL OPERATORS

-> logical operators: >, >=, <, <=
works for integers and dates

SELECT movie_name, movie_length FROM movies
WHERE movie_length > 120;

-> data example

SELECT * FROM movies
WHERE release_date > '1999-12-31';