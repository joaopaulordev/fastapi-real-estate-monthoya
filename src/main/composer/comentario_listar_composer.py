from src.models.repositories.comentario_repository import ComentarioRepository
from src.controllers.comentario_listar_controller import ComentarioListarController
from src.views.comentario_listar_view import ComentarioListarView
from sqlalchemy.orm import Session

def comentario_listar_composer(db: Session):
    model = ComentarioRepository(db)
    controller = ComentarioListarController(model)
    view = ComentarioListarView(controller)

    return view