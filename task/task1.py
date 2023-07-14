from enum import Enum
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host='localhost', port='5433', database='task1', user='postgres',  password='123455', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)


@app.get("/task1/no1")
def get_post():
    cursor.execute('''
    SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
    FROM employees e
    JOIN salaries s
    ON e.emp_no = s.emp_no;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no2")
def get_post():
    cursor.execute('''
    SELECT first_name, last_name, hire_date 
    FROM employees
    WHERE hire_date BETWEEN '1986-1-1' and '1986-12-31'
    ORDER BY hire_date ASC;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no3")
def get_post():
    cursor.execute('''
    SELECT dm.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name 
    FROM dept_manager dm
    JOIN employees e
    ON dm.emp_no = e.emp_no
    JOIN departments d
    ON dm.dept_no = d.dept_no
    ORDER BY d.dept_name ASC;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no4")
def get_post():
    cursor.execute('''
    SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
    FROM employees e
    JOIN dept_emp de 
    ON e.emp_no = de.emp_no
    JOIN departments d
    ON d.dept_no = de.dept_no
    ORDER BY d.dept_name ASC;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no5")
def get_post():
    cursor.execute('''
    SELECT first_name, last_name, sex
    FROM employees 
    WHERE first_name = 'Hercules' AND last_name LIKE 'B%'
    ORDER BY last_name ASC;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no6")
def get_post():
    cursor.execute('''
    SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
    FROM employees e
    JOIN dept_emp de 
    ON e.emp_no = de.emp_no
    JOIN departments d
    ON d.dept_no = de.dept_no
    WHERE d.dept_name = 'Sales';
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no7")
def get_post():
    cursor.execute('''
    SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
    FROM employees e
    JOIN dept_emp de 
    ON e.emp_no = de.emp_no
    JOIN departments d
    ON d.dept_no = de.dept_no
    WHERE d.dept_name = 'Sales' OR d.dept_name = 'Development'
    ORDER BY d.dept_name ASC;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}

@app.get("/task1/no8")
def get_post():
    cursor.execute('''
    SELECT last_name, count(emp_no) as num_employees_with_same_last_name
    FROM employees
    GROUP BY last_name
    ORDER BY num_employees_with_same_last_name DESC;
    ''')
    posts = cursor.fetchall()
    return {"data":posts}