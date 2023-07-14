from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
import time
from uspass import user, password

app = FastAPI()

while True:
    try:
        conn = pg2.connect(database = 'sql-challenge',
                           user= user(),
                           password=password(), 
                           cursor_factory= RealDictCursor)
        cur = conn.cursor()
        print('Database connection was successful.')
        break
    except Exception as error:
        print("Connectiong to database failed.")
        print('Error: ', error)
        time.sleep(2)

@app.get('/')
def root():
    return {"Title": "SQL Challenge",
            "Creator": "Astra Data Management and Achitecture Internship"}

@app.get('/DA1')
def num1():
    cur.execute(
        '''SELECT salaries.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
        FROM employees
        INNER JOIN salaries
        ON salaries.emp_no = employees.emp_no
        ;''')
    answer = cur.fetchall()
    return {"Problem": "List the following details of each employee: employee number, last name, first name, sex, and salary.",
            "Answer": answer}

@app.get('/DA2')
def num2():
    cur.execute(
        '''SELECT first_name, last_name, hire_date FROM employees
        WHERE EXTRACT(YEAR FROM hire_date) = 1986
        ;''')
    answer = cur.fetchall()
    return {"Problem": "List first name, last name, and hire date for employees who were hired in 1986.",
            "Answer": answer}

@app.get('/DA3')
def num3():
    cur.execute(
        '''SELECT departments.dept_no, departments.dept_name, employees.emp_no, employees.last_name, employees.first_name 
        FROM dept_manager
        INNER JOIN employees
        ON employees.emp_no = dept_manager.emp_no
        INNER JOIN departments
        ON departments.dept_no = dept_manager.dept_no;''')
    answer = cur.fetchall()
    return {"Problem": "List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.",
            "Answer": answer}

@app.get('/DA4')
def num4():
    cur.execute(
        '''SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
        FROM dept_emp
        INNER JOIN employees
        ON employees.emp_no = dept_emp.emp_no
        INNER JOIN departments
        ON departments.dept_no = dept_emp.dept_no;''')
    answer = cur.fetchall()
    return {"Problem": "List the department of each employee  with the following information: employee number, last name,  first name, and department name.",
            "Answer": answer}

@app.get('/DA5')
def num5():
    cur.execute(
        '''SELECT * 
        FROM employees
        WHERE first_name = 'Hercules' AND last_name ILIKE 'B%'
        ;''')
    answer = cur.fetchall()
    return {"Problem": 'List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."',
            "Answer": answer}

@app.get('/DA6')
def num6():
    cur.execute(
        '''SELECT dept_emp.emp_no,  employees.last_name, employees.first_name, departments.dept_name
        FROM dept_emp
        INNER JOIN departments
        ON departments.dept_no = dept_emp.dept_no
        INNER JOIN employees
        ON employees.emp_no = dept_emp.emp_no
        WHERE dept_emp.dept_no = 'd007'
        ;''')
    answer = cur.fetchall()
    return {"Problem": "List all employees in the Sales department, including their employee number, last name, first name, and department name.",
            "Answer": answer}

@app.get('/DA7')
def num7():
    cur.execute(
        '''SELECT dept_emp.emp_no,  employees.last_name, employees.first_name, departments.dept_name
        FROM dept_emp
        INNER JOIN departments
        ON departments.dept_no = dept_emp.dept_no
        INNER JOIN employees
        ON employees.emp_no = dept_emp.emp_no
        WHERE dept_emp.dept_no = 'd005' OR dept_emp.dept_no = 'd007'
        ;''')
    answer = cur.fetchall()
    return {"Problem": "List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.",
            "Answer": answer}

@app.get('/DA8')
def num8():
    cur.execute(
        '''SELECT last_name, COUNT(*) AS frequency
        FROM employees
        GROUP BY last_name
        ORDER BY COUNT(*) DESC
        ;''')
    answer = cur.fetchall()
    return {"Problem": "In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.",
            "Answer": answer}

