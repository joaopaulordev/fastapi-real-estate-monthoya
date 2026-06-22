from src.models.repositories.config_whatsapp_repository import ConfigWhatsappRepository
from src.controllers.config_whatsapp_atualizar_controller import ConfigWhatsappAtualizarController
from src.views.config_whatsapp_atualizar_view import ConfigWhatsappAtualizarView
from sqlalchemy.orm import Session

def configwhatsapp_atualizar_composer(db: Session):
    model = ConfigWhatsappRepository(db)
    controller = ConfigWhatsappAtualizarController(model)
    view = ConfigWhatsappAtualizarView(controller)
    return view