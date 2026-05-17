from src.models.repositories.pretensao_repository import PretensaoRepository
from src.controllers.pretensao_inserir_controller import PretensaoInserirController
from src.views.pretensao_inserir_view import PretensaoInserirView
from sqlalchemy.orm import Session

def pretensao_inserir_composer(db: Session):
    model = PretensaoRepository(db)
    controller = PretensaoInserirController(model)
    view = PretensaoInserirView(controller)
    return view