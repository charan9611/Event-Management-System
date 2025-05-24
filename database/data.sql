
CREATE DATABASE demo;
USE demo;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user VARCHAR(25),
    email VARCHAR(50) UNIQUE,
    phone_number VARCHAR(15),
    address VARCHAR(100),
    password VARCHAR(255) 
);


Create TABLE booking(
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_type varchar(15),
    event_date varchar(15),
    venue varchar(25),
    guests INT,
    name varchar(25),
    email varchar(25)
);

Create TABLE contact(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25),
    number VARCHAR(10),
    email VARCHAR(25),
    message varchar(25)
);





