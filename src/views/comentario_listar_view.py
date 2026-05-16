from src.errors.error_handler import error_handler
from src.controllers.interfaces.comentario_listar_controller import ComentarioListarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ComentarioListarView:
    def __init__(self, controller: ComentarioListarControllerInterface) -> None:
        self.__controller = controller

    async def handle_listar_comentarios(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body_response = await self.__controller.listar(http_request.param["imovel_id"])
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
