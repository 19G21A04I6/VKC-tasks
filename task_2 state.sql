create table project.`state`(
id int primary key auto_increment,
statename varchar(45)
);
drop table project.`student`;

create table project.`district`(
id int,
districtname varchar(45),
stateid int
);

insert into project.state (id,statename) values(1,'AP');
insert into project.state (id,statename) values(2,'TS');
insert into project.state (id,statename) values(3,'TN');
insert into project.state (id,statename) values(4,'MH');
delete from project.state;
select*from project.district;
select*from project.state;


insert into project.district(id,districtname,stateid) values(1,'nellore',1);
insert into project.district(id,districtname,stateid) values(2,'tirupati',1);
insert into project.district(id,districtname,stateid) values(3,'warangal',2);
insert into project.district(id,districtname,stateid) values(4,'mumbai',4);
insert into project.district(id,districtname,stateid) values(5,'mumbai',4);

alter table project.district
add constraint fk_district_state_id foreign key(stateid) references project.state(id);

select * from project.state as s
left join project.district as d on s.id=d.stateid;

select * from project.state as s
right join project.district as d on s.id=d.stateid;

select * from project.state as s
inner join project.district as d on s.id=d.stateid;

select * from project.state
cross join project.district;