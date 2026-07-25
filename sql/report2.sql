CREATE DATABASE report2;
CREATE TABLE IF NOT EXISTS prefectures(
    prefecture_id INT,
    prefecture_name VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS genders(
    gender_id INT,
    gender_name VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS age(
    age_id INT,
    age_num INT
);

CREATE TABLE IF NOT EXISTS hoken_tokei(
    hoken_tokei_id INT,
    prefecture_id INT,
    age_id INT,
    gender_id INT,
    height_ave FLOAT,
    height_sd FLOAT,
    weight_ave FLOAT,
    weight_sd FLOAT
);
