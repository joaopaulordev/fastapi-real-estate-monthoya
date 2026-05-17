from src.errors.error_handler import error_handler
from src.controllers.interfaces.tipo_imovel_visualizar_controller import TipoImovelVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class TipoImovelVisualizarView:
    def __init__(self, controller: TipoImovelVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_tipo_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            tipo_imovel_id = http_request.param.get("tipo_imovel_id")
            body_response = await self.__controller.visualizar(tipo_imovel_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
