from src.models.repositories.foto_repository import FotoRepository
from src.controllers.foto_deletar_controller import FotoDeletarController
from src.views.foto_deletar_view import FotoDeletarView
from sqlalchemy.orm import Session

def foto_deletar_composer(db: Session):
    model = FotoRepository(db)
    controller = FotoDeletarController(model)
    view = FotoDeletarView(controller)

    return view