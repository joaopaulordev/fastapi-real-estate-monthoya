from src.models.repositories.tipo_imovel_repository import TipoImovelRepository
from src.controllers.tipo_imovel_visualizar_controller import TipoImovelVisualizarController
from src.views.tipo_imovel_visualizar_view import TipoImovelVisualizarView
from sqlalchemy.orm import Session

def tipo_imovel_visualizar_composer(db: Session):
    model = TipoImovelRepository(db)
    controller = TipoImovelVisualizarController(model)
    view = TipoImovelVisualizarView(controller)

    return view