from src.models.repositories.foto_repository import FotoRepository
from src.controllers.foto_listar_controller import FotoListarController
from src.views.foto_listar_view import FotoListarView
from sqlalchemy.orm import Session

def foto_listar_composer(db: Session):
    model = FotoRepository(db)
    controller = FotoListarController(model)
    view = FotoListarView(controller)

    return view