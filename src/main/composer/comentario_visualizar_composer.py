from src.models.repositories.comentario_repository import ComentarioRepository
from src.controllers.comentario_visualizar_controller import ComentarioVisualizarController
from src.views.comentario_visualizar_view import ComentarioVisualizarView
from sqlalchemy.orm import Session

def comentario_visualizar_composer(db: Session):
    model = ComentarioRepository(db)
    controller = ComentarioVisualizarController(model)
    view = ComentarioVisualizarView(controller)

    return view