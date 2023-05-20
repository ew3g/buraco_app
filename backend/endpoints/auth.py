from fastapi import APIRouter, HTTPException
from models.request import AuthRequest
from models.response import AuthResponse
from models.models import Usuario
from db.database import Database
from sqlalchemy import and_
from auth.auth_handler import signJWT
import hashlib

router = APIRouter(
    prefix="/auth", tags=["Buraco"], responses={404: {"description": "Not Found"}}
)


database = Database()
engine = database.get_db_connection()


@router.post("/", response_description="Usuário autenticado com sucesso")
async def post_auth(auth_req: AuthRequest):
    session = database.get_db_session(engine)
    data = None
    code = None
    usuario = None
    try:
        usuario = (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.email == auth_req.email,
                    Usuario.senha
                    == hashlib.md5(auth_req.senha.encode("utf-8")).hexdigest(),
                    Usuario.ativo == True,
                )
            )
            .one()
        )
        if usuario:
            token = signJWT(usuario.email)
            return AuthResponse(token, usuario.id)
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal error")
