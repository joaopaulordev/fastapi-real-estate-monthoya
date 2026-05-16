from src.errors.error_handler import error_handler
from src.controllers.interfaces.interessado_listar_controller import InteressadoListarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class InteressadoListarView:
    def __init__(self, controller: InteressadoListarControllerInterface) -> None:
        self.__controller = controller

    async def handle_listar_interessados(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body_response = await self.__controller.listar(http_request.param["imovel_id"])
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
