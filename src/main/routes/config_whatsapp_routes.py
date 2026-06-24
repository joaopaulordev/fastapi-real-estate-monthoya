from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import ConfigWhatsappSchema
from src.models.entities.imovel import Usuario
from src.models.settings.dependencies import get_session_db, check_token
from src.views.http_types.http_request import HttpRequest
from src.main.composer.config_whatsapp_atualizar_composer import configwhatsapp_atualizar_composer
from src.main.composer.config_whatsapp_deletar_composer import configwhatsapp_deletar_composer
from src.main.composer.config_whatsapp_inserir_composer import configwhatsapp_inserir_composer
from src.main.composer.config_whatsapp_listar_composer import configwhatsapp_listar_composer
from src.main.composer.config_whatsapp_visualizar_composer import configwhatsapp_visualizar_composer


configwhatsapp_routes = APIRouter(tags=["Configuração Whatsapps"])

@configwhatsapp_routes.post("/config-whatsapp/adicionar", dependencies=[Depends(check_token)])
async def adicionar_configwhatsapp(body: ConfigWhatsappSchema, db: Session = Depends(get_session_db)):
    configwhatsapp_inserir = configwhatsapp_inserir_composer(db)

    http_request =HttpRequest(body=dict(body))
    http_response = await configwhatsapp_inserir.handle_inserir_configwhatsapp(http_request)
    
    return JSONResponse(
        content= http_response.body,
        status_code=http_response.status_code
     )    


@configwhatsapp_routes.get("/config-whatsapp/listar")
async def listar_configwhatsapps(db: Session = Depends(get_session_db)):    
    view = configwhatsapp_listar_composer(db)

    http_request = HttpRequest()
    http_response = await view.handle_listar_configwhatsapps(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@configwhatsapp_routes.get("/config-whatsapp/visualizar/{configwhatsapp_id}", dependencies=[Depends(check_token)])
async def visualizar_configwhatsapp(configwhatsapp_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"config_whatsapp_id": configwhatsapp_id})
    view = configwhatsapp_visualizar_composer(db)

    http_response = await view.handle_visualizar_configwhatsapp(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@configwhatsapp_routes.put("/config-whatsapp/atualizar/{configwhatsapp_id}", dependencies=[Depends(check_token)])
async def atualizar_configwhatsapp(configwhatsapp_id: int, body: ConfigWhatsappSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"config_whatsapp_id": configwhatsapp_id})
    configwhatsapp_atualizar = configwhatsapp_atualizar_composer(db)

    http_response = await configwhatsapp_atualizar.handle_atualizar_configwhatsapp(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@configwhatsapp_routes.delete("/config-whatsapp/deletar/{configwhatsapp_id}", dependencies=[Depends(check_token)])
async def deletar_configwhatsapp(configwhatsapp_id: int, db: Session = Depends(get_session_db)):    
    view = configwhatsapp_deletar_composer(db)

    http_request = HttpRequest(param={"config_whatsapp_id": configwhatsapp_id})
    http_response = await view.handle_deletar_configwhatsapp(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
