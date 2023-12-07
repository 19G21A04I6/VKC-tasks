use project;
create table project.user(
id int primary key auto_increment,
name varchar(45),
mail varchar(25)
);

drop table project.user;
insert into project.user (name,mail) values('dhahul','d@gmail.com');
insert into project.user (name,mail) values('sai','s@gmail.com');
insert into project.user (name,mail) values('jay','j@gmail.com');

delete from project.user;

select * from project.user;

create table project.orderuser(
id int primary key auto_increment,
orderitem varchar(45),
orderdedplace varchar(25),
detailsid int,
constraint fk_orderuserc_user_id foreign key(detailsid) references project.user(id)
);

insert into project.orderuser (orderitem,orderdedplace,detailsid) values('blanket','naidupet','1');
insert into project.orderuser (orderitem,orderdedplace,detailsid) values('headphones','nellore','3');
insert into project.orderuser (orderitem,orderdedplace,detailsid) values('pillows','sulurupet','2');
insert into project.orderuser (orderitem,orderdedplace,detailsid) values('carpet','nellore','3');
insert into project.orderuser (orderitem,orderdedplace,detailsid) values('Dizo watch','naidupet','1');

select * from project.orderuser;

select * from project.user as usr
inner join project.orderuser as usrord on usr.id = usrord.detailsid;

select * from project.user as usr
right join project.orderuser as usrord on usr.id = usrord.detailsid;

select * from project.user as usr
left join project.orderuser as usrord on usr.id = usrord.detailsid;

select * from project.user
cross join project.orderuser
