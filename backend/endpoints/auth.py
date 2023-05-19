from fastapi import APIRouter
from models.request import AuthRequest
from models.response import AuthResponse
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
    data = None
    code = None
    usuario = None
    try:
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
            data = {
                "token": token,
                "usuarioId": usuario.id
            }
            response_msg = "Usuário autenticado com sucesso"
        else:
            code = 401
    except Exception as ex:
        code = 500
        print("Error", ex)
        response_msg = "Erro ao autenticar usuário"
    return AuthResponse(token, usuario.id)
