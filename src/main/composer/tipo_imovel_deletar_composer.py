from src.models.repositories.tipo_imovel_repository import TipoImovelRepository
from src.controllers.tipo_imovel_deletar_controller import TipoImovelDeletarController
from src.views.tipo_imovel_deletar_view import TipoImovelDeletarView
from sqlalchemy.orm import Session

def tipo_imovel_deletar_composer(db: Session):
    model = TipoImovelRepository(db)
    controller = TipoImovelDeletarController(model)
    view = TipoImovelDeletarView(controller)

    return view