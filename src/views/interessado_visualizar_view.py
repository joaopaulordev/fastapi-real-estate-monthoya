from src.errors.error_handler import error_handler
from src.controllers.interfaces.interessado_visualizar_controller import InteressadoVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class InteressadoVisualizarView:
    def __init__(self, controller: InteressadoVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_interessado(self, http_request: HttpRequest) -> HttpResponse:
        try:
            interessado_id = http_request.param.get("interessado_id")
            body_response = await self.__controller.visualizar(interessado_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
