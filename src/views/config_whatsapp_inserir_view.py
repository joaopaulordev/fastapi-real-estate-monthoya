from src.controllers.interfaces.config_whatsapp_inserir_controller import ConfigWhatsappInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ConfigWhatsappInserirView:
    def __init__(self, controller: ConfigWhatsappInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_configwhatsapp(self, http_request: HttpRequest) -> HttpResponse:
        try:            
            configwhatsapp_data = http_request.body
            response = await self.__controller.inserir(configwhatsapp_data)               
            return HttpResponse(body=response, status_code=201)         
        except Exception as exception:
            error_handler(exception)