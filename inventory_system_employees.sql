use inventory_manager;

drop table employees;

CREATE TABLE employees 
(
  employee_id varchar(4) NOT NULL,
  first_name varchar(45) NOT NULL,
  last_name varchar(45) NOT NULL,
  phone_number varchar(10) DEFAULT NULL,
  dept varchar(45) DEFAULT NULL,
  pass varchar(45) NOT NULL,
  PRIMARY KEY (employee_id));
  
LOCK TABLES employees WRITE;
INSERT INTO employees VALUES ('0001','Ralph','Pura','5555555555','Receiving','password'),('0002','John','Doe','6666666666','Assembly','youtube'),('0003','Jane','Smith','7777777777','Testing','minecraft'),('0004','John','Gibson','8888888888','Shipping','reddit');


UNLOCK TABLES;
