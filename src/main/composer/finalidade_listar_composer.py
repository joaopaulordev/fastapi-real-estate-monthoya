from src.models.repositories.finalidade_repository import FinalidadeRepository
from src.controllers.finalidade_listar_controller import FinalidadeListarController
from src.views.finalidade_listar_view import FinalidadeListarView
from sqlalchemy.orm import Session

def finalidade_listar_composer(db: Session):
    model = FinalidadeRepository(db)
    controller = FinalidadeListarController(model)
    view = FinalidadeListarView(controller)

    return view