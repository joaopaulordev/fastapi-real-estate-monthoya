from src.models.repositories.finalidade_repository import FinalidadeRepository
from src.controllers.finalidade_inserir_controller import FinalidadeInserirController
from src.views.finalidade_inserir_view import FinalidadeInserirView
from sqlalchemy.orm import Session

def finalidade_inserir_composer(db: Session):
    model = FinalidadeRepository(db)
    controller = FinalidadeInserirController(model)
    view = FinalidadeInserirView(controller)
    return view