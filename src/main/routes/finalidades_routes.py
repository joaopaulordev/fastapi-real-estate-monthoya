from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import FinalidadeSchema
from src.models.settings.dependencies import get_session_db
from src.views.http_types.http_request import HttpRequest
from src.main.composer.finalidade_atualizar_composer import finalidade_atualizar_composer
from src.main.composer.finalidade_deletar_composer import finalidade_deletar_composer
from src.main.composer.finalidade_inserir_composer import finalidade_inserir_composer
from src.main.composer.finalidade_listar_composer import finalidade_listar_composer
from src.main.composer.finalidade_visualizar_composer import finalidade_visualizar_composer


finalidade_routes = APIRouter(tags=["Finalidades"])

@finalidade_routes.post("/finalidades/adicionar")
async def adicionar_finalidade(body: FinalidadeSchema, db: Session = Depends(get_session_db)):
    finalidade_inserir = finalidade_inserir_composer(db)

    http_request =HttpRequest(body=dict(body))
    http_response = await finalidade_inserir.handle_inserir_finalidade(http_request)
    
    return JSONResponse(
        content= http_response.body,
        status_code=http_response.status_code
     )    


@finalidade_routes.get("/finalidades/listar")
async def listar_finalidades(db: Session = Depends(get_session_db)):    
    view = finalidade_listar_composer(db)

    http_request = HttpRequest()
    http_response = await view.handle_listar_finalidades(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@finalidade_routes.get("/finalidades/visualizar/{finalidade_id}")
async def visualizar_finalidade(finalidade_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"finalidade_id": finalidade_id})
    view = finalidade_visualizar_composer(db)

    http_response = await view.handle_visualizar_finalidade(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@finalidade_routes.put("/finalidades/atualizar/{finalidade_id}")
async def atualizar_finalidade(finalidade_id: int, body: FinalidadeSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"finalidade_id": finalidade_id})
    finalidade_atualizar = finalidade_atualizar_composer(db)

    http_response = await finalidade_atualizar.handle_atualizar_finalidade(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@finalidade_routes.delete("/finalidades/deletar/{finalidade_id}")
async def deletar_finalidade(finalidade_id: int, db: Session = Depends(get_session_db)):    
    view = finalidade_deletar_composer(db)

    http_request = HttpRequest(param={"finalidade_id": finalidade_id})
    http_response = await view.handle_deletar_finalidade(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
