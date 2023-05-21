from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class TamanhoBuracoRequest(BaseModel):
    nome: str = Field(None, title="Tamanho Buraco Nome", max_length=50)
    cor: str = Field(None, title="Tamanho Buraco Cor", max_length=50)


class TamanhoBuracoUpdateRequest(BaseModel):
    nome: str = Field(None, title="Tamanho Buraco Nome", max_length=50)
    cor: str = Field(None, title="Tamanho Buraco Cor", max_length=50)


class UsuarioRequest(BaseModel):
    nome_usuario: str = Field(None, title="Usuário Nome", max_length=50)
    email: EmailStr = Field(None, title="Usuário Email")
    senha: str = Field(None, title="Usuário Senha", max_length=50)
    ativo: bool = Field(None, title="Usuário Ativo")
    adm: bool = Field(None, title="Usuário Adm")
    questao_usuario_id: int = Field(None, title="Questão Usuário Id")
    questao_usuario_resposta: str = Field(None, title="Questão Usuário Resposta", max_length=50)



class UsuarioUpdateRequest(BaseModel):
    ativo: bool = Field(True, title="Usuário Ativo")


class NovaSenhaUsuarioRequest(BaseModel):
    email: EmailStr = Field(None, title="Usuário Email")
    senha: str = Field(None, title="Usuário Senha", max_length=50)
    nova_senha: str = Field(None, title="Usuário Nova Senha", max_length=50)


class EsqueciSenhaRequest(BaseModel):
    email: EmailStr = Field(None, title="Usuário Email")
    questao_usuario_resposta: str = Field(None, title="Questão Usuário Resposta", max_length=50)
    nova_senha: str = Field(None, title="Usuário Nova Senha", max_length=50)

class BuracoRequest(BaseModel):
    latitude: str = Field(None, title="Buraco Latitude")
    longitude: str = Field(None, title="Buraco Longitude")
    tamanho_buraco_id: int = Field(None, title="Buraco Tamanho")
    usuario_id: int = Field(None, title="Buraco Usuário")
    votos: int = Field(None, title="Votos")


class BuracoUpdateRequest(BaseModel):
    latitude: str = Field(None, title="Buraco Latitude")
    longitude: str = Field(None, title="Buraco Longitude")
    tamanho_buraco_id: int = Field(None, title="Buraco Tamanho")
    usuario_id: int = Field(None, title="Buraco Usuário")
    votos: int = Field(None, title="Votos")


class AuthRequest(BaseModel):
    email: EmailStr = Field(None, title="Usuário Email")
    senha: str = Field(None, title="Usuário Senha")
    
class QuestaoRequest(BaseModel):
    email: EmailStr = Field(None, title="Usuário Email")
