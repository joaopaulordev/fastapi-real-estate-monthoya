from src.models.repositories.tipo_imovel_repository import TipoImovelRepository
from src.controllers.tipo_imovel_inserir_controller import TipoImovelInserirController
from src.views.tipo_imovel_inserir_view import TipoImovelInserirView
from sqlalchemy.orm import Session

def tipo_imovel_inserir_composer(db: Session):
    model = TipoImovelRepository(db)
    controller = TipoImovelInserirController(model)
    view = TipoImovelInserirView(controller)
    return view