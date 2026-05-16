from src.errors.error_handler import error_handler
from src.controllers.interfaces.finalidade_visualizar_controller import FinalidadeVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class FinalidadeVisualizarView:
    def __init__(self, controller: FinalidadeVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_finalidade(self, http_request: HttpRequest) -> HttpResponse:
        try:
            finalidade_id = http_request.param.get("finalidade_id")
            body_response = await self.__controller.visualizar(finalidade_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
