-- Create A Table 1

create table project.user1(
id int primary key auto_increment,
name varchar(40)not null ,
email varchar(40),
gender varchar(6)
);

select * from project.user1;

insert into project.user1(name,email,gender) values('mohan','m@gmmail.com','male');
insert into project.user1(name,email,gender) values('kala','k@gmmail.com','female');
insert into project.user1(name,email,gender) values('sai','s@gmmail.com','male');
insert into project.user1(name,email,gender) values('vasavi','v@gmmail.com','female');


-- Create A Table 2

create table project.useraddress(
door_no varchar(10),
street varchar(35),
area varchar(35),
city varchar(30),
district varchar(15),
state varchar(15),
country varchar(20),
userid int,
foreign key(userid) references user1(id)
);

select*from project.useraddress;
insert into project.useraddress(door_no,street,area,city,district,state,country,userid) values(123, 'jio Tower', 'graddagunta', 'Naidupet', 'Tirupati', 'Andhrapradesh', 'India',1), (131, 'Agraharapet', 'Naidupet', 'Naidupet', 'Tirupati', 'Andhrapradesh', 'India',2), (103, 'Andhrabank road', 'KPHB Colony', 'Hyderabad', 'Hyderabad', 'Telangana', 'India',3);

-- Create A Joins Tables  

SELECT * FROM project.user1 AS t1
INNER JOIN project.useraddress AS t2 ON t1.id = t2.userid;

SELECT * FROM project.user1 AS t1
LEFT JOIN project.useraddress AS t2 ON t1.id = t2.userid;

SELECT * FROM project.user1 AS t1
RIGHT JOIN project.useraddress AS t2 ON t1.id = t2.userid;

SELECT * FROM project.user1
CROSS JOIN project.useraddress;