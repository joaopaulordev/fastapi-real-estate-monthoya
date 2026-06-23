from src.errors.error_handler import error_handler
from src.controllers.interfaces.imovel_buscar_similares_controller import ImovelBuscarSimilaresControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ImovelBuscarSimilaresView:
    def __init__(self, controller: ImovelBuscarSimilaresControllerInterface) -> None:
        self.__controller = controller

    async def handle_buscar_similares_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_id = http_request.param.get("imovel_id")
            body_response = await self.__controller.buscar_similares(imovel_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
