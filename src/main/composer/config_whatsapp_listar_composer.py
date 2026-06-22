from src.models.repositories.config_whatsapp_repository import ConfigWhatsappRepository
from src.controllers.config_whatsapp_listar_controller import ConfigWhatsappListarController
from src.views.config_whatsapp_listar_view import ConfigWhatsappListarView
from sqlalchemy.orm import Session

def configwhatsapp_listar_composer(db: Session):
    model = ConfigWhatsappRepository(db)
    controller = ConfigWhatsappListarController(model)
    view = ConfigWhatsappListarView(controller)

    return view