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

// Get all emp
router.get('/', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;
        connection.query('SELECT * from employees', (err, rows) => {
            connection.release(); // return the connection to the pool

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
            }

            console.log('The data from employees table are: \n', rows);
        });
    });
});

//read emp by id
router.get('/:emp_no', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;
        connection.query('SELECT * FROM employees WHERE emp_no = ?', [req.params.emp_no], (err, rows) => {
            connection.release(); // return the connection to the pool

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
            }

            console.log('The data from employees table are: \n', rows);
        });
    });
});

module.exports = router