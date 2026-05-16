from src.errors.error_handler import error_handler
from src.controllers.interfaces.comentario_visualizar_controller import ComentarioVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ComentarioVisualizarView:
    def __init__(self, controller: ComentarioVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_comentario(self, http_request: HttpRequest) -> HttpResponse:
        try:
            comentario_id = http_request.param.get("comentario_id")
            body_response = await self.__controller.visualizar(comentario_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
