from fastapi import APIRouter
from models.request import AuthRequest
from models.response import Response
from models.models import Usuario
from db.database import Database
from sqlalchemy import and_
from auth.auth_handler import signJWT

router = APIRouter(
    prefix="/auth", tags=["Buraco"], responses={404: {"description": "Not Found"}}
)


database = Database()
engine = database.get_db_connection()


@router.post("/", response_description="Usuário autenticado com sucesso")
async def post_auth(auth_req: AuthRequest):
    session = database.get_db_session(engine)
    token = None
    code = None
    try:
        print(auth_req.email)
        print(auth_req.senha)
        usuario = (
            session.query(Usuario)
            .filter(
                and_(
                    Usuario.email == auth_req.email,
                    Usuario.senha == auth_req.senha,
                    Usuario.ativo == True,
                )
            )
            .one()
        )
        if usuario:
            code = 200
            token = signJWT(usuario.email)
            response_msg = "Usuário autenticado com sucesso"
        else:
            code = 401
    except Exception as ex:
        print("Error", ex)
        response_msg = "Erro ao autenticar usuário"
    return Response(token, code, response_msg, False)
