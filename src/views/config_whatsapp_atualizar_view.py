from src.controllers.interfaces.config_whatsapp_atualizar_controller import ConfigWhatsappAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ConfigWhatsappAtualizarView:
    def __init__(self, controller: ConfigWhatsappAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_configwhatsapp(self, http_request: HttpRequest) -> HttpResponse:
        try:
            configwhatsapp_data = {"id": http_request.param.get("config_whatsapp_id"), "ativo": http_request.body.get("ativo"), "mensagem": http_request.body.get("mensagem"), "telefone": http_request.body.get("telefone")}
            response = await self.__controller.atualizar(configwhatsapp_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)