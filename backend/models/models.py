from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    ForeignKey,
    INTEGER,
    String,
    TIMESTAMP,
    BIGINT,
    BOOLEAN,
    TEXT,
)
from sqlalchemy.orm import relationship

Base = declarative_base()


class TamanhoBuraco(Base):
    __tablename__ = "tamanhoBuraco"
    id = Column(INTEGER, primary_key=True)
    nome = Column(String(50), nullable=False)
    cor = Column(String(50), nullable=False)
    apagado = Column(BOOLEAN, default=False)


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(INTEGER, primary_key=True)
    nomeUsuario = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    senha = Column(String(50), nullable=False)
    ativo = Column(BOOLEAN)
    apagado = Column(BOOLEAN, default=False)
    adm = Column(BOOLEAN, default=False)


class QuestaoUsuario(Base):
    __tablename__ = "questaoUsuario"
    id = Column(INTEGER, primary_key=True)
    pergunta = Column(String(100), nullable=False)
    
class QuestaoUsuarioResposta(Base):
    __tablename__ = "questaoUsuarioResposta"
    id = Column(INTEGER, primary_key=True)
    idQuestaoUsuario = Column(INTEGER, ForeignKey("questaoUsuario.id"))
    idUsuario = Column(INTEGER, ForeignKey("usuario.id"))
    resposta = Column(String(50), nullable=False)

    usuario = relationship("Usuario", backref="questaoUsuarioResposta")
    questaoUsuario = relationship("QuestaoUsuario", backref="questaoUsuarioResposta")


class Buraco(Base):
    __tablename__ = "buraco"
    id = Column(INTEGER, primary_key=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    idTamanhoBuraco = Column(INTEGER, ForeignKey("tamanhoBuraco.id"), nullable=False)
    idUsuario = Column(INTEGER, ForeignKey("usuario.id"))
    votos = Column(INTEGER, default=0)
    apagado = Column(BOOLEAN, default=False)

    tamanhoBuraco = relationship("TamanhoBuraco", backref="buraco")
    usuario = relationship("Usuario", backref="buraco")
