from src.errors.error_handler import error_handler
from src.controllers.interfaces.finalidade_deletar_controller import FinalidadeDeletarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class FinalidadeDeletarView:
    def __init__(self, controller: FinalidadeDeletarControllerInterface) -> None:
        self.__controller = controller

    async def handle_deletar_finalidade(self, http_request: HttpRequest) -> HttpResponse:
        try:
            finalidade_id = http_request.param.get("finalidade_id")
            body_response = await self.__controller.deletar(finalidade_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
