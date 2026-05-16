from src.controllers.interfaces.finalidade_inserir_controller import FinalidadeInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class FinalidadeInserirView:
    def __init__(self, controller: FinalidadeInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_finalidade(self, http_request: HttpRequest) -> HttpResponse:
        try:            
            finalidade_data = http_request.body
            response = await self.__controller.inserir(finalidade_data)               
            return HttpResponse(body=response, status_code=201)         
        except Exception as exception:
            error_handler(exception)