const express = require('express')
const router = express.Router()
const mysql = require('mysql')

// MySQL connection setup
const pool = mysql.createPool({
    connectionLimit: 10,
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE,
});

//DA 1
router.get('/satu', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
            SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
            FROM employees e LEFT
            JOIN salaries s ON e.emp_no = s.emp_no
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 1: \n', rows);
        });
    });
});

//DA 2
router.get('/dua', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
            SELECT first_name, last_name, hire_date
            FROM employees
            WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31'
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 2: \n', rows);
        });
    });
});

//DA 3
router.get('/tiga', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
            SELECT d.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name
            FROM dept_manager m LEFT JOIN
            employees e on m.emp_no = e.emp_no left join
            departments d on d.dept_no = m.dept_no
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 3: \n', rows);
        });
    });
});

//DA 4
router.get('/empat', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
        SELECT 	e.emp_no, last_name, first_name, dept_name
        FROM employees e LEFT JOIN 
        dept_emp de on e.emp_no = de.emp_no LEFT JOIN
        departments d on d.dept_no = de.dept_no
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 4: \n', rows);
        });
    });
});

//DA 5
router.get('/lima', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
        SELECT first_name, last_name, sex
        FROM employees
        WHERE first_name = 'Hercules' and last_name like 'B%';
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 5: \n', rows);
        });
    });
});

//DA 6
router.get('/enam', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
            SELECT e.emp_no, last_name, first_name, dept_name
            FROM employees e left join
            dept_emp de on e.emp_no = de.emp_no left join
            departments d on d.dept_no = de.dept_no
            WHERE dept_name = 'Sales'
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 6: \n', rows);
        });
    });
});

//DA 7
router.get('/tujuh', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
            SELECT e.emp_no, last_name, first_name, dept_name
            FROM employees e left join
            dept_emp de on e.emp_no = de.emp_no left join
            departments d on d.dept_no = de.dept_no
            WHERE dept_name = 'Sales' or dept_name = 'Development'
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 7: \n', rows);
        });
    });
});

//DA 8
router.get('/delapan', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        const query = `
            SELECT last_name, count(emp_no) as total_emp
            FROM employees
            GROUP BY last_name
            ORDER BY total_emp desc;
        `;

        connection.query(query, (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
                res.status(500).send('Internal Server Error');
            }

            console.log('Answer of DA 8: \n', rows);
        });
    });
});

module.exports = router