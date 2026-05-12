from src.models.repositories.foto_repository import FotoRepository
from src.controllers.foto_inserir_controller import FotoInserirController
from src.views.foto_inserir_view import FotoInserirView
from sqlalchemy.orm import Session

def foto_inserir_composer(db: Session):
    model = FotoRepository(db)
    controller = FotoInserirController(model)
    view = FotoInserirView(controller)
    return view