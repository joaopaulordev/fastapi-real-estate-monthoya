from src.errors.error_handler import error_handler
from src.controllers.interfaces.config_whatsapp_listar_controller import ConfigWhatsappListarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ConfigWhatsappListarView:
    def __init__(self, controller: ConfigWhatsappListarControllerInterface) -> None:
        self.__controller = controller

    async def handle_listar_configwhatsapps(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body_response = await self.__controller.listar()
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
