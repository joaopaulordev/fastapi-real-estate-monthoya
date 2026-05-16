from src.models.repositories.interessado_repository import InteressadoRepository
from src.controllers.interessado_listar_controller import InteressadoListarController
from src.views.interessado_listar_view import InteressadoListarView
from sqlalchemy.orm import Session

def interessado_listar_composer(db: Session):
    model = InteressadoRepository(db)
    controller = InteressadoListarController(model)
    view = InteressadoListarView(controller)

    return view