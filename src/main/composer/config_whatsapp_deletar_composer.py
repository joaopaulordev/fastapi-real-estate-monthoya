from src.models.repositories.config_whatsapp_repository import ConfigWhatsappRepository
from src.controllers.config_whatsapp_deletar_controller import ConfigWhatsappDeletarController
from src.views.config_whatsapp_deletar_view import ConfigWhatsappDeletarView
from sqlalchemy.orm import Session

def configwhatsapp_deletar_composer(db: Session):
    model = ConfigWhatsappRepository(db)
    controller = ConfigWhatsappDeletarController(model)
    view = ConfigWhatsappDeletarView(controller)

    return view