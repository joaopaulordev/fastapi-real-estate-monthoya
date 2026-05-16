from src.controllers.interfaces.comentario_atualizar_controller import ComentarioAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ComentarioAtualizarView:
    def __init__(self, controller: ComentarioAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_comentario(self, http_request: HttpRequest) -> HttpResponse:
        try:
            comentario_data = {"id": http_request.param.get("comentario_id"), **http_request.body}
            response = await self.__controller.atualizar(comentario_data)
            return HttpResponse(body=response, status_code=200)            
        except Exception as exception:
            error_handler(exception)