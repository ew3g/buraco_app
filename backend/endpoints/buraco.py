from fastapi import APIRouter, Depends, HTTPException, Request
from models.request import BuracoRequest, BuracoUpdateRequest
from models.response import BuracoResponse, BuracoListResponse
from models.models import Buraco
from db.database import Database
from sqlalchemy import and_
from auth.auth_bearer import JWTBearer
from endpoints.usuario import get_usuario_by_email
from auth.auth_handler import decodeJWT


router = APIRouter(
    prefix="/buraco", tags=["Buraco"], responses={404: {"description": "Not Found"}}
)

database = Database()
engine = database.get_db_connection()


@router.post(
    "/",
    dependencies=[Depends(JWTBearer())],
    status_code=201,
)
async def add_buraco(buraco_req: BuracoRequest):    
    new_buraco = Buraco()
    new_buraco.idTamanhoBuraco = buraco_req.tamanho_buraco_id
    new_buraco.idUsuario = buraco_req.usuario_id
    new_buraco.latitude = buraco_req.latitude
    new_buraco.longitude = buraco_req.longitude
    new_buraco.votos = buraco_req.votos

    session = database.get_db_session(engine)

    session.add(new_buraco)
    session.flush()

    session.refresh(new_buraco, attribute_names=["id"])
    session.commit()
    session.close()


@router.put("/{buraco_id}", dependencies=[Depends(JWTBearer())], status_code=204)
async def update_buraco(buraco_id: str, buraco_update_req: BuracoUpdateRequest):
    session = database.get_db_session(engine)

    buraco_existente = get_buraco(buraco_id)
    if not buraco_existente:
        raise HTTPException(status_code=404, detail="Buraco não encontrado")

    try:
        is_buraco_updated = (
            session.query(Buraco)
            .filter(Buraco.id == buraco_id)
            .update(
                {
                    Buraco.idTamanhoBuraco: buraco_update_req.tamanho_buraco_id,
                    Buraco.votos: buraco_update_req.votos,
                },
                synchronize_session=False,
            )
        )

        session.flush()
        session.commit()
        if is_buraco_updated == 0:
            raise HTTPException(status_code=404, detail="Buraco não existe")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.delete("/{buraco_id}", dependencies=[Depends(JWTBearer())], status_code=204)
async def delete_buraco(buraco_id: str):
    session = database.get_db_session(engine)

    buraco_existente = get_buraco(buraco_id)
    if not buraco_existente:
        raise HTTPException(status_code=404, detail="Buraco não encontrado")

    try:
        is_buraco_updated = (
            session.query(Buraco)
            .filter(and_(Buraco.id == buraco_id, Buraco.apagado == False))
            .update({Buraco.apagado: True}, synchronize_session=False)
        )
        session.flush()
        session.commit()
        if is_buraco_updated == 0:
            raise HTTPException(status_code=404, detail="Buraco não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


@router.get("/{buraco_id}", dependencies=[Depends(JWTBearer())], status_code=200)
async def read_buraco(buraco_id: str):
    buraco_existente = get_buraco(buraco_id)
    if not buraco_existente:
        raise HTTPException(status_code=404, detail="Buraco não encontrado")
    return BuracoResponse(buraco_existente)


@router.get("/", dependencies=[Depends(JWTBearer())])
async def read_all_buraco():
    session = database.get_db_session(engine)
    data = session.query(Buraco).filter(Buraco.apagado == False).all()
    return BuracoListResponse(data)


@router.post("/{buraco_id}", dependencies=[Depends(JWTBearer())], status_code=204)
async def votar_buraco(buraco_id: str):
    session = database.get_db_session(engine)

    buraco_existente = get_buraco(buraco_id)
    if not buraco_existente:
        raise HTTPException(status_code=404, detail="Buraco não encontrado")

    try:
        is_buraco_updated = (
            session.query(Buraco)
            .filter(Buraco.id == buraco_id, Buraco.apagado == False)
            .update(
                {
                    Buraco.votos: Buraco.votos + 1,
                },
                synchronize_session=False,
            )
        )

        session.flush()
        session.commit()
        if is_buraco_updated == 0:
            raise HTTPException(status_code=404, detail="Buraco não encontrado")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")


def get_buraco(id):
    session = database.get_db_session(engine)
    try:
        return (
            session.query(Buraco)
            .filter(
                and_(
                    Buraco.id == id,
                    Buraco.apagado == False,
                )
            )
            .one()
        )
    except:
        return None
