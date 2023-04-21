from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class TamanhoBuracoRequest(BaseModel):
    nome: str = Field(None, title="Tamanho Buraco Nome", max_length=50)


class TamanhoBuracoUpdateRequest(BaseModel):
    tamanho_buraco_id: int
    nome: str = Field(None, title="Tamanho Buraco Nome", max_length=50)


class UsuarioRequest(BaseModel):
    nome_usuario: str = Field(None, title="Usuário Nome", max_length=50)
    email: EmailStr = Field(None, title="Usuário Email", max_length=150)
    senha: str = Field(None, title="Usuário Senha", max_length=50)
    ativo: bool = Field(None, title="Usuário Ativo")


class UsuarioUpdateRequest(BaseModel):
    usuario_id: int
    senha: str = Field(None, title="Usuário Senha", max_length=50)
    ativo: bool = Field(None, title="Usuário Ativo")


class BuracoRequest(BaseModel):
    latitude: str = Field(None, title="Buraco Latitude")
    longitude: str = Field(None, title="Buraco Longitude")
    tamanho_buraco_id: int = Field(None, title="Buraco Tamanho")
    usuario_id: int = Field(None, title="Buraco Usuário")


class BuracoUpdateRequest(BaseModel):
    buraco_id: int
    latitude: str = Field(None, title="Buraco Latitude")
    longitude: str = Field(None, title="Buraco Longitude")
    tamanho_buraco_id: int = Field(None, title="Buraco Tamanho")
    usuario_id: int = Field(None, title="Buraco Usuário")
