from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, INTEGER, String, TIMESTAMP, BIGINT, BOOLEAN, TEXT
from sqlalchemy.orm import relationship

Base = declarative_base()


class TamanhoBuraco(Base):
    __tablename__ = "tamanhoBuraco"
    id = Column(INTEGER, primary_key=True)
    nome = Column(String(50), nullable=False)
    apagado = Column(BOOLEAN, default=False)


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(INTEGER, primary_key=True)
    nomeUsuario = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    senha = Column(String(50), nullable=False)
    ativo = Column(BOOLEAN)


class Buraco(Base):
    __tablename__ = "buraco"
    id = Column(INTEGER, primary_key=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    idTamanhoBuraco = Column(INTEGER, ForeignKey("tamanhoBuraco.id") nullable=False)
    idUsuario = Column(INTEGER, ForeignKey("usuario.id"))
    apagado = Column(BOOLEAN, default=False)

    tamanhoBuraco = relationship("tamanhoBuraco", backref="buraco")
    usuario = relationship("usuario", backref="buraco")
