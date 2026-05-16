from src.models.repositories.comentario_repository import ComentarioRepository
from src.controllers.comentario_atualizar_controller import ComentarioAtualizarController
from src.views.comentario_atualizar_view import ComentarioAtualizarView
from sqlalchemy.orm import Session

def comentario_atualizar_composer(db: Session):
    model = ComentarioRepository(db)
    controller = ComentarioAtualizarController(model)
    view = ComentarioAtualizarView(controller)
    return view