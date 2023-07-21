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
        const query = `
            SELECT d.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name
            FROM dept_manager m LEFT JOIN
            employees e on m.emp_no = e.emp_no left join
            departments d on d.dept_no = m.dept_no
        `;

        connection.query(query, [emp_no], (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
            }

            console.log('The data from managers table are: \n', rows);
        });
    });
});

//read emp by id
router.get('/:dept_no', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;
        const query = `
            SELECT d.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name
            FROM dept_manager m
            LEFT JOIN employees e ON m.emp_no = e.emp_no
            LEFT JOIN departments d ON d.dept_no = m.dept_no
            WHERE m.dept_no = ?
        `;

        connection.query(query, [req.params.dept_no], (err, rows) => {
            connection.release();

            if (!err) {
                res.send(rows);
            } else {
                console.log(err);
            }

            console.log('The data from managers table are: \n', rows);
        });
    });
});

router.post('/', (req, res) => {
    const { emp_no, dept_no } = req.body;

    if (!emp_no || !dept_no) {
        return res.status(400).json({ message: 'Employee number and department number are required.' });
    }

    pool.getConnection((err, connection) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ message: 'Database connection error.' });
        }

        const query = 'INSERT INTO dept_manager (emp_no, dept_no) VALUES (?, ?)';
        connection.query(query, [emp_no, dept_no], (err, result) => {
            connection.release();

            if (err) {
                console.error(err);
                return res.status(500).json({ message: 'Error adding data to dept_manager.' });
            }

            res.status(201).json({ message: 'Data added to dept_manager successfully.' });
        });
    });
});

// DELETE dept_manager by emp_no and dept_no
router.delete('/:emp_no/:dept_no', (req, res) => {
    const emp_no = req.params.emp_no;
    const dept_no = req.params.dept_no;

    pool.getConnection((err, connection) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ message: 'Database connection error.' });
        }

        const query = 'DELETE FROM dept_manager WHERE emp_no = ? AND dept_no = ?';
        connection.query(query, [emp_no, dept_no], (err, result) => {
            connection.release();

            if (err) {
                console.error(err);
                return res.status(500).json({ message: 'Error deleting data from dept_manager.' });
            }

            if (result.affectedRows === 0) {
                return res.status(404).json({ message: 'Data not found in dept_manager.' });
            }

            res.status(200).json({ message: 'Data deleted from dept_manager successfully.' });
        });
    });
});

module.exports = router;