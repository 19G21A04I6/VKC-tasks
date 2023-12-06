create schema `project`;
use  `project`;

create table project.`task1`(
id int,
name varchar(45),
email varchar(45),
street varchar(45),
area varchar(45),
city varchar(45),
state varchar(45)
);

insert into project.task1(id,name,email,street,area,city,state) values(1,'dhahul','d@gmail.com','agraharapet','naidupet','tirupati','ap');
insert into project.task1(id,name,email,street,area,city,state) values(2,'sai','s@gmail.com','graddagunta','naidupet','tirupati','ap');
select * from project.task1;

update project.task1 set city = 'nellore';
update project.task1 set city = 'tirupati' where name='sai';

delete from project.task1 where name = 'sai'; 
delete from project.task1; 