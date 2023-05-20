from fastapi import APIRouter, Depends, HTTPException, Request
from models.request import TamanhoBuracoRequest, TamanhoBuracoUpdateRequest
from models.response import TamanhoBuracoListResponse, TamanhoBuracoResponse
from models.models import TamanhoBuraco
from db.database import Database
from sqlalchemy import and_
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decodeJWT
from endpoints.usuario import get_usuario_by_email

router = APIRouter(
    prefix="/tamanho-buraco",
    tags=["TamanhoBuraco"],
    responses={404: {"description": "Not Found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post(
    "/",
    response_description="Tamanho Buraco added into the database",
    dependencies=[Depends(JWTBearer())],
    status_code=201,
)
async def add_tamanho_buraco(tamanho_buraco_req: TamanhoBuracoRequest, req: Request):
    email_usuario = decodeJWT(req.headers["Authorization"].split()[1])["user_id"]
    usuario_logado = get_usuario_by_email(email_usuario)
    
    if not usuario_logado.adm:
        raise HTTPException(status_code=403, detail="Ação proibida")
    
    new_tamanho_buraco = TamanhoBuraco()
    new_tamanho_buraco.nome = tamanho_buraco_req.nome
    new_tamanho_buraco.cor = tamanho_buraco_req.cor

    session = database.get_db_session(engine)

    tamanho_buraco_existente = (
        session.query(TamanhoBuraco)
        .filter(TamanhoBuraco.nome == new_tamanho_buraco.nome)
        .first()
    )
    if tamanho_buraco_existente:
        raise HTTPException(status_code=409, detail="Tamanho Buraco já existe")

    session.add(new_tamanho_buraco)
    session.flush()

    session.refresh(new_tamanho_buraco, attribute_names=["id"])
    session.commit()
    session.close()


@router.put(
    "/{tamanho_buraco_id}", dependencies=[Depends(JWTBearer())], status_code=204
)
async def update_tamanho_buraco(
    tamanho_buraco_id: str, tamanho_buraco_update_req: TamanhoBuracoUpdateRequest, req: Request
):
    email_usuario = decodeJWT(req.headers["Authorization"].split()[1])["user_id"]
    usuario_logado = get_usuario_by_email(email_usuario)
    
    if not usuario_logado.adm:
        raise HTTPException(status_code=403, detail="Ação proibida")
    
    session = database.get_db_session(engine)

    tamanho_buraco_existente = get_tamanho_buraco(tamanho_buraco_id)
    if not tamanho_buraco_existente:
        raise HTTPException(status_code=404, detail="Tamanho Buraco não encontrado")

    try:
        is_tamanho_buraco_updated = (
            session.query(TamanhoBuraco)
            .filter(TamanhoBuraco.id == tamanho_buraco_id)
            .update(
                {
                    TamanhoBuraco.nome: tamanho_buraco_update_req.nome,
                    TamanhoBuraco.cor: tamanho_buraco_update_req.cor,
                },
                synchronize_session=False,
            )
        )
        print(tamanho_buraco_id)
        session.flush()
        session.commit()
        if is_tamanho_buraco_updated == 0:
            raise HTTPException(status_code=404, detail="Tamanho Buraco não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.delete(
    "/{tamanho_buraco_id}", dependencies=[Depends(JWTBearer())], status_code=204
)
async def delete_tamanho_buraco(tamanho_buraco_id: str, req: Request):
    email_usuario = decodeJWT(req.headers["Authorization"].split()[1])["user_id"]
    usuario_logado = get_usuario_by_email(email_usuario)
    
    if not usuario_logado.adm:
        raise HTTPException(status_code=403, detail="Ação proibida")
    
    session = database.get_db_session(engine)

    tamanho_buraco_existente = get_tamanho_buraco(tamanho_buraco_id)
    if not tamanho_buraco_existente:
        raise HTTPException(status_code=404, detail="Tamanho Buraco não encontrado")

    try:
        is_tamanho_buraco_updated = (
            session.query(TamanhoBuraco)
            .filter(
                and_(
                    TamanhoBuraco.id == tamanho_buraco_id,
                    TamanhoBuraco.apagado == False,
                )
            )
            .update({TamanhoBuraco.apagado: True}, synchronize_session=False)
        )
        session.flush()
        session.commit()
        if is_tamanho_buraco_updated == 0:
            raise HTTPException(status_code=404, detail="Buraco não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.get("/{tamanho_buraco_id}", dependencies=[Depends(JWTBearer())])
async def read_tamanho_buraco(tamanho_buraco_id: str):
    tamanho_buraco_existente = get_tamanho_buraco(tamanho_buraco_id)
    if not tamanho_buraco_existente:
        raise HTTPException(status_code=404, detail="Tamanho Buraco não encontrado")

    return TamanhoBuracoResponse(tamanho_buraco_existente)


@router.get("/", dependencies=[Depends(JWTBearer())])
async def read_all_tamanho_buraco():
    session = database.get_db_session(engine)
    data = session.query(TamanhoBuraco).filter(TamanhoBuraco.apagado == False).all()
    return TamanhoBuracoListResponse(data)


def get_tamanho_buraco(id):
    session = database.get_db_session(engine)
    try:
        return (
            session.query(TamanhoBuraco)
            .filter(
                and_(
                    TamanhoBuraco.id == id,
                    TamanhoBuraco.apagado == False,
                )
            )
            .one()
        )
    except:
        return None
