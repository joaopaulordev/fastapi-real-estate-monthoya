from src.errors.error_handler import error_handler
from src.controllers.interfaces.tipo_imovel_deletar_controller import TipoImovelDeletarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class TipoImovelDeletarView:
    def __init__(self, controller: TipoImovelDeletarControllerInterface) -> None:
        self.__controller = controller

    async def handle_deletar_tipo_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            tipo_imovel_id = http_request.param.get("tipo_imovel_id")
            body_response = await self.__controller.deletar(tipo_imovel_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
