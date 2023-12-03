create database if not exists Twitter;

use Twitter;

create table if not exists Twitter_bitcoins(
	id integer auto_increment primary key,
	fecha date not null,
    usuario varchar(255) not null,
    texto varchar(999) not null,
    likes integer not null);
    
    
ALTER TABLE Twitter_bitcoins AUTO_INCREMENT = 1;
