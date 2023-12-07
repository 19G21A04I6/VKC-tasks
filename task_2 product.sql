create table project.product(
id int auto_increment primary key,
productname varchar(45)
);

insert into project.product(productname) value('Taj tea powder');
insert into project.product(productname) value('Sunflower Oil');
insert into project.product(productname) value('Apple');

select * from project.product;


create table project.productspecific(
id int primary key auto_increment,
produtmanufactured varchar(45),
quantity int ,
productid int,
constraint fk_productspecific_product_id foreign key(productid) references project.product(id)
);

insert into project.productspecific (produtmanufactured,quantity,productid) values('assam',3,1);
insert into project.productspecific (produtmanufactured,quantity,productid) values('assam',7,1);
insert into project.productspecific (produtmanufactured,quantity,productid) values('kerala',2,2);
insert into project.productspecific (produtmanufactured,quantity,productid) values('kashmir',5,3);
insert into project.productspecific (produtmanufactured,quantity,productid) values('hyderabad',3,null);


select * from project.product as p
inner join project.productspecific as ps on p.id = ps.productid;


select * from project.product as p
left join project.productspecific as ps on p.id = ps.productid;

select * from project.product as p
right join project.productspecific as ps on p.id = ps.productid;

select * from project.product
cross join project.productspecific