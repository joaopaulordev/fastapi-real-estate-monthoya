from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import ConfiguracaoSchema
from src.models.settings.dependencies import get_session_db, check_token
from src.views.http_types.http_request import HttpRequest
from src.main.composer.configuracao_atualizar_composer import configuracao_atualizar_composer
from src.main.composer.configuracao_listar_composer import configuracao_listar_composer


configuracao_routes = APIRouter(tags=["Configurações"])


@configuracao_routes.get("/configuracoes/listar")
async def listar_configuracoes(db: Session = Depends(get_session_db)):    
    view = configuracao_listar_composer(db)

    http_request = HttpRequest()
    http_response = await view.handle_listar_configuracoes(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@configuracao_routes.put("/configuracoes/atualizar/{configuracao_id}", dependencies=[Depends(check_token)])
async def atualizar_configuracao(configuracao_id: int, body: ConfiguracaoSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"configuracao_id": configuracao_id})
    configuracao_atualizar = configuracao_atualizar_composer(db)

    http_response = await configuracao_atualizar.handle_atualizar_configuracao(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )