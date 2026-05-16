from src.models.repositories.comentario_repository import ComentarioRepository
from src.controllers.comentario_inserir_controller import ComentarioInserirController
from src.views.comentario_inserir_view import ComentarioInserirView
from sqlalchemy.orm import Session

def comentario_inserir_composer(db: Session):
    model = ComentarioRepository(db)
    controller = ComentarioInserirController(model)
    view = ComentarioInserirView(controller)
    return view