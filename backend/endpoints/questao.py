from fastapi import APIRouter, Depends, HTTPException, Request
from models.request import QuestaoRequest
from models.response import (
    TamanhoBuracoListResponse,
    QuestaoResponse,
    QuestaoListResponse,
)
from models.models import Usuario, QuestaoUsuarioResposta, QuestaoUsuario
from db.database import Database
from sqlalchemy import and_
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decodeJWT
from endpoints.usuario import get_usuario_by_email

router = APIRouter(
    prefix="/questao",
    tags=["Questão"],
    responses={404: {"description": "Not Found"}},
)

database = Database()
engine = database.get_db_connection()


@router.get("/", status_code=200)
async def read_all_questao():
    session = database.get_db_session(engine)
    data = session.query(QuestaoUsuario).all()
    return QuestaoListResponse(data)


@router.post("/usuario", status_code=200)
async def read_questao_by_usuario(questao_req: QuestaoRequest):
    session = database.get_db_session(engine)

    usuario_existente = None
    try:
        usuario_existente = (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.email == questao_req.email,
                )
            )
            .one()
        )
    except:
        usuario_existente = None

    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Not found")

    questao_resposta_existente = None
    try:
        questao_resposta_existente = (
            session.query(QuestaoUsuarioResposta)
            .filter(
                and_(
                    QuestaoUsuarioResposta.idUsuario == usuario_existente.id,
                )
            )
            .one()
        )
    except:
        raise HTTPException(status_code=404, detail="Not found")

    return QuestaoResponse(questao_resposta_existente.questaoUsuario)
