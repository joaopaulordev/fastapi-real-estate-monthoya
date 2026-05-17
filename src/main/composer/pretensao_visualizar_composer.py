from src.models.repositories.pretensao_repository import PretensaoRepository
from src.controllers.pretensao_visualizar_controller import PretensaoVisualizarController
from src.views.pretensao_visualizar_view import PretensaoVisualizarView
from sqlalchemy.orm import Session

def pretensao_visualizar_composer(db: Session):
    model = PretensaoRepository(db)
    controller = PretensaoVisualizarController(model)
    view = PretensaoVisualizarView(controller)

    return view