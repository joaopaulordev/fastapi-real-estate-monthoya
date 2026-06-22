from fastapi import APIRouter, Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.models.settings.dependencies import get_session_db
from src.views.http_types.http_request import HttpRequest
from src.errors.types.http_not_found_error import HttpNotFoundError
import os
from src.main.composer.imovel_atualizar_composer import imovel_atualizar_composer
from src.main.composer.imovel_visualizar_composer import imovel_visualizar_composer


foto_localizacao_routes = APIRouter(tags=["Foto Localização"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@foto_localizacao_routes.put("/foto-localizacao/adicionar/{imovel_id}")
async def adicionar_foto_localizacao(imovel_id: int, localizacao_desc: str = Form(...), file: UploadFile = File(...), db: Session = Depends(get_session_db)):
    imovel_atualizar = imovel_atualizar_composer(db)

    file_path = os.path.join(UPLOAD_DIR, str(imovel_id) + "-localizacao-" + file.filename)     
    content = await file.read()        
    with open(file_path, "wb") as f:
        f.write(content)

    new_http_request = HttpRequest(body={"localizacao_desc": localizacao_desc, "localizacao_img": file_path}, param={"imovel_id": imovel_id})
    http_response = await imovel_atualizar.handle_atualizar_imovel(new_http_request)    

    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@foto_localizacao_routes.put("/foto-localizacao/deletar/{imovel_id}")
async def deletar_foto_localizacao(imovel_id: int, db: Session = Depends(get_session_db)):       
    http_request = HttpRequest(param={"imovel_id": imovel_id})
    imovel_visualizar = imovel_visualizar_composer(db)
    http_response = await imovel_visualizar.handle_visualizar_imovel(http_request, False)
    file_path = http_response.body["imovel"]["localizacao_img"]   
    if os.path.exists(file_path):
        os.remove(file_path)

    imovel_atualizar = imovel_atualizar_composer(db)
    http_request = HttpRequest(body={ }, param={"imovel_id": imovel_id})
    http_response = await imovel_atualizar.handle_atualizar_imovel(http_request, True) 
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
