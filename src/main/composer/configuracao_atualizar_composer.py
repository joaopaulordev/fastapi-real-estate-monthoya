from src.models.repositories.configuracao_repository import ConfiguracaoRepository
from src.controllers.configuracao_atualizar_controller import ConfiguracaoAtualizarController
from src.views.configuracao_atualizar_view import ConfiguracaoAtualizarView
from sqlalchemy.orm import Session

def configuracao_atualizar_composer(db: Session):
    model = ConfiguracaoRepository(db)
    controller = ConfiguracaoAtualizarController(model)
    view = ConfiguracaoAtualizarView(controller)
    return view