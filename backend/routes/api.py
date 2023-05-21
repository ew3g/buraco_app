from fastapi import APIRouter
from endpoints import tamanhoBuraco, usuario, buraco, auth, questao

router = APIRouter()
router.include_router(tamanhoBuraco.router)
router.include_router(usuario.router)
router.include_router(buraco.router)
router.include_router(auth.router)
router.include_router(questao.router)

# https: // www.tutorialsbuddy.com/create-rest-api-to-perform-crud-operations-using-fastapi-and -mysql
