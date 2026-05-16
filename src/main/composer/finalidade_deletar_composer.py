from src.models.repositories.finalidade_repository import FinalidadeRepository
from src.controllers.finalidade_deletar_controller import FinalidadeDeletarController
from src.views.finalidade_deletar_view import FinalidadeDeletarView
from sqlalchemy.orm import Session

def finalidade_deletar_composer(db: Session):
    model = FinalidadeRepository(db)
    controller = FinalidadeDeletarController(model)
    view = FinalidadeDeletarView(controller)

    return view