# Display semua employees
@app.get('/employees')
def all_employee():
    cur.execute(
        '''
        DROP VIEW IF EXISTS dept_emp_2;
        CREATE VIEW dept_emp_2 AS
        SELECT employees.emp_no AS emp_no, departments.dept_name AS dept_name
        FROM dept_emp
        INNER JOIN employees
        ON employees.emp_no = dept_emp.emp_no
        INNER JOIN departments
        ON departments.dept_no = dept_emp.dept_no;
        ''')
    conn.commit()
    cur.execute(
        '''
        SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", 
        employees.last_name AS "Last Name", employees.sex AS "Sex", salaries.salary AS "Salary", titles.title AS "Title", dept_emp_2.dept_name AS "Department Name"
        FROM employees
        INNER JOIN salaries
        ON salaries.emp_no = employees.emp_no
        INNER JOIN titles
        ON titles.title_id = employees.emp_title_id
        INNER JOIN dept_emp_2
        ON dept_emp_2.emp_no = employees.emp_no
        '''
    )
    employees = cur.fetchall()
    if not employees:  
        # # cara 1
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Employee dengan id {id} tidak ditemukan.')
    return {"Employees Data": employees}

# Cari employee dengan id 
@app.get('/employees/{id}')
def info_employee(id: int,
                  response: Response):
    cur.execute(
        '''
        DROP VIEW IF EXISTS dept_emp_2;
        CREATE VIEW dept_emp_2 AS
        SELECT employees.emp_no AS emp_no, departments.dept_name AS dept_name
        FROM dept_emp
        INNER JOIN employees
        ON employees.emp_no = dept_emp.emp_no
        INNER JOIN departments
        ON departments.dept_no = dept_emp.dept_no;
        ''')
    conn.commit()
    cur.execute(
        '''
        SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", 
        employees.last_name AS "Last Name", employees.sex AS "Sex", salaries.salary AS "Salary", titles.title AS "Title", dept_emp_2.dept_name AS "Department Name"
        FROM employees
        INNER JOIN salaries
        ON salaries.emp_no = employees.emp_no
        INNER JOIN titles
        ON titles.title_id = employees.emp_title_id
        INNER JOIN dept_emp_2
        ON dept_emp_2.emp_no = employees.emp_no
        WHERE employees.emp_no = %s
        ''',
        (str(id),)
    )
    employee = cur.fetchone()
    if not employee:  
        # # cara 1
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Employee dengan id {id} tidak ditemukan.')
    return {"Employees Data": employee}

# Display semua data managers
@app.get('/managers')
def all_manager():
    cur.execute(
        '''
        DROP VIEW IF EXISTS dept_manager_2;
        CREATE VIEW dept_manager_2 AS
        SELECT departments.dept_name , employees.emp_no AS emp_no
        FROM dept_manager
        INNER JOIN employees
        ON employees.emp_no = dept_manager.emp_no
        INNER JOIN departments
        ON departments.dept_no = dept_manager.dept_no;
        ''')
    conn.commit()
    cur.execute(
        '''
        SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", employees.last_name  AS "Last Name", employees.sex AS "Sex", 
        salaries.salary AS Salary, titles.title AS Title, dept_manager_2.dept_name AS "Departement Name"
        FROM employees
        INNER JOIN salaries
        ON salaries.emp_no = employees.emp_no
        INNER JOIN titles
        ON titles.title_id = employees.emp_title_id
        INNER JOIN dept_manager_2
        ON dept_manager_2.emp_no = employees.emp_no
        '''
    )
    managers = cur.fetchall()
    if not managers:  
        # # cara 1
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Manager dengan id {id} tidak ditemukan.')
    return {"Managers Data": managers}

# cari manager dengan id
@app.get('/managers/{id}')
def info_manager(id: int,
                  response: Response):
    cur.execute(
        '''
        DROP VIEW IF EXISTS dept_manager_2;
        CREATE VIEW dept_manager_2 AS
        SELECT departments.dept_name , employees.emp_no AS emp_no
        FROM dept_manager
        INNER JOIN employees
        ON employees.emp_no = dept_manager.emp_no
        INNER JOIN departments
        ON departments.dept_no = dept_manager.dept_no;
        ''')
    conn.commit()
    cur.execute(
        '''
        SELECT employees.emp_no AS "ID", employees.first_name AS "First Name", employees.last_name  AS "Last Name", employees.sex AS "Sex", 
        salaries.salary AS Salary, titles.title AS Title, dept_manager_2.dept_name AS "Departement Name"
        FROM employees
        INNER JOIN salaries
        ON salaries.emp_no = employees.emp_no
        INNER JOIN titles
        ON titles.title_id = employees.emp_title_id
        INNER JOIN dept_manager_2
        ON dept_manager_2.emp_no = employees.emp_no
        WHERE employees.emp_no = %s
        ''',
        (str(id),)
    )
    manager = cur.fetchone()
    if not manager:  
        # # cara 1
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Manager dengan id {id} tidak ditemukan.')
    return {"Manager Data": manager}

