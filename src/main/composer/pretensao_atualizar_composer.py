from src.models.repositories.pretensao_repository import PretensaoRepository
from src.controllers.pretensao_atualizar_controller import PretensaoAtualizarController
from src.views.pretensao_atualizar_view import PretensaoAtualizarView
from sqlalchemy.orm import Session

def pretensao_atualizar_composer(db: Session):
    model = PretensaoRepository(db)
    controller = PretensaoAtualizarController(model)
    view = PretensaoAtualizarView(controller)
    return view