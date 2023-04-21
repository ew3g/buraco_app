from fastapi import APIRouter
from endpoints import tamanhoBuraco

router = APIRouter()
router.include_router(tamanhoBuraco.router)


https: // www.tutorialsbuddy.com/create-rest-api-to-perform-crud-operations-using-fastapi-and -mysql
