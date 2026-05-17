from src.controllers.interfaces.tipo_imovel_inserir_controller import TipoImovelInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class TipoImovelInserirView:
    def __init__(self, controller: TipoImovelInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_tipo_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:            
            tipo_imovel_data = http_request.body
            response = await self.__controller.inserir(tipo_imovel_data)               
            return HttpResponse(body=response, status_code=201)         
        except Exception as exception:
            error_handler(exception)