from src.models.repositories.pretensao_repository import PretensaoRepository
from src.controllers.pretensao_listar_controller import PretensaoListarController
from src.views.pretensao_listar_view import PretensaoListarView
from sqlalchemy.orm import Session

def pretensao_listar_composer(db: Session):
    model = PretensaoRepository(db)
    controller = PretensaoListarController(model)
    view = PretensaoListarView(controller)

    return view