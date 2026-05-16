from src.models.repositories.comentario_repository import ComentarioRepository
from src.controllers.comentario_deletar_controller import ComentarioDeletarController
from src.views.comentario_deletar_view import ComentarioDeletarView
from sqlalchemy.orm import Session

def comentario_deletar_composer(db: Session):
    model = ComentarioRepository(db)
    controller = ComentarioDeletarController(model)
    view = ComentarioDeletarView(controller)

    return view