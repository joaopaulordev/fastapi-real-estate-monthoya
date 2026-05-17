from src.models.repositories.tipo_imovel_repository import TipoImovelRepository
from src.controllers.tipo_imovel_listar_controller import TipoImovelListarController
from src.views.tipo_imovel_listar_view import TipoImovelListarView
from sqlalchemy.orm import Session

def tipo_imovel_listar_composer(db: Session):
    model = TipoImovelRepository(db)
    controller = TipoImovelListarController(model)
    view = TipoImovelListarView(controller)

    return view