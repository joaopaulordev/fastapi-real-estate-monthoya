from src.controllers.interfaces.configuracao_atualizar_controller import ConfiguracaoAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ConfiguracaoAtualizarView:
    def __init__(self, controller: ConfiguracaoAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_configuracao(self, http_request: HttpRequest) -> HttpResponse:
        try:
            configuracao_data = {"id": http_request.param.get("configuracao_id"), "quantidade": http_request.body.get("quantidade")}
            response = await self.__controller.atualizar(configuracao_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)