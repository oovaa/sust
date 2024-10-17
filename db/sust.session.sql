CREATE TABLE IF NOT EXISTS student(
    student_id INT,
    email VARCHAR(45),
    password VARCHAR(45),
    fname VARCHAR(45),
    lname VARCHAR(45),
    dod Date,
    phone VARCHAR(45),
    mobile VARCHAR(45),
    date_of_join DATE,
    status BOOLEAN,
    last_login_date DATE,
    last_login_ip VARCHAR(45),
    PRIMARY KEY(student_id)
);

CREATE TABLE IF NOT EXISTS course(
    course_id INT PRIMARY KEY,
    name VARCHAR(45),
    description VARCHAR(45)
    
);

CREATE TABLE IF NOT EXISTS exam(
    exam_id INT PRIMARY KEY,
    name VARCHAR(45),
    start_date DATE
);

CREATE TABLE IF NOT EXISTS exam_result(
    exam_id INT,
    student_id INT,
    course_id INT,
    marks INT,
    FOREIGN KEY (exam_id) REFERENCES exam(exam_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

INSERT INTO student (student_id, email, password, fname, lname, dod, phone, mobile, date_of_join, status, last_login_date, last_login_ip) VALUES
(1, 'john@example.com', 'pass123', 'John', 'Doe', '1990-01-01', '1234567890', '0987654321', '2020-09-01', TRUE, '2023-10-01', '192.168.1.1'),
(2, 'jane@example.com', 'pass456', 'Jane', 'Smith', '1992-02-02', '2345678901', '1987654321', '2021-09-01', TRUE, '2023-10-02', '192.168.1.2'),
(3, 'alice@example.com', 'pass789', 'Alice', 'Jones', '1994-03-03', '3456789012', '2987654321', '2022-09-01', TRUE, '2023-10-03', '192.168.1.3');

INSERT INTO course (course_id, name, description) VALUES
(1, 'Mathematics', 'Basic Mathematics Course'),
(2, 'Physics', 'Basic Physics Course'),
(3, 'Chemistry', 'Basic Chemistry Course');

INSERT INTO exam (exam_id, name, start_date) VALUES
(1, 'Midterm Exam', '2023-10-10'),
(2, 'Final Exam', '2023-12-15'),
(3, 'Quiz', '2023-11-05');


INSERT INTO exam_result (exam_id, student_id, course_id, marks) VALUES
(1, 1, 1, 85),
(1, 2, 2, 90),
(1, 3, 3, 88),
(2, 1, 1, 75),
(2, 2, 2, 80),
(2, 3, 3, 78),
(3, 1, 1, 95),
(3, 2, 2, 85),
(3, 3, 3, 92);


SELECT s.fname, s.lname, c.name AS course_name, er.marks
FROM exam_result er
JOIN student s ON er.student_id = s.student_id
JOIN course c ON er.course_id = c.course_id
JOIN exam e ON er.exam_id = e.exam_id
WHERE e.name = 'Final Exam';

SELECT * FROM student;
SELECT * FROM course;
SELECT * FROM exam;
SELECT * FROM exam_result;