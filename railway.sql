create DATABASE railway;

use railway;
show tables;

create table train1(
    train_no int not null primary key,
    train_name varchar(50),
    station_no_1 int,
    station_no_2 int,
    station_no_3 int,
    station_no_4 int);

describe train1;

create table station_table(
    station_no int not null primary key,
    location VARCHAR(25)
);

describe station_table;

create table seat_table(

    seat_no int not null primary key,
    seat_type varchar(5)  not null,
    username  VARCHAR(20) 
);

describe seat_table;

drop table seat_table;

select * from seat_table;

truncate table seat_table;

drop table seat_table;

create table user_table(
    firstname VARCHAR(20) not null,
    lastname VARCHAR(20) not null,
    username VARCHAR(20) not null UNIQUE,
    email VARCHAR(40) not null UNIQUE,
    phone_no bigint not null UNIQUE,
    gender VARCHAR(1) not null,
    address VARCHAR(100) ,
    password VARCHAR(50) not null,
    PRIMARY key(username)

);


describe user_table;


select * from user_table;

insert into user_table values(

'rudraksh',
    'naik',
   'h5hkat',
   'rudrakshnaik@gmail.com',
     9921098769,
    'M',
   'D-203 , Alcove Society , Pimple Saudagar , Pune , Maharashtra',
     '123'
);



TRUNCATE table user_table;

drop table user_table;

select * from user_table where username = 'ha5hkat';

select seat_no,seat_type from seat_table where firstname is null ; 
select seat_no,seat_type from seat_table;


select * from seat_table WHERE username = 'ha5hkat';



UPDATE seat_table set username = NULL where username = "ha5hkat";


select * from seat_table;

select * from seat_table where username = 'void';

select seat_table.username, seat_table.seat_no, seat_table.seat_type, user_table.firstname 
from user_table left join seat_table on user_table.username = seat_table.username ;