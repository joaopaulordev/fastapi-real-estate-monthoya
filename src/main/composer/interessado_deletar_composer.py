from src.models.repositories.interessado_repository import InteressadoRepository
from src.controllers.interessado_deletar_controller import InteressadoDeletarController
from src.views.interessado_deletar_view import InteressadoDeletarView
from sqlalchemy.orm import Session

def interessado_deletar_composer(db: Session):
    model = InteressadoRepository(db)
    controller = InteressadoDeletarController(model)
    view = InteressadoDeletarView(controller)

    return view