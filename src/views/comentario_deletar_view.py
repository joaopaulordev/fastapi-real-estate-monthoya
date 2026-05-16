from src.errors.error_handler import error_handler
from src.controllers.interfaces.comentario_deletar_controller import ComentarioDeletarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ComentarioDeletarView:
    def __init__(self, controller: ComentarioDeletarControllerInterface) -> None:
        self.__controller = controller

    async def handle_deletar_comentario(self, http_request: HttpRequest) -> HttpResponse:
        try:
            comentario_id = http_request.param.get("comentario_id")
            body_response = await self.__controller.deletar(comentario_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
