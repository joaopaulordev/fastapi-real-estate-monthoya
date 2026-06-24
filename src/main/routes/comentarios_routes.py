from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import ComentarioSchema
from src.models.settings.dependencies import get_session_db, check_token
from src.views.http_types.http_request import HttpRequest
from src.main.composer.comentario_inserir_composer import comentario_inserir_composer
from src.main.composer.comentario_listar_composer import comentario_listar_composer
from src.main.composer.comentario_visualizar_composer import comentario_visualizar_composer
from src.main.composer.comentario_atualizar_composer import comentario_atualizar_composer
from src.main.composer.comentario_deletar_composer import comentario_deletar_composer

comentario_routes = APIRouter(tags=["Comentários"], dependencies=[Depends(check_token)])

@comentario_routes.post("/comentarios/adicionar/{imovel_id}")
async def adicionar_comentario(imovel_id: int, body: ComentarioSchema, db: Session = Depends(get_session_db)):
    comentario_inserir = comentario_inserir_composer(db)

    http_response = await comentario_inserir.handle_inserir_comentario(HttpRequest(body={"imovel_id": imovel_id, "texto": body.texto}))
    
    return JSONResponse(
        content= http_response.body,
        status_code=http_response.status_code
     )    


@comentario_routes.get("/comentarios/listar/{imovel_id}")
async def listar_comentarios(imovel_id: int, db: Session = Depends(get_session_db)):    
    view = comentario_listar_composer(db)

    http_request = HttpRequest(param={"imovel_id": imovel_id})
    http_response = await view.handle_listar_comentarios(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@comentario_routes.get("/comentarios/visualizar/{comentario_id}")
async def visualizar_comentario(comentario_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"comentario_id": comentario_id})
    view = comentario_visualizar_composer(db)

    http_response = await view.handle_visualizar_comentario(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@comentario_routes.put("/comentarios/atualizar/{comentario_id}")
async def atualizar_comentario(comentario_id: int, body: ComentarioSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"comentario_id": comentario_id})
    comentario_atualizar = comentario_atualizar_composer(db)

    http_response = await comentario_atualizar.handle_atualizar_comentario(http_request)

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@comentario_routes.delete("/comentarios/deletar/{comentario_id}")
async def deletar_comentario(comentario_id: int, db: Session = Depends(get_session_db)):    
    view = comentario_deletar_composer(db)

    http_request = HttpRequest(param={"comentario_id": comentario_id})
    http_response = await view.handle_deletar_comentario(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
