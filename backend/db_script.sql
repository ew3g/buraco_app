create database if not exists buraco_db;

use buraco_db;

-- drop table tamanhoBuraco;
create table if not exists tamanhoBuraco (
	id int auto_increment primary key,
    nome varchar(50) not null unique,
    cor varchar(50) not null unique,
    apagado boolean default false
);

-- drop table usuario
create table if not exists usuario (
	id int auto_increment primary key,
    nomeUsuario varchar(50) not null,
    email varchar(150) not null,
    senha varchar(50) not null,
    ativo boolean,
    apagado boolean default false
);

-- drop table buraco
create table if not exists buraco (
	id int auto_increment primary key,
    latitude text not null,
    longitude text not null,
    idTamanhoBuraco int not null,
    idUsuario int not null,
    votos int default 0,
    apagado boolean default false,
    constraint fk_buraco_tamanhoBuraco foreign key (idTamanhoBuraco) references tamanhoBuraco(id),
    constraint fk_buraco_usuario foreign key (idUsuario) references usuario(id) 
);
