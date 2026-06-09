from src.errors.error_handler import error_handler
from src.controllers.interfaces.configuracao_listar_controller import ConfiguracaoListarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ConfiguracaoListarView:
    def __init__(self, controller: ConfiguracaoListarControllerInterface) -> None:
        self.__controller = controller

    async def handle_listar_configuracoes(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body_response = await self.__controller.listar()
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
