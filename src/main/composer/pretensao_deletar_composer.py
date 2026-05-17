from src.models.repositories.pretensao_repository import PretensaoRepository
from src.controllers.pretensao_deletar_controller import PretensaoDeletarController
from src.views.pretensao_deletar_view import PretensaoDeletarView
from sqlalchemy.orm import Session

def pretensao_deletar_composer(db: Session):
    model = PretensaoRepository(db)
    controller = PretensaoDeletarController(model)
    view = PretensaoDeletarView(controller)

    return view