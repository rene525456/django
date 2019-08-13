# django

create database bd_cooperativa
use bd_cooperativa
CREATE USER 'cooperativa'@'localhost' IDENTIFIED BY 'cooperativa';
GRANT ALL PRIVILEGES ON bd_cooperativa.* TO 'cooperativa'@'localhost';
FLUSH PRIVILEGES

