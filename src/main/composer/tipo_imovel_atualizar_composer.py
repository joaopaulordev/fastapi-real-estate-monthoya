from src.models.repositories.tipo_imovel_repository import TipoImovelRepository
from src.controllers.tipo_imovel_atualizar_controller import TipoImovelAtualizarController
from src.views.tipo_imovel_atualizar_view import TipoImovelAtualizarView
from sqlalchemy.orm import Session

def tipo_imovel_atualizar_composer(db: Session):
    model = TipoImovelRepository(db)
    controller = TipoImovelAtualizarController(model)
    view = TipoImovelAtualizarView(controller)
    return view