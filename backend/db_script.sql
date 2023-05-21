create database if not exists buraco_db;

use buraco_db;

/*
drop table buraco;
drop table tamanhoBuraco;
drop table questaoUsuarioResposta;
drop table questaoUsuario;
drop table usuario;
*/

-- drop table tamanhoBuraco;
create table if not exists tamanhoBuraco (
	id int auto_increment primary key,
    nome varchar(50) not null,
    cor varchar(50) not null,
    apagado boolean default false
);

-- drop table usuario
create table if not exists usuario (
	id int auto_increment primary key,
    nomeUsuario varchar(50) not null,
    email varchar(150) not null unique,
    senha varchar(50) not null,
    ativo boolean,
    apagado boolean default false,
    adm boolean
);

-- drop table questaoUsuario;
create table if not exists questaoUsuario (
    id int auto_increment primary key,
    pergunta varchar(100) not null
);

-- drop table questaoUsuarioResposta;
create table if not exists questaoUsuarioResposta (
    id int auto_increment primary key,
    idQuestaoUsuario int not null,
    idUsuario int not null,
    resposta varchar(50) not null,
    constraint fk_resposta_questao foreign key (idQuestaoUsuario) references questaoUsuario(id),
    constraint fk_resposta_usuario foreign key (idUsuario) references usuario(id) 
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
