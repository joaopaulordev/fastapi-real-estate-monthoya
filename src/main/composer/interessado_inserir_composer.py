from src.models.repositories.interessado_repository import InteressadoRepository
from src.controllers.interessado_inserir_controller import InteressadoInserirController
from src.views.interessado_inserir_view import InteressadoInserirView
from sqlalchemy.orm import Session

def interessado_inserir_composer(db: Session):
    model = InteressadoRepository(db)
    controller = InteressadoInserirController(model)
    view = InteressadoInserirView(controller)
    return view