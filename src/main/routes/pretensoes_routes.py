from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import PretensaoSchema
from src.models.settings.dependencies import get_session_db
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pretensao_atualizar_composer import pretensao_atualizar_composer
from src.main.composer.pretensao_deletar_composer import pretensao_deletar_composer
from src.main.composer.pretensao_inserir_composer import pretensao_inserir_composer
from src.main.composer.pretensao_listar_composer import pretensao_listar_composer
from src.main.composer.pretensao_visualizar_composer import pretensao_visualizar_composer


pretensao_routes = APIRouter(tags=["Pretensões"])

@pretensao_routes.post("/pretensoes/adicionar")
async def adicionar_pretensao(body: PretensaoSchema, db: Session = Depends(get_session_db)):
    pretensao_inserir = pretensao_inserir_composer(db)

    http_request =HttpRequest(body=dict(body))
    http_response = await pretensao_inserir.handle_inserir_pretensao(http_request)
    
    return JSONResponse(
        content= http_response.body,
        status_code=http_response.status_code
     )    


@pretensao_routes.get("/pretensoes/listar")
async def listar_pretensoes(db: Session = Depends(get_session_db)):    
    view = pretensao_listar_composer(db)

    http_request = HttpRequest()
    http_response = await view.handle_listar_pretensoes(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@pretensao_routes.get("/pretensoes/visualizar/{pretensao_id}")
async def visualizar_pretensao(pretensao_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"pretensao_id": pretensao_id})
    view = pretensao_visualizar_composer(db)

    http_response = await view.handle_visualizar_pretensao(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@pretensao_routes.put("/pretensoes/atualizar/{pretensao_id}")
async def atualizar_pretensao(pretensao_id: int, body: PretensaoSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"pretensao_id": pretensao_id})
    pretensao_atualizar = pretensao_atualizar_composer(db)

    http_response = await pretensao_atualizar.handle_atualizar_pretensao(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@pretensao_routes.delete("/pretensoes/deletar/{pretensao_id}")
async def deletar_pretensao(pretensao_id: int, db: Session = Depends(get_session_db)):    
    view = pretensao_deletar_composer(db)

    http_request = HttpRequest(param={"pretensao_id": pretensao_id})
    http_response = await view.handle_deletar_pretensao(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
