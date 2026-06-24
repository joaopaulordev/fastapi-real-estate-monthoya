from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import TipoImovelSchema
from src.models.settings.dependencies import get_session_db, check_token
from src.views.http_types.http_request import HttpRequest
from src.main.composer.tipo_imovel_deletar_composer import tipo_imovel_deletar_composer
from src.main.composer.tipo_imovel_inserir_composer import tipo_imovel_inserir_composer
from src.main.composer.tipo_imovel_listar_composer import tipo_imovel_listar_composer
from src.main.composer.tipo_imovel_visualizar_composer import tipo_imovel_visualizar_composer
from src.main.composer.tipo_imovel_atualizar_composer import tipo_imovel_atualizar_composer


tipo_imovel_routes = APIRouter(tags=["Tipo Imóveis"])

@tipo_imovel_routes.post("/tipo-imoveis/adicionar", dependencies=[Depends(check_token)])
async def adicionar_tipo_imovel(body: TipoImovelSchema, db: Session = Depends(get_session_db)):
    tipo_imovel_inserir = tipo_imovel_inserir_composer(db)

    http_request =HttpRequest(body=dict(body))
    http_response = await tipo_imovel_inserir.handle_inserir_tipo_imovel(http_request)
    
    return JSONResponse(
        content= http_response.body,
        status_code=http_response.status_code
     )    


@tipo_imovel_routes.get("/tipo-imoveis/listar")
async def listar_tipo_imoveis(db: Session = Depends(get_session_db)):    
    view = tipo_imovel_listar_composer(db)

    http_request = HttpRequest()
    http_response = await view.handle_listar_tipo_imoveis(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@tipo_imovel_routes.get("/tipo-imoveis/visualizar/{tipo_imovel_id}", dependencies=[Depends(check_token)])
async def visualizar_tipo_imovel(tipo_imovel_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"tipo_imovel_id": tipo_imovel_id})
    view = tipo_imovel_visualizar_composer(db)

    http_response = await view.handle_visualizar_tipo_imovel(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@tipo_imovel_routes.put("/tipo-imoveis/atualizar/{tipo_imovel_id}", dependencies=[Depends(check_token)])
async def atualizar_tipo_imovel(tipo_imovel_id: int, body: TipoImovelSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"tipo_imovel_id": tipo_imovel_id})
    view = tipo_imovel_atualizar_composer(db)

    http_response = await view.handle_atualizar_tipo_imovel(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@tipo_imovel_routes.delete("/tipo-imoveis/deletar/{tipo_imovel_id}", dependencies=[Depends(check_token)])
async def deletar_tipo_imovel(tipo_imovel_id: int, db: Session = Depends(get_session_db)):    
    view = tipo_imovel_deletar_composer(db)

    http_request = HttpRequest(param={"tipo_imovel_id": tipo_imovel_id})
    http_response = await view.handle_deletar_tipo_imovel(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
