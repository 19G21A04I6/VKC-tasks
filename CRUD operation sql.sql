select * from zomato.users;
insert into zomato.users(id,username,email,street,location,city,state,country,pincode)
	values(1,'Dhahul','d@gamil.com','agraharapet','naidupet','tirupati','AP','india',524126),
	(2,'sai','sai@gamil.com','agraharapet','naidupet','tirupati','AP','india',524126);
    update zomato.users set email='dhahul@gmail.com' where email='d@gmail.com';
	delete from zomato.users where id=2;
