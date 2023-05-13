from fastapi import APIRouter, Depends
from models.request import UsuarioRequest, UsuarioUpdateRequest
from models.response import Response
from models.models import Usuario
from db.database import Database
from sqlalchemy import and_
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/usuario", tags=["Usuario"], responses={404: {"description": "Not Found"}}
)

database = Database()
engine = database.get_db_connection()


@router.post(
    "/",
    response_description="Usuario added into the database",
    dependencies=[Depends(JWTBearer())],
)
async def add_usuario(usuario_req: UsuarioRequest):
    new_usuario = Usuario()
    new_usuario.email = usuario_req.email
    new_usuario.nomeUsuario = usuario_req.nome_usuario
    new_usuario.senha = usuario_req.senha
    new_usuario.ativo = True

    session = database.get_db_session(engine)

    usuario_existente = (
        session.query(Usuario)
        .filter(Usuario.nomeUsuario == new_usuario.nomeUsuario)
        .first()
    )
    if usuario_existente:
        return Response(None, 400, "Usuario já existe", False)

    session.add(new_usuario)
    session.flush()

    session.refresh(new_usuario, attribute_names=["id"])
    data = {"usuario_id": new_usuario.id}
    session.commit()
    session.close()
    return Response(data, 201, "Usuario cadastrado com sucesso.", False)


@router.put("/{usuario_id}", dependencies=[Depends(JWTBearer())])
async def update_usuario(usuario_id: str, usuario_update_req: UsuarioUpdateRequest):
    session = database.get_db_session(engine)

    try:
        is_usuario_updated = (
            session.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .update(
                {
                    Usuario.senha: usuario_update_req.senha,
                    Usuario.ativo: usuario_update_req.ativo,
                },
                synchronize_session=False,
            )
        )

        session.flush()
        session.commit()
        response_msg = "Usuario atualizado com sucesso."
        response_code = 204
        error = False
        if is_usuario_updated == 1:
            data = session.query(Usuario).filter(Usuario.id == usuario_id).one()
        elif is_usuario_updated == 0:
            response_msg = (
                "Usuario não atualizado. Nenhum Usuario encontrado com o id: "
                + str(usuario_id)
            )
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error: ", ex)


@router.delete("/{usuario_id}", dependencies=[Depends(JWTBearer())])
async def delete_usuario(usuario_id: str):
    session = database.get_db_session(engine)

    try:
        is_usuario_updated = (
            session.query(Usuario)
            .filter(and_(Usuario.id == usuario_id, Usuario.apagado == False))
            .update({Usuario.apagado: True}, synchronize_session=False)
        )
        session.flush()
        session.commit()
        response_msg = "Usuario apagado com sucesso"
        response_code = 204
        error = False
        data = {"usuario_id": usuario_id}
        if is_usuario_updated == 0:
            response_msg = (
                "Usuario não apagado. Nenhum Usuario encontrado com o id: "
                + str(usuario_id)
            )
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error: ", ex)


@router.get("/{usuario_id}", dependencies=[Depends(JWTBearer())])
async def read_usuario(usuario_id: str):
    session = database.get_db_session(engine)
    response_msg = "Usuario encontrado com sucesso"
    data = None
    try:
        data = (
            session.query(Usuario)
            .filter(and_(Usuario.id == usuario_id, Usuario.apagado == False))
            .one()
        )
    except Exception as ex:
        print("Error", ex)
        response_msg = "Usuario não encontrado"
    error = False
    return Response(data, 200, response_msg, error)


@router.get("/", dependencies=[Depends(JWTBearer())])
async def read_all_usuario():
    session = database.get_db_session(engine)
    data = session.query(Usuario).filter(Usuario.apagado == False).all()
    return Response(data, 200, "", False)
