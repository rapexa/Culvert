CREATE DATABASE CulvertDB CHARACTER SET utf8;
CREATE USER 'CulvertUser'@'localhost' IDENTIFIED BY 'CulvertPass';
GRANT ALL PRIVILEGES ON CulvertDB.* TO 'CulvertUser'@'localhost';