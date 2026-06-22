from src.models.repositories.config_whatsapp_repository import ConfigWhatsappRepository
from src.controllers.config_whatsapp_inserir_controller import ConfigWhatsappInserirController
from src.views.config_whatsapp_inserir_view import ConfigWhatsappInserirView
from sqlalchemy.orm import Session

def configwhatsapp_inserir_composer(db: Session):
    model = ConfigWhatsappRepository(db)
    controller = ConfigWhatsappInserirController(model)
    view = ConfigWhatsappInserirView(controller)
    return view