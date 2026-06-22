from src.errors.error_handler import error_handler
from src.controllers.interfaces.config_whatsapp_visualizar_controller import ConfigWhatsappVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ConfigWhatsappVisualizarView:
    def __init__(self, controller: ConfigWhatsappVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_configwhatsapp(self, http_request: HttpRequest) -> HttpResponse:
        try:
            configwhatsapp_id = http_request.param.get("config_whatsapp_id")
            body_response = await self.__controller.visualizar(configwhatsapp_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
