from fastapi import APIRouter, Depends
from models.request import BuracoRequest, BuracoUpdateRequest
from models.response import Response
from models.models import Buraco
from db.database import Database
from sqlalchemy import and_
from auth.auth_bearer import JWTBearer


router = APIRouter(
    prefix="/buraco", tags=["Buraco"], responses={404: {"description": "Not Found"}}
)

database = Database()
engine = database.get_db_connection()


@router.post(
    "/",
    response_description="Buraco added into the database",
    dependencies=[Depends(JWTBearer())],
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
    data = {"buraco_id": new_buraco.id}
    session.commit()
    session.close()
    return Response(data, 201, "Buraco cadastrado com sucesso.", False)


@router.put("/{buraco_id}", dependencies=[Depends(JWTBearer())])
async def update_buraco(buraco_id: str, buraco_update_req: BuracoUpdateRequest):
    session = database.get_db_session(engine)

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
        response_msg = "Buraco atualizado com sucesso."
        response_code = 204
        error = False
        if is_buraco_updated == 1:
            data = session.query(Buraco).filter(Buraco.id == buraco_id).one()
        elif is_buraco_updated == 0:
            response_msg = (
                "Buraco não atualizado. Nenhum Buraco encontrado com o id: "
                + str(buraco_id)
            )
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error: ", ex)


@router.delete("/{buraco_id}", dependencies=[Depends(JWTBearer())])
async def delete_buraco(buraco_id: str):
    session = database.get_db_session(engine)

    try:
        is_buraco_updated = (
            session.query(Buraco)
            .filter(and_(Buraco.id == buraco_id, Buraco.apagado == False))
            .update({Buraco.apagado: True}, synchronize_session=False)
        )
        session.flush()
        session.commit()
        response_msg = "Buraco apagado com sucesso"
        response_code = 204
        error = False
        data = {"buraco_id": buraco_id}
        if is_buraco_updated == 0:
            response_msg = (
                "Buraco não apagado. Nenhum Buraco encontrado com o id: "
                + str(buraco_id)
            )
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error: ", ex)


@router.get("/{buraco_id}", dependencies=[Depends(JWTBearer())])
async def read_buraco(buraco_id: str):
    session = database.get_db_session(engine)
    response_msg = "Buraco encontrado com sucesso"
    data = None
    try:
        data = (
            session.query(Buraco)
            .filter(and_(Buraco.id == buraco_id, Buraco.apagado == False))
            .one()
        )
    except Exception as ex:
        print("Error", ex)
        response_msg = "Buraco não encontrado"
    error = False
    return Response(data, 200, response_msg, error)


@router.get("/", dependencies=[Depends(JWTBearer())])
async def read_all_buraco():
    session = database.get_db_session(engine)
    data = session.query(Buraco).filter(Buraco.apagado == False).all()
    return Response(data, 200, "", False)
