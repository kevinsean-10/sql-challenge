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

// DA1
router.get('/', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;
        connection.query('SELECT * from departments', (err, rows) => {
            connection.release(); // return the connection to the pool

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
            }

            console.log('The data from departments table are: \n', rows);
        });
    });
});

//read dept by id
router.get('/:dept_no', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;
        connection.query('SELECT * FROM departments WHERE dept_no = ?', [req.params.dept_no], (err, rows) => {
            connection.release(); // return the connection to the pool

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
            }

            console.log('The data from departments table are: \n', rows);
        });
    });
});

module.exports = router