-- test02.sql
DROP TABLE IF EXISTS test02;
CREATE TABLE test02 (
  id INT,
  text VARCHAR(10),
  sum INT
);
INSERT INTO test02 VALUES
  (0, 'zero', 0),
  (1, 'one', 1),
  (2, 'two', 3),
  (3, 'three', 6),
  (4, 'four', 10);
SELECT * FROM test02;
UPDATE test02 SET text = 'small' WHERE id < 2;
UPDATE test02 SET text = 'big' WHERE id > 2;
SELECT * FROM test02;