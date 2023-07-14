# dataarchitecture
Hello from Team B! Here's what we've accomplished, please check it out!

## ERD (Data Modeling):
![ERD](https://github.com/skyler288/sql-challenge/blob/main/ERD.png)

## Data Engineering

## Data Analysis
* With Bigquery : https://console.cloud.google.com/bigquery?sq=563744052132:bf71cddf2d154e17b20ec65bab72ab09 
* With PostgreSQL :

## Bonus

## API
* With Node.js (Express) : 
* With FastAPI :

## API Endpoint
**Node.js**
|Endpoint|Method|Body|
|-------|:----:|:---:|
|`/emp`|`GET`|`emp_no`, `emp_title_id`, `birth_date`, `first_name`, `last_name`, `sex`, `hire_date`|
|`/emp/{emp_no}`|`GET`|`emp_no`, `emp_title_id`, `birth_date`, `first_name`, `last_name`, `sex`, `hire_date`|
|`/dep`|`GET`|`dept_no`, `dept_name`|
|`/dep/{dep_no}`|`GET`|`dept_no`, `dept_name`|
|`/da/satu`|`GET`|`emp_no`, `last_name`, `first_name`, `sex`, `salary`|
|`/da/dua`|`GET`|`first_name`, `last_name`, `hire_date`|
|`/da/tiga`|`GET`|`dept_no`, `dept_name`, `emp_no`, `last_name`, `first_name`|
|`/da/empat`|`GET`|`emp_no`, `last_name`, `first_name`,`dept_name`|
|`/da/lima`|`GET`|`first_name`, `last_name`, `sex`, `first_name`,`dept_name`|
|`/da/enam`|`GET`|`emp_no`, `last_name`,  `first_name`, `dept_name`|
|`/da/tujuh`|`GET`|`emp_no`, `last_name`, `first_name`, `dept_name`|
|`/da/delapan`|`GET`|`last_name`, `total_emp`|
