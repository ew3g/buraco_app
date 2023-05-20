from fastapi import APIRouter, Depends, HTTPException
from models.request import (
    UsuarioRequest,
    UsuarioUpdateRequest,
    NovaSenhaUsuarioRequest,
    EsqueciSenhaRequest,
)
from models.response import Response, UsuarioResponse, UsuarioListResponse
from models.models import Usuario
from db.database import Database
from sqlalchemy import and_
from auth.auth_bearer import JWTBearer
import hashlib
from auth.auth_handler import signJWT

router = APIRouter(
    prefix="/usuario", tags=["Usuario"], responses={404: {"description": "Not Found"}}
)

database = Database()
engine = database.get_db_connection()


@router.post(
    "/", response_description="Usuario added into the database", status_code=201
)
async def add_usuario(usuario_req: UsuarioRequest):
    new_usuario = Usuario()
    new_usuario.email = usuario_req.email
    new_usuario.nomeUsuario = usuario_req.nome_usuario
    new_usuario.senha = hashlib.md5(usuario_req.senha.encode("utf-8")).hexdigest()
    new_usuario.ativo = True

    session = database.get_db_session(engine)

    usuario_existente = (
        session.query(Usuario)
        .filter(Usuario.nomeUsuario == new_usuario.nomeUsuario)
        .first()
    )
    if usuario_existente:
        raise HTTPException(status_code=409, detail="Usuário já existe")

    session.add(new_usuario)
    session.flush()

    session.refresh(new_usuario, attribute_names=["id"])
    session.commit()
    session.close()


@router.put("/{usuario_id}", dependencies=[Depends(JWTBearer())], status_code=204)
async def update_usuario(usuario_id: str, usuario_update_req: UsuarioUpdateRequest):
    session = database.get_db_session(engine)

    usuario_existente = get_usuario(usuario_id)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    try:
        is_usuario_updated = (
            session.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .update(
                {
                    Usuario.ativo: usuario_update_req.ativo,
                },
                synchronize_session=False,
            )
        )

        session.flush()
        session.commit()
        if is_usuario_updated == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.delete("/{usuario_id}", dependencies=[Depends(JWTBearer())], status_code=204)
async def delete_usuario(usuario_id: str):
    session = database.get_db_session(engine)

    usuario_existente = get_usuario(usuario_id)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    try:
        is_usuario_updated = (
            session.query(Usuario)
            .filter(and_(Usuario.id == usuario_id, Usuario.apagado == False))
            .update({Usuario.apagado: True}, synchronize_session=False)
        )
        session.flush()
        session.commit()
        if is_usuario_updated == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.get("/{usuario_id}", dependencies=[Depends(JWTBearer())])
async def read_usuario(usuario_id: str):
    usuario_existente = get_usuario(usuario_id)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return UsuarioResponse(usuario_existente)


@router.get("/", dependencies=[Depends(JWTBearer())])
async def read_all_usuario():
    session = database.get_db_session(engine)
    data = session.query(Usuario).filter(Usuario.apagado == False).all()
    return UsuarioListResponse(data)


@router.post(
    "/nova-senha/{usuario_id}", dependencies=[Depends(JWTBearer())], status_code=204
)
async def change_password_usuario(
    usuario_id: str, nova_senha_usuario_req: NovaSenhaUsuarioRequest
):
    session = database.get_db_session(engine)

    usuario_existente = None
    try:
        usuario_existente = (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.id == usuario_id,
                    Usuario.email == nova_senha_usuario_req.email,
                    Usuario.senha
                    == hashlib.md5(
                        nova_senha_usuario_req.senha.encode("utf-8")
                    ).hexdigest(),
                    Usuario.apagado == False,
                )
            )
            .one()
        )
    except:
        usuario_existente = None

    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    try:
        is_usuario_updated = (
            session.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .update(
                {
                    Usuario.senha: hashlib.md5(
                        nova_senha_usuario_req.nova_senha.encode("utf-8")
                    ).hexdigest(),
                },
                synchronize_session=False,
            )
        )

        session.flush()
        session.commit()
        if is_usuario_updated == 0:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.post("/esqueci-senha", dependencies=[Depends(JWTBearer())], status_code=201)
async def enviar_email_esqueci_senha(esqueci_senha_request: EsqueciSenhaRequest):
    session = database.get_db_session(engine)

    usuario_existente = None
    try:
        usuario_existente = (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.email == esqueci_senha_request.email,
                    Usuario.apagado == False,
                )
            )
            .one()
        )
    except:
        usuario_existente = None

    if usuario_existente:
        token = signJWT(usuario_existente.email)
        print(token)


@router.post("/esqueci-senha", dependencies=[Depends(JWTBearer())], status_code=201)
async def enviar_email_esqueci_senha(esqueci_senha_request: EsqueciSenhaRequest):
    session = database.get_db_session(engine)

    usuario_existente = None
    try:
        usuario_existente = (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.email == esqueci_senha_request.email,
                    Usuario.apagado == False,
                )
            )
            .one()
        )
    except:
        usuario_existente = None

    if usuario_existente:
        token = signJWT(usuario_existente.email)
        print(token)


def get_usuario(id):
    session = database.get_db_session(engine)
    try:
        return (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.id == id,
                    Usuario.apagado == False,
                )
            )
            .one()
        )
    except:
        return None
