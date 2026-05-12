from src.errors.error_handler import error_handler
from src.controllers.interfaces.foto_deletar_controller import FotoDeletarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class FotoDeletarView:
    def __init__(self, controller: FotoDeletarControllerInterface) -> None:
        self.__controller = controller

    async def handle_deletar_foto(self, http_request: HttpRequest) -> HttpResponse:
        try:
            foto_id = http_request.param.get("foto_id")
            body_response = await self.__controller.deletar(foto_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
