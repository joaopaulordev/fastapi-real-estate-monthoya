from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.models.settings.dependencies import get_session_db
from src.views.http_types.http_request import HttpRequest
from src.errors.types.http_not_found_error import HttpNotFoundError
import os
from typing import List
from src.main.composer.foto_inserir_composer import foto_inserir_composer
from src.main.composer.foto_listar_composer import foto_listar_composer
from src.main.composer.foto_deletar_composer import foto_deletar_composer


fotos_routes = APIRouter(tags=["Fotos"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@fotos_routes.post("/fotos/adicionar/{imovel_id}")
async def adicionar_fotos(imovel_id: int, files: List[UploadFile] = File(...), db: Session = Depends(get_session_db)):
    foto_inserir = foto_inserir_composer(db)

    for file in files:        
        file_path = os.path.join(UPLOAD_DIR, str(imovel_id) + "-" + file.filename)        
        await foto_inserir.handle_inserir_foto(HttpRequest(body={"imovel_id": imovel_id, "caminho": file_path}))
        
        content = await file.read()        
        with open(file_path, "wb") as f:
            f.write(content)
    
    return {"message": f"Uploaded {len(files)} fotos com sucesso."}


@fotos_routes.get("/fotos/listar/{imovel_id}")
async def listar_fotos(imovel_id: int, db: Session = Depends(get_session_db)):    
    view = foto_listar_composer(db)

    http_request = HttpRequest(param={"imovel_id": imovel_id})
    http_response = await view.handle_listar_fotos(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@fotos_routes.delete("/fotos/deletar/{foto_id}")
async def deletar_foto(foto_id: int, db: Session = Depends(get_session_db)):    
    view = foto_deletar_composer(db)

    http_request = HttpRequest(param={"foto_id": foto_id})
    http_response = await view.handle_deletar_foto(http_request)
    
    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
