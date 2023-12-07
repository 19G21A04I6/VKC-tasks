use project;

create table project.employee(
id int primary key auto_increment,
name varchar(25),
mail varchar(25),
gender varchar(6)
);

select * from project.employee;

insert into project.employee(name,mail,gender) values('Dhahul','d@mail.com','Male');
insert into project.employee(name,mail,gender) values('Sai','s@mail.com','Male');
insert into project.employee(name,mail,gender) values('sundari','sd@mail.com','Female');
insert into project.employee(name,mail,gender) values('jayanth','j@mail.com','Male');

delete from project.employee where id = 3;

-- alter table project.employee
-- drop column ;

create table project.employeeaddrees(
area varchar(25),
city varchar(25),
state varchar(20),
employeeid int,
constraint fk_employeeaddrees_employee_id foreign key(employeeid) references project.employee(id)
);

drop table project.employeeaddrees;
select * from project.employeeaddrees;

insert into project.employeeaddrees(area,city,state,employeeid) values('Naidupet','Tirupati','AP',1);
insert into project.employeeaddrees(area,city,state,employeeid) values('kurnool','kurnool','AP',5);
insert into project.employeeaddrees(area,city,state,employeeid) values('nellore','nellore','AP',2);

select * from project.employee as emp
inner join project.employeeaddrees as empadd on emp.id=empadd.employeeid;

select * from project.employee as emp
right join project.employeeaddrees as empadd on emp.id=empadd.employeeid;

select * from project.employee as emp
left join project.employeeaddrees as empadd on emp.id=empadd.employeeid;

select * from project.employee
cross join project.employeeaddrees;
