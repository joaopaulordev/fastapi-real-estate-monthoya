from src.models.repositories.interessado_repository import InteressadoRepository
from src.controllers.interessado_visualizar_controller import InteressadoVisualizarController
from src.views.interessado_visualizar_view import InteressadoVisualizarView
from sqlalchemy.orm import Session

def interessado_visualizar_composer(db: Session):
    model = InteressadoRepository(db)
    controller = InteressadoVisualizarController(model)
    view = InteressadoVisualizarView(controller)

    return view