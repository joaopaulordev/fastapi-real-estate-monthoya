from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import InteressadoSchema
from src.models.settings.dependencies import get_session_db
from src.views.http_types.http_request import HttpRequest
from src.main.composer.interessado_inserir_composer import interessado_inserir_composer
from src.main.composer.interessado_listar_composer import interessado_listar_composer
from src.main.composer.interessado_visualizar_composer import interessado_visualizar_composer
from src.main.composer.interessado_atualizar_composer import interessado_atualizar_composer
from src.main.composer.interessado_deletar_composer import interessado_deletar_composer

interessado_routes = APIRouter(tags=["Interessados"])

@interessado_routes.post("/interessados/adicionar/{imovel_id}")
async def adicionar_interessado(imovel_id: int, body: InteressadoSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"imovel_id": imovel_id})
    interessado_inserir = interessado_inserir_composer(db)

    http_response = await interessado_inserir.handle_inserir_interessado(http_request)
    
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )

@interessado_routes.get("/interessados/listar/{imovel_id}")
async def listar_interessados(imovel_id: int, db: Session = Depends(get_session_db)):    
    view = interessado_listar_composer(db)

    http_request = HttpRequest(param={"imovel_id": imovel_id})
    http_response = await view.handle_listar_interessados(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@interessado_routes.get("/interessados/visualizar/{interessado_id}")
async def visualizar_interessado(interessado_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"interessado_id": interessado_id})
    view = interessado_visualizar_composer(db)

    http_response = await view.handle_visualizar_interessado(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@interessado_routes.put("/interessados/atualizar/{interessado_id}")
async def atualizar_interessado(interessado_id: int, body: InteressadoSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"interessado_id": interessado_id})
    interessado_atualizar = interessado_atualizar_composer(db)

    http_response = await interessado_atualizar.handle_atualizar_interessado(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@interessado_routes.delete("/interessados/deletar/{interessado_id}")
async def deletar_interessado(interessado_id: int, db: Session = Depends(get_session_db)):    
    view = interessado_deletar_composer(db)

    http_request = HttpRequest(param={"interessado_id": interessado_id})
    http_response = await view.handle_deletar_interessado(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
