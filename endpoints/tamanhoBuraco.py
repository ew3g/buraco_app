from fastapi import APIRouter
from models.request import TamanhoBuracoRequest, TamanhoBuracoUpdateRequest
from models.response import Response
from models.models import TamanhoBuraco
from db.database import Database
from sqlalchemy import and_

router = APIRouter(prefix="/tamanho-buraco",
                   tags=["TamanhoBuraco"],
                   responses={404: {"description": "Not Found"}})

database = Database()
engine = database.get_db_connection()


@router.post("/", response_description="Tamanho Buraco added into the database")
async def add_tamanho_buraco(tamanho_buraco_req: TamanhoBuracoRequest):
    new_tamanho_buraco = TamanhoBuraco()
    new_tamanho_buraco.nome = tamanho_buraco_req.nome

    session = database.get_db_session(engine)

    tamanho_buraco_existente = session.query(TamanhoBuraco).filter(
        TamanhoBuraco.nome == new_tamanho_buraco.nome).first()
    if tamanho_buraco_existente:
        return Response(None, 400, "Tamanho Buraco jã existe", False)

    session.add(new_tamanho_buraco)
    session.flush()

    session.refresh(new_tamanho_buraco, attribute_names=["id"])
    data = {"tamanho_buraco_id": new_tamanho_buraco.id}
    session.commit()
    session.close()
    return Response(data, 201, "Tamanho Buraco cadastrado com sucesso.", False)


@router.put("/{tamanho_buraco_id}")
async def update_tamanho_buraco(tamanho_buraco_id: str, tamanho_buraco_update_req: TamanhoBuracoUpdateRequest):
    session = database.get_db_session(engine)

    try:
        is_tamanho_buraco_updated = session.query(TamanhoBuraco).filter(TamanhoBuraco.id == tamanho_buraco_id).update(
            {TamanhoBuraco.nome: tamanho_buraco_update_req.nome}, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Tamanho Buraco atualizado com sucesso."
        response_code = 204
        error = False
        if is_tamanho_buraco_updated == 1:
            data = session.query(TamanhoBuraco).filter(
                TamanhoBuraco.id == tamanho_buraco_id).one()
        elif is_tamanho_buraco_updated == 0:
            response_msg = "Tamanho Produto não atualizado. Nenhum Tamanho Buraco encontrado com o id: " + \
                str(tamanho_buraco_id)
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error: ", ex)


@router.delete("/{tamanho_buraco_id}")
async def delete_tamanho_buraco(tamanho_buraco_id: str):
    session = database.get_db_session(engine)

    try:
        is_tamanho_buraco_updated = session.query(TamanhoBuraco).filter(and_(TamanhoBuraco.id == tamanho_buraco_id, TamanhoBuraco.apagado == False)).update({
            TamanhoBuraco.apagado: True
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Tamanho Buraco apagado com sucesso"
        response_code = 204
        error = False
        data = {"tamanho_buraco_id": tamanho_buraco_id}
        if is_tamanho_buraco_updated == 0:
            response_msg = "Tamanho Buraco não apagado. Nenhum Tamanho Buraco encontrado com o id: " + \
                str(tamanho_buraco_id)
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error: ", ex)


@router.get("/{tamanho_buraco_id}")
async def read_tamanho_buraco(tamanho_buraco_id: str):
    session = database.get_db_session(engine)
    response_msg = "Tamanho Buraco encontrado com sucesso"
    data = None
    try:
        data = session.query(TamanhoBuraco).filter(and_(
            TamanhoBuraco.id == tamanho_buraco_id, TamanhoBuraco.apagado == False)).one()
    except Exception as ex:
        print("Error", ex)
        response_msg = "TamanhoBuraco não encontrado"
    error = False
    return Response(data, 200, response_msg, error)


@router.get("/")
async def read_all_tamanho_buraco():
    session = database.get_db_session(engine)
    data = session.query(TamanhoBuraco).filter(
        TamanhoBuraco.apagado == False).all()
    return Response(data, 200, "", False)
