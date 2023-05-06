from fastapi import APIRouter
from endpoints import tamanhoBuraco, usuario, buraco

router = APIRouter()
router.include_router(tamanhoBuraco.router)
router.include_router(usuario.router)
router.include_router(buraco.router)

# https: // www.tutorialsbuddy.com/create-rest-api-to-perform-crud-operations-using-fastapi-and -mysql
