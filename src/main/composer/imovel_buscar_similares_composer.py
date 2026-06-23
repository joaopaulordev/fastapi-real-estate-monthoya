from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_buscar_similares_controller import ImovelBuscarSimilaresController
from src.views.imovel_buscar_similares_view import ImovelBuscarSimilaresView
from sqlalchemy.orm import Session

def imovel_buscarsimilares_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelBuscarSimilaresController(model)
    view = ImovelBuscarSimilaresView(controller)

    return view