from src.models.repositories.finalidade_repository import FinalidadeRepository
from src.controllers.finalidade_visualizar_controller import FinalidadeVisualizarController
from src.views.finalidade_visualizar_view import FinalidadeVisualizarView
from sqlalchemy.orm import Session

def finalidade_visualizar_composer(db: Session):
    model = FinalidadeRepository(db)
    controller = FinalidadeVisualizarController(model)
    view = FinalidadeVisualizarView(controller)

    return view