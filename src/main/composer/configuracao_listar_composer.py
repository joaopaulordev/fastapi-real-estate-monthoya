from src.models.repositories.configuracao_repository import ConfiguracaoRepository
from src.controllers.configuracao_listar_controller import ConfiguracaoListarController
from src.views.configuracao_listar_view import ConfiguracaoListarView
from sqlalchemy.orm import Session

def configuracao_listar_composer(db: Session):
    model = ConfiguracaoRepository(db)
    controller = ConfiguracaoListarController(model)
    view = ConfiguracaoListarView(controller)

    return view