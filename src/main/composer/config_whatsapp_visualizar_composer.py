from src.models.repositories.config_whatsapp_repository import ConfigWhatsappRepository
from src.controllers.config_whatsapp_visualizar_controller import ConfigWhatsappVisualizarController
from src.views.config_whatsapp_visualizar_view import ConfigWhatsappVisualizarView
from sqlalchemy.orm import Session

def configwhatsapp_visualizar_composer(db: Session):
    model = ConfigWhatsappRepository(db)
    controller = ConfigWhatsappVisualizarController(model)
    view = ConfigWhatsappVisualizarView(controller)

    return view