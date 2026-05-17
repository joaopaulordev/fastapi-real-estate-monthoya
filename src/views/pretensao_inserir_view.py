from src.controllers.interfaces.pretensao_inserir_controller import PretensaoInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class PretensaoInserirView:
    def __init__(self, controller: PretensaoInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_pretensao(self, http_request: HttpRequest) -> HttpResponse:
        try:            
            pretensao_data = http_request.body
            response = await self.__controller.inserir(pretensao_data)               
            return HttpResponse(body=response, status_code=201)         
        except Exception as exception:
            error_handler(exception)