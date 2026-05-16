from src.controllers.interfaces.interessado_inserir_controller import InteressadoInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class InteressadoInserirView:
    def __init__(self, controller: InteressadoInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_interessado(self, http_request: HttpRequest) -> HttpResponse:
        try:
            interessado_data = {"imovel_id": http_request.param.get("imovel_id"), **http_request.body}
            response = await self.__controller.inserir(interessado_data)               
            return HttpResponse(body=response, status_code=201)         
        except Exception as exception:
            error_handler(exception)