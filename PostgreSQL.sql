-- -- create titles table
-- CREATE TABLE titles (
-- 	title_id varchar(5) PRIMARY KEY,
-- 	title varchar(30)
-- );

-- -- create employees table
-- CREATE TABLE employees (
-- 	emp_no varchar(10) PRIMARY KEY,
-- 	emp_title_id varchar(5) references titles(title_id),
-- 	birth_date date,
-- 	first_name varchar(45),
-- 	last_name varchar(45), 
-- 	sex varchar(1),
-- 	hire_date date
-- );

-- -- create departments table
-- CREATE TABLE departments (
-- 	dept_no varchar(5) PRIMARY KEY,
-- 	dept_name varchar(30)
-- );

-- -- create department managers table
-- CREATE TABLE dept_manager (
-- 	dept_no varchar(5) references departments(dept_no),
-- 	emp_no varchar(10) references employees(emp_no)
-- );

-- -- create department employees table
-- CREATE TABLE dept_emp (
-- 	emp_no varchar(10) references employees(emp_no),
-- 	dept_no varchar(5) references departments(dept_no)
-- );

-- -- create salaries table
-- CREATE TABLE salaries (
-- 	emp_no varchar(10) references employees(emp_no),
-- 	salary int
-- );

-- SET datestyle = 'ISO, MDY';

-- COPY salaries
-- FROM 'D:\OneDrive - Institut Teknologi Bandung\[NONAKADEMIK]\Internship\Astra\Data Management\Challenge\sql-challenge-main\EmployeeSQL\data\salaries.csv'
-- DELIMITER ','
-- CSV HEADER;

-- COPY employees
-- FROM 'D:\OneDrive - Institut Teknologi Bandung\[NONAKADEMIK]\Internship\Astra\Data Management\Challenge\sql-challenge-main\EmployeeSQL\data\employees.csv'
-- DELIMITER ','
-- CSV HEADER;

-- COPY titles
-- FROM 'D:\OneDrive - Institut Teknologi Bandung\[NONAKADEMIK]\Internship\Astra\Data Management\Challenge\sql-challenge-main\EmployeeSQL\data\titles.csv'
-- DELIMITER ','
-- CSV HEADER;

-- COPY dept_employees
-- FROM 'D:\OneDrive - Institut Teknologi Bandung\[NONAKADEMIK]\Internship\Astra\Data Management\Challenge\sql-challenge-main\EmployeeSQL\data\dept_employees.csv'
-- DELIMITER ','
-- CSV HEADER;

-- COPY departments
-- FROM 'D:\OneDrive - Institut Teknologi Bandung\[NONAKADEMIK]\Internship\Astra\Data Management\Challenge\sql-challenge-main\EmployeeSQL\data\departments.csv'
-- DELIMITER ','
-- CSV HEADER;

-- COPY dept_manager
-- FROM 'D:\OneDrive - Institut Teknologi Bandung\[NONAKADEMIK]\Internship\Astra\Data Management\Challenge\sql-challenge-main\EmployeeSQL\data\dept_manager.csv'
-- DELIMITER ','
-- CSV HEADER;

-- 1
SELECT salaries.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
FROM employees
INNER JOIN salaries
ON salaries.emp_no = employees.emp_no
;

-- 2
SELECT first_name, last_name, hire_date FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 1986
;

-- 3
SELECT departments.dept_no, departments.dept_name AS "Department Name", employees.emp_no, employees.last_name, employees.first_name 
FROM dept_manager
INNER JOIN employees
ON employees.emp_no = dept_manager.emp_no
INNER JOIN departments
ON departments.dept_no = dept_manager.dept_no;

-- 4
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
INNER JOIN employees
ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments
ON departments.dept_no = dept_emp.dept_no
;

-- 5
SELECT * 
FROM employees
WHERE first_name = 'Hercules' AND last_name ILIKE 'B%'
;

-- 6
SELECT dept_emp.emp_no,  employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
INNER JOIN departments
ON departments.dept_no = dept_emp.dept_no
INNER JOIN employees
ON employees.emp_no = dept_emp.emp_no
WHERE dept_emp.dept_no = 'd007'
;

-- 7
SELECT dept_emp.emp_no,  employees.last_name, employees.first_name, departments.dept_name
FROM dept_emp
INNER JOIN departments
ON departments.dept_no = dept_emp.dept_no
INNER JOIN employees
ON employees.emp_no = dept_emp.emp_no
WHERE dept_emp.dept_no = 'd005' OR dept_emp.dept_no = 'd007'
;

-- 8
SELECT last_name, COUNT(*) AS frequency
FROM employees
GROUP BY last_name
ORDER BY COUNT(*) DESC
;

-- BONUS
SELECT titles.title_id, titles.title AS Title, ROUND(AVG(salaries.salary),2) AS "Average Salary"
FROM salaries
INNER JOIN employees
ON salaries.emp_no = employees.emp_no
INNER JOIN titles
ON titles.title_id = employees.emp_title_id
GROUP BY titles.title_id;

-- other
DROP VIEW IF EXISTS dept_emp_2;
CREATE VIEW dept_emp_2 AS
SELECT employees.emp_no AS emp_no, departments.dept_name AS dept_name
FROM dept_emp
INNER JOIN employees
ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments
ON departments.dept_no = dept_emp.dept_no;
SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", 
employees.last_name AS "Last Name", employees.sex AS "Sex", salaries.salary AS "Salary", titles.title AS "Title", dept_emp_2.dept_name AS "Department Name"
FROM employees
INNER JOIN salaries
ON salaries.emp_no = employees.emp_no
INNER JOIN titles
ON titles.title_id = employees.emp_title_id
INNER JOIN dept_emp_2
ON dept_emp_2.emp_no = employees.emp_no;

DROP VIEW IF EXISTS dept_emp_2;
CREATE VIEW dept_emp_2 AS
SELECT employees.emp_no AS emp_no, departments.dept_name AS dept_name
FROM dept_emp
INNER JOIN employees
ON employees.emp_no = dept_emp.emp_no
INNER JOIN departments
ON departments.dept_no = dept_emp.dept_no;
SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", 
employees.last_name AS "Last Name", employees.sex AS "Sex", salaries.salary AS "Salary", titles.title AS "Title", dept_emp_2.dept_name AS "Department Name"
FROM employees
INNER JOIN salaries
ON salaries.emp_no = employees.emp_no
INNER JOIN titles
ON titles.title_id = employees.emp_title_id
INNER JOIN dept_emp_2
ON dept_emp_2.emp_no = employees.emp_no
WHERE employees.emp_no = '10044'
;

DROP VIEW IF EXISTS dept_manager_2;
CREATE VIEW dept_manager_2 AS
SELECT departments.dept_name , employees.emp_no AS emp_no
FROM dept_manager
INNER JOIN employees
ON employees.emp_no = dept_manager.emp_no
INNER JOIN departments
ON departments.dept_no = dept_manager.dept_no;

SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", employees.last_name  AS "Last Name", employees.sex AS "Sex", 
salaries.salary AS Salary, titles.title AS Title, dept_manager_2.dept_name AS "Departement Name"
FROM employees
INNER JOIN salaries
ON salaries.emp_no = employees.emp_no
INNER JOIN titles
ON titles.title_id = employees.emp_title_id
INNER JOIN dept_manager_2
ON dept_manager_2.emp_no = employees.emp_no
WHERE employees.emp_no = '110022'
;
