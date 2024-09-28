CREATE DATABASE IF NOT EXISTS cleanarch;

CREATE TABLE IF NOT EXISTS `cleanarch`.`users` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age BIGINT NOT NULL,
    primary key (id)
);
