from src.controllers.interfaces.interessado_atualizar_controller import InteressadoAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class InteressadoAtualizarView:
    def __init__(self, controller: InteressadoAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_interessado(self, http_request: HttpRequest) -> HttpResponse:
        try:
            interessado_data = {"id": http_request.param.get("interessado_id"), **http_request.body}
            response = await self.__controller.atualizar(interessado_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)