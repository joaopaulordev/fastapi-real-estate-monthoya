from src.models.repositories.finalidade_repository import FinalidadeRepository
from src.controllers.finalidade_atualizar_controller import FinalidadeAtualizarController
from src.views.finalidade_atualizar_view import FinalidadeAtualizarView
from sqlalchemy.orm import Session

def finalidade_atualizar_composer(db: Session):
    model = FinalidadeRepository(db)
    controller = FinalidadeAtualizarController(model)
    view = FinalidadeAtualizarView(controller)
    return view