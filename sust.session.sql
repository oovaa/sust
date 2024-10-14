CREATE TABLE IF NOT EXISTS exams(
exam_id int,
name VARCHAR(45),
start_date Date    
) ;

INSERT into exams (exam_id, name, start_date) VALUES (1, 'arabic', '2023-12-12');

SELECT * FROM exams;INSERT INTO exams (exam_id, name, start_date)
VALUES (
    exam_id:int,
    'name:varchar',
    'start_date:date'
  );