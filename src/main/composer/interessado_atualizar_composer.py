from src.models.repositories.interessado_repository import InteressadoRepository
from src.controllers.interessado_atualizar_controller import InteressadoAtualizarController
from src.views.interessado_atualizar_view import InteressadoAtualizarView
from sqlalchemy.orm import Session

def interessado_atualizar_composer(db: Session):
    model = InteressadoRepository(db)
    controller = InteressadoAtualizarController(model)
    view = InteressadoAtualizarView(controller)
    return